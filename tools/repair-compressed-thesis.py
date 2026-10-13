"""Replace empty RGB ICC profiles using the valid sRGB profile in the same PDF.

Preserves the submitted input and checks text and rendered pixels on every page.
This validation uses MuPDF; opening the result in Acrobat is a separate check.
"""
from pathlib import Path
import hashlib
import json
import re
import fitz
from PIL import ImageCms
import io

source = Path('Thesis-review-compressed.pdf')
target = Path('Thesis-review-compressed-corrected.pdf')
if target.exists():
    raise SystemExit(f'Refusing to overwrite {target}')
original_hash = hashlib.sha256(source.read_bytes()).hexdigest()
doc = fitz.open(source)
references = set()
for xref in range(1, doc.xref_length()):
    references.update(int(x) for x in re.findall(
        r'/ICCBased\s+(\d+)\s+0\s+R', doc.xref_object(xref)))
empty_rgb = []
valid_srgb = None
for xref in sorted(references):
    _, components = doc.xref_get_key(xref, 'N')
    if components != '3':
        continue
    profile = doc.xref_stream(xref)
    if not profile:
        empty_rgb.append(xref)
    else:
        description = ImageCms.getProfileDescription(ImageCms.ImageCmsProfile(io.BytesIO(profile)))
        if 'srgb' in description.lower():
            valid_srgb = profile
if not empty_rgb or valid_srgb is None:
    raise SystemExit('Expected empty RGB profiles and an existing valid sRGB profile were not found')
for xref in empty_rgb:
    doc.update_stream(xref, valid_srgb)
doc.save(target, garbage=3, deflate=True)
doc.close()

old = fitz.open(source)
new = fitz.open(target)
assert len(old) == len(new) == 248
assert old.metadata == new.metadata, 'PDF metadata changed'
assert old.get_toc() == new.get_toc(), 'Bookmarks changed'
fitz.TOOLS.mupdf_warnings()
issues = []
different_pixels = []
different_text = []
for index in range(len(old)):
    before = old[index].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
    before_text = old[index].get_text()
    fitz.TOOLS.mupdf_warnings()
    after = new[index].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
    after_text = new[index].get_text()
    warnings = fitz.TOOLS.mupdf_warnings()
    if warnings:
        issues.append({'pdf_page': index + 1, 'warnings': warnings})
    if before_text != after_text:
        different_text.append(index + 1)
    if (before.width, before.height, before.samples) != (after.width, after.height, after.samples):
        different_pixels.append(index + 1)
assert hashlib.sha256(source.read_bytes()).hexdigest() == original_hash
report = {'input': str(source), 'output': str(target), 'input_sha256': original_hash,
          'output_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
          'repaired_empty_rgb_profile_objects': empty_rgb, 'pages': len(new),
          'input_bytes': source.stat().st_size, 'output_bytes': target.stat().st_size,
          'metadata_preserved': True, 'bookmarks_preserved': True,
          'pages_with_text_differences': different_text,
          'pages_with_pixel_differences_at_72dpi': different_pixels,
          'corrected_pdf_warnings': issues,
          'validation_engine': 'MuPDF; Acrobat not automatically verified'}
Path('.build/compressed-pdf-repair-report.json').write_text(
    json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
old.close()
new.close()
if different_text or different_pixels:
    raise SystemExit('Review required: output differs from recovered input rendering or text')
