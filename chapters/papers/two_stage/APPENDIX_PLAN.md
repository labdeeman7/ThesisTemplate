# Proposed Chapter 5 Supplementary Appendix

The main chapter is intentionally concise. The following material should be added immediately after the main chapter during the next milestone.

## A. Prompt and response specifications

- Completed in `appendix_body.tex`: Direct SFT instructions and schema; shared vocabularies and null-class serialisation; the three-stage Sequential Dialogue Prediction prompts; the complete ontology-guidance content; the authoritative teacher-generation prompt and structured rationale schema; and the two multitask evaluation modes.
- The appendix excludes the unused instrument-identification dialogue turn, the superseded mixed Direct-SFT/sequential dataset version, and obsolete early rationale templates.

## B. Instrument-tip context heuristic

- Completed in `appendix_body.tex`: field-of-view estimation, boundary-based instrument-base estimation, furthest-mask-point tip selection, the 12.5% disk definition, instrument-mask exclusion, candidate-radius selection note, EndoViT argmax-label proportions, failure behaviour, and the exact textual-prior format.
- The representative successful and ambiguous-tip examples remain in the main chapter; no duplicate appendix figure was added.

## C. Training configuration summary

- Completed in `appendix_body.tex`: the common QLoRA and optimisation table, official validation/checkpoint protocol, adaptation-specific deviations, and the shared total visual-token budget across single-frame and temporal inputs.
- No unsupported numerical pixel limits or unenforced text sequence-length limit are reported.

## D. Distilled rationale examples and quality-control scope

- Completed in `appendix_body.tex`: one unedited final-schema example (`t50_VID14_000126_reasoning`), the distinction between label-conditioned supervision generation and independent prediction, the approximately ten-example informal inspection scope, absence of clinician validation, and equal rationale/answer token weighting.

## E. Secondary and optimisation results

- Completed: the full five-configuration optimisation-sensitivity study has been moved from the main chapter to `appendix_body.tex`, including all metrics and the warning that several variables change simultaneously.
- Completed: row-normalised action and target confusion matrices for the official test-set predictions of Direct SFT, three-frame temporal context, and Multitask---Direct SFT evaluation, with descriptive interpretation and explicit single-seed caveats.
- Optional secondary negative-result table if the main chapter is later shortened for journal submission.

## F. Additional qualitative material

- A blank qualitative-figure panel is reserved in `appendix_body.tex` for later replacement with carefully selected official test-set examples illustrating temporal action ambiguity, anatomically ambiguous targets, and a possible annotation inconsistency.
- Any available examples of malformed or omitted outputs should be labelled qualitative only because their frequency was not measured systematically.
