# Ten-minute thesis presentation

Open `Thesis_overview_10min.pptx` for an editable PowerPoint presentation, or `Thesis_overview_10min.pdf` to present immediately. Both contain exactly ten slides. Speaker notes are embedded in PowerPoint and available separately in `Thesis_overview_10min_notes.md`. Planned slide timings total 600 seconds; rehearse once to fit your own pace.

The presentation follows the current thesis title and narrative: review, instrument instance segmentation, grounded triplet data and TargetFusionNet, then two-stage multimodal interaction prediction. Slides 3–4 explain the review and its connection to the research gap. The final chapter uses the current two-stage manuscript, rather than archived Qwen work.

Validation: ten slides and ten PDF pages checked; notes present on every slide; the PDF layout and screenshots exported by the installed Microsoft PowerPoint were visually inspected.

## Existing presentations inspected

- `TPC presentation.pptx`: early review taxonomy and 2023 research plans. Used for context; the old PhD aims and draft review counts are superseded by the thesis.
- `poster_presentation.pptx`: CholecInstanceSeg dataset and annotation pipeline.
- `BII_reduced.pptx`: triplet task, dataset alignment, baselines, and TargetFusionNet.
- `Auditorium_2026-07-02_1500_Alabi_Oluwatosin_IPCAI-R-1291.pptx`: recent grounding narrative and figures. Used alongside the thesis sources.

Thesis figures are embedded as images; slide titles, text, cards and result values are editable. Exact figure and claim sources are recorded in `Thesis_overview_10min_sources.json` and the slide notes. The PDF was generated directly from the same slide content, so no LaTeX or Office installation is needed to use it.

## Interpretation of results

Complete-system mask-based triplet AP: Mask2Former-Triplet 12.23, TargetFusionNet 13.47, two-stage Direct SFT 13.52. The last two are comparable; the 0.05-point difference is not presented as an established gain. The higher 14.56, 15.31 and 15.89 results use ground-truth instrument prompting and are a separate Stage 2 evaluation. Only Direct SFT was evaluated with predicted instruments. Sequential dialogue and three-frame results are exploratory observations.

## Regenerate

From the repository root:

```powershell
.\.venv\Scripts\python.exe tools\build_thesis_overview.py
```

Required Python packages: `python-pptx`, `pymupdf`, `reportlab`, and `Pillow`. The script uses the Arial fonts installed with Windows.
