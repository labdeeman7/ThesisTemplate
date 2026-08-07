"""Build weak text priors from EndoViT target logits around instruments."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from endovit import (
    ENDOVIT_NUM_CLASSES,
    ENDOVIT_PROMPT_CLASS_NAMES,
    ENDOVIT_TARGET_CLASSES,
)


@dataclass(frozen=True)
class EndoViTPriorConfig:
    """Configuration for local EndoViT text-prior extraction."""

    use_endovit_text_prior: bool = False
    endovit_prior_region: str = "tip_disk"
    endovit_bbox_scale: float = 1.6
    endovit_bbox_padding: int | None = None
    tip_disk_radius: int | None = None
    tip_disk_radius_fraction: float = 1.0 / 8.0
    endovit_prior_topk: int = 3
    endovit_ignore_channels: tuple[int, ...] = (0, 7, 8)
    endovit_logits_dir: Path | None = None
    endovit_resize_mismatched_logits: bool = False
    tip_boundary_margin: int = 20
    tip_fallback_mode: str = "none"
    make_endovit_semantic_maps: bool = False
    make_endovit_bbox_debug: bool = False
    save_tip_debug_images: bool = False


@dataclass(frozen=True)
class EndoViTPrior:
    """Computed prior summary for one instrument instance."""

    instance_id: str
    bbox_xyxy: tuple[int, int, int, int]
    top_classes: tuple[tuple[str, float], ...]
    region: str
    expanded_bbox_xyxy: tuple[int, int, int, int] | None = None
    tip_xy: tuple[int, int] | None = None
    base_xy: tuple[float, float] | None = None
    disk_radius: int | None = None
    fov_center_xy: tuple[float, float] | None = None
    fov_radius: float | None = None
    boundary_pixels_xy: tuple[tuple[int, int], ...] = ()
    mask: np.ndarray | None = None
    tip_confidence: str = "failed"


def softmax_channel_first(logits: np.ndarray) -> np.ndarray:
    """Compute a numerically stable softmax over the channel axis."""

    shifted = logits - np.max(logits, axis=0, keepdims=True)
    exp = np.exp(shifted)
    return exp / np.sum(exp, axis=0, keepdims=True)


def expand_bbox(
    bbox_xyxy: Iterable[int],
    image_size_wh: tuple[int, int],
    scale: float,
    padding: int | None,
) -> tuple[int, int, int, int]:
    """Expand an xyxy box by scale or absolute padding and clip to the image."""

    x1, y1, x2, y2 = [int(v) for v in bbox_xyxy]
    width, height = image_size_wh

    if padding is not None:
        ex1, ey1, ex2, ey2 = x1 - padding, y1 - padding, x2 + padding, y2 + padding
    else:
        cx = (x1 + x2) / 2.0
        cy = (y1 + y2) / 2.0
        bw = max(1.0, (x2 - x1 + 1) * scale)
        bh = max(1.0, (y2 - y1 + 1) * scale)
        ex1 = int(round(cx - bw / 2.0))
        ey1 = int(round(cy - bh / 2.0))
        ex2 = int(round(cx + bw / 2.0))
        ey2 = int(round(cy + bh / 2.0))

    ex1 = max(0, min(ex1, width - 1))
    ey1 = max(0, min(ey1, height - 1))
    ex2 = max(0, min(ex2, width - 1))
    ey2 = max(0, min(ey2, height - 1))
    return ex1, ey1, ex2, ey2


def rasterize_instance_mask(
    polys: list,
    image_size_wh: tuple[int, int],
) -> np.ndarray:
    """Rasterize all LabelMe polygons for one instance into a binary mask."""

    width, height = image_size_wh
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    for poly in polys:
        if len(poly) >= 3:
            draw.polygon([tuple(map(float, pt)) for pt in poly], fill=255)
    return np.asarray(mask, dtype=np.uint8) > 0


def estimate_fov(rgb_image: Image.Image) -> tuple[tuple[float, float] | None, float | None, np.ndarray]:
    """Approximate the circular laparoscopic FOV from non-black image pixels."""

    rgb = np.asarray(rgb_image.convert("RGB"))
    valid = np.max(rgb, axis=2) > 12
    valid_ratio = float(valid.mean())
    if valid_ratio < 0.10:
        return None, None, valid

    ys, xs = np.nonzero(valid)
    if len(xs) < 100:
        return None, None, valid

    center = (float(np.median(xs)), float(np.median(ys)))
    distances = np.sqrt((xs - center[0]) ** 2 + (ys - center[1]) ** 2)
    radius = float(np.percentile(distances, 98))
    if not np.isfinite(radius) or radius < 20:
        return None, None, valid
    return center, radius, valid


def estimate_tip_from_mask(
    mask: np.ndarray,
    rgb_image: Image.Image,
    boundary_margin: int,
    fallback_mode: str = "none",
) -> dict:
    """Estimate instrument base and tip from a mask and the laparoscopic FOV."""

    height, width = mask.shape
    _, _, valid_pixels = estimate_fov(rgb_image)
    if not mask.any() or float(valid_pixels.mean()) < 0.10:
        return {"confidence": "failed"}

    center, radius, _ = estimate_fov(rgb_image)
    ys, xs = np.nonzero(mask)

    # Boundary candidates represent the likely shaft entry point. Prefer the
    # laparoscopic circular boundary, then fall back to image edges.
    image_edge = (
        (xs <= boundary_margin)
        | (ys <= boundary_margin)
        | (xs >= width - 1 - boundary_margin)
        | (ys >= height - 1 - boundary_margin)
    )
    if center is not None and radius is not None:
        dist_from_center = np.sqrt((xs - center[0]) ** 2 + (ys - center[1]) ** 2)
        fov_edge = dist_from_center >= max(0.0, radius - boundary_margin)
        boundary_selector = image_edge | fov_edge
    else:
        boundary_selector = image_edge

    if not np.any(boundary_selector):
        if fallback_mode != "centroid":
            return {"confidence": "failed", "fov_center_xy": center, "fov_radius": radius}
        base_x, base_y = float(xs.mean()), float(ys.mean())
        confidence = "low"
        boundary_xy: tuple[tuple[int, int], ...] = ()
    else:
        boundary_xs = xs[boundary_selector]
        boundary_ys = ys[boundary_selector]
        base_x, base_y = float(boundary_xs.mean()), float(boundary_ys.mean())
        confidence = "medium"
        sample_step = max(1, len(boundary_xs) // 200)
        boundary_xy = tuple(
            (int(x), int(y))
            for x, y in zip(boundary_xs[::sample_step], boundary_ys[::sample_step])
        )

    distances = (xs - base_x) ** 2 + (ys - base_y) ** 2
    tip_idx = int(np.argmax(distances))
    return {
        "confidence": confidence,
        "base_xy": (base_x, base_y),
        "tip_xy": (int(xs[tip_idx]), int(ys[tip_idx])),
        "fov_center_xy": center,
        "fov_radius": radius,
        "boundary_pixels_xy": boundary_xy,
    }


def disk_region_mask(
    image_shape_hw: tuple[int, int],
    center_xy: tuple[int, int],
    radius: int,
    exclude_mask: np.ndarray | None = None,
) -> np.ndarray:
    """Create a disk mask, optionally excluding instrument pixels."""

    height, width = image_shape_hw
    cx, cy = center_xy
    yy, xx = np.ogrid[:height, :width]
    disk = (xx - cx) ** 2 + (yy - cy) ** 2 <= radius**2
    if exclude_mask is not None:
        disk = disk & ~exclude_mask
    return disk


def mean_argmax_class_scores(
    probs: np.ndarray,
    region_mask: np.ndarray,
    candidate_channels: list[int],
    ignore_channels: tuple[int, ...],
) -> list[tuple[int, float]] | None:
    """Score classes by argmax-label proportions inside a valid region."""

    pred = np.argmax(probs, axis=0)
    valid_region = region_mask & ~np.isin(pred, ignore_channels)
    if not np.any(valid_region):
        return None

    return [
        (ch, float((pred[valid_region] == ch).mean()))
        for ch in candidate_channels
    ]


def resolve_tip_disk_radius(
    image_size_wh: tuple[int, int],
    config: EndoViTPriorConfig,
) -> int:
    """Resolve fixed or image-relative tip disk radius in pixels."""

    if config.tip_disk_radius is not None:
        return int(config.tip_disk_radius)
    width, height = image_size_wh
    return max(1, int(round(min(width, height) * config.tip_disk_radius_fraction)))


def load_logits(
    logits_path: Path,
    image_size_wh: tuple[int, int],
    allow_spatial_mismatch: bool = False,
) -> np.ndarray | None:
    """Load and validate EndoViT logits, returning None for unusable files."""

    if not logits_path.exists():
        return None

    try:
        with np.load(logits_path) as data:
            logits = data["logits"]
    except Exception:
        return None

    width, height = image_size_wh
    if logits.shape == (ENDOVIT_NUM_CLASSES, height, width):
        return logits.astype(np.float32, copy=False)
    if not allow_spatial_mismatch:
        return None
    if logits.ndim != 3 or logits.shape[0] != ENDOVIT_NUM_CLASSES:
        return None
    return logits.astype(np.float32, copy=False)


def resize_probs_to_image(probs: np.ndarray, image_size_wh: tuple[int, int]) -> np.ndarray:
    """Resize channel probabilities to image size and renormalize per pixel."""

    width, height = image_size_wh
    if probs.shape[1:] == (height, width):
        return probs

    resized = np.stack(
        [
            np.asarray(
                Image.fromarray(channel.astype(np.float32), mode="F").resize(
                    (width, height),
                    resample=Image.Resampling.BILINEAR,
                ),
                dtype=np.float32,
            )
            for channel in probs
        ],
        axis=0,
    )
    denom = np.maximum(resized.sum(axis=0, keepdims=True), 1e-6)
    return resized / denom


def compute_instance_prior(
    instance_id: str,
    bbox_xyxy: Iterable[int],
    probs: np.ndarray,
    config: EndoViTPriorConfig,
) -> EndoViTPrior | None:
    """Summarize top EndoViT anatomy probabilities inside one local region."""

    if config.endovit_prior_region != "expanded_bbox":
        return None

    _, height, width = probs.shape
    expanded = expand_bbox(
        bbox_xyxy=bbox_xyxy,
        image_size_wh=(width, height),
        scale=config.endovit_bbox_scale,
        padding=config.endovit_bbox_padding,
    )
    x1, y1, x2, y2 = expanded
    if x2 < x1 or y2 < y1:
        return None

    region = probs[:, y1 : y2 + 1, x1 : x2 + 1]
    if region.size == 0:
        return None

    candidate_channels = [
        ch
        for ch in ENDOVIT_PROMPT_CLASS_NAMES
        if ch not in set(config.endovit_ignore_channels)
    ]
    region_mask = np.zeros((height, width), dtype=bool)
    region_mask[y1 : y2 + 1, x1 : x2 + 1] = True
    means = mean_argmax_class_scores(
        probs=probs,
        region_mask=region_mask,
        candidate_channels=candidate_channels,
        ignore_channels=config.endovit_ignore_channels,
    )
    if means is None:
        return None
    means.sort(key=lambda item: item[1], reverse=True)
    top = tuple(
        (ENDOVIT_PROMPT_CLASS_NAMES[ch], prob)
        for ch, prob in means[: config.endovit_prior_topk]
    )

    return EndoViTPrior(
        instance_id=instance_id,
        bbox_xyxy=tuple(int(v) for v in bbox_xyxy),
        top_classes=top,
        region="expanded_bbox",
        expanded_bbox_xyxy=expanded,
        tip_confidence="medium",
    )


def compute_tip_disk_prior(
    instance_id: str,
    bbox_xyxy: Iterable[int],
    polys: list,
    probs: np.ndarray,
    image: Image.Image,
    config: EndoViTPriorConfig,
) -> EndoViTPrior | None:
    """Summarize EndoViT probabilities in tissue around the estimated tip."""

    if config.endovit_prior_region != "tip_disk":
        return None

    _, height, width = probs.shape
    mask = rasterize_instance_mask(polys=polys, image_size_wh=(width, height))
    tip_state = estimate_tip_from_mask(
        mask=mask,
        rgb_image=image,
        boundary_margin=config.tip_boundary_margin,
        fallback_mode=config.tip_fallback_mode,
    )
    if tip_state.get("confidence") in {None, "failed"}:
        return None

    tip_xy = tip_state["tip_xy"]
    radius = resolve_tip_disk_radius((width, height), config)
    region_mask = disk_region_mask(
        image_shape_hw=(height, width),
        center_xy=tip_xy,
        radius=radius,
        exclude_mask=mask,
    )
    if not np.any(region_mask):
        return None

    candidate_channels = [
        ch
        for ch in ENDOVIT_PROMPT_CLASS_NAMES
        if ch not in set(config.endovit_ignore_channels)
    ]
    means = mean_argmax_class_scores(
        probs=probs,
        region_mask=region_mask,
        candidate_channels=candidate_channels,
        ignore_channels=config.endovit_ignore_channels,
    )
    if means is None:
        return None
    means.sort(key=lambda item: item[1], reverse=True)
    top = tuple(
        (ENDOVIT_PROMPT_CLASS_NAMES[ch], prob)
        for ch, prob in means[: config.endovit_prior_topk]
    )

    return EndoViTPrior(
        instance_id=instance_id,
        bbox_xyxy=tuple(int(v) for v in bbox_xyxy),
        top_classes=top,
        region="tip_disk",
        tip_xy=tip_xy,
        base_xy=tip_state.get("base_xy"),
        disk_radius=radius,
        fov_center_xy=tip_state.get("fov_center_xy"),
        fov_radius=tip_state.get("fov_radius"),
        boundary_pixels_xy=tip_state.get("boundary_pixels_xy", ()),
        mask=mask,
        tip_confidence=tip_state.get("confidence", "failed"),
    )


def format_prior_block(priors: list[EndoViTPrior]) -> str:
    """Render per-instance EndoViT priors for insertion into the user prompt."""

    if not priors:
        return ""

    region = priors[0].region
    if region == "tip_disk":
        sections = [
            "Weak local anatomy prior from a separate segmentation model, computed near the estimated instrument tip:"
        ]
    else:
        sections = [
            "Weak local anatomy prior from a separate segmentation model, computed inside an expanded bounding box around the highlighted instrument:"
        ]
    for prior in priors:
        sections.append(f"Instance {prior.instance_id}:")
        for rank, (name, prob) in enumerate(prior.top_classes, start=1):
            sections.append(f"{rank}. {name}: {prob:.2f}")

    sections.append("")
    if region == "tip_disk":
        sections.append(
            "The tip location is estimated automatically and may be imperfect. The anatomy prior is weak and may be wrong. Pay close attention to the image first, and use this prior only as contextual supporting evidence. The final target must still be chosen from the surgical triplet target ontology."
        )
    else:
        sections.append(
            "This prior is local, weak, and may be wrong. Use it only as supporting evidence. The final target must still be chosen from the surgical triplet target ontology."
        )
    return "\n".join(sections)


def save_semantic_map(probs: np.ndarray, out_path: Path):
    """Write an RGB argmax semantic map for manual EndoViT inspection."""

    pred = np.argmax(probs, axis=0)
    height, width = pred.shape
    rgb = np.zeros((height, width, 3), dtype=np.uint8)
    for class_idx, meta in ENDOVIT_TARGET_CLASSES.items():
        rgb[pred == class_idx] = np.array(meta["color"], dtype=np.uint8)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(rgb, mode="RGB").save(out_path)


def _load_font(size: int = 18) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Load the repo font when available, otherwise use Pillow's default font."""

    for candidate in (
        Path("assets/fonts/DejaVuSans.ttf"),
        Path("/nfs/home/talabi/repositories/surg_prvit/assets/fonts/DejaVuSans.ttf"),
    ):
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def save_bbox_debug_image(image_path: Path, priors: list[EndoViTPrior], out_path: Path):
    """Draw expanded prior boxes and top probabilities on the source image."""

    if not priors:
        return

    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    font = _load_font()

    for prior in priors:
        x1, y1, x2, y2 = prior.expanded_bbox_xyxy
        draw.rectangle([x1, y1, x2, y2], outline=(255, 230, 0), width=3)

        label_lines = [prior.instance_id] + [
            f"{name}: {prob:.0%}" for name, prob in prior.top_classes
        ]
        text = "\n".join(label_lines)
        left, top, right, bottom = draw.multiline_textbbox((0, 0), text, font=font, spacing=2)
        text_w, text_h = right - left, bottom - top
        tx = min(max(0, x1), max(0, image.width - text_w - 8))
        ty = y1 - text_h - 10
        if ty < 0:
            ty = min(image.height - text_h - 8, y1 + 6)

        draw.rectangle(
            [tx - 4, ty - 4, tx + text_w + 4, ty + text_h + 4],
            fill=(0, 0, 0),
            outline=(255, 230, 0),
            width=1,
        )
        draw.multiline_text((tx, ty), text, fill=(255, 255, 255), font=font, spacing=2)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)


def save_tip_debug_image(image_path: Path, priors: list[EndoViTPrior], out_path: Path):
    """Draw masks, FOV, base/tip points, tip disks, and top prior text."""

    if not priors:
        return

    image = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    font = _load_font()

    for prior in priors:
        if prior.mask is not None:
            mask_img = Image.fromarray((prior.mask.astype(np.uint8) * 90), mode="L")
            color = Image.new("RGBA", image.size, (0, 220, 255, 0))
            color.putalpha(mask_img)
            overlay = Image.alpha_composite(overlay, color)
            draw = ImageDraw.Draw(overlay)

        if prior.fov_center_xy is not None and prior.fov_radius is not None:
            cx, cy = prior.fov_center_xy
            r = prior.fov_radius
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255, 140), width=2)

        for bx, by in prior.boundary_pixels_xy:
            draw.point((bx, by), fill=(255, 128, 0, 220))

        if prior.base_xy is not None:
            bx, by = prior.base_xy
            draw.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(255, 128, 0, 255))

        if prior.tip_xy is not None and prior.disk_radius is not None:
            tx, ty = prior.tip_xy
            r = prior.disk_radius
            draw.ellipse([tx - r, ty - r, tx + r, ty + r], outline=(255, 230, 0, 230), width=3)
            draw.ellipse([tx - 6, ty - 6, tx + 6, ty + 6], fill=(255, 0, 0, 255))

            label_lines = [prior.instance_id, f"tip: {prior.tip_confidence}"] + [
                f"{name}: {prob:.0%}" for name, prob in prior.top_classes
            ]
            text = "\n".join(label_lines)
            left, top, right, bottom = draw.multiline_textbbox((0, 0), text, font=font, spacing=2)
            text_w, text_h = right - left, bottom - top
            x1, y1, _, _ = prior.bbox_xyxy
            tx_label = min(max(0, x1), max(0, image.width - text_w - 8))
            ty_label = max(0, y1 - text_h - 10)
            draw.rectangle(
                [tx_label - 4, ty_label - 4, tx_label + text_w + 4, ty_label + text_h + 4],
                fill=(0, 0, 0, 210),
                outline=(255, 230, 0, 255),
                width=1,
            )
            draw.multiline_text((tx_label, ty_label), text, fill=(255, 255, 255, 255), font=font, spacing=2)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    Image.alpha_composite(image, overlay).convert("RGB").save(out_path)
