# Proposed Chapter 5 Supplementary Appendix

The main chapter is intentionally concise. The following material should be added immediately after the main chapter during the next milestone.

## A. Prompt and response specifications

- Direct SFT instruction template.
- Complete verb and target vocabularies.
- Structured output schema, including `null_verb` and `null_target`.
- Sequential Dialogue Prediction training and inference templates.
- Ontology-Guided Prompting template and an example instrument-specific verb--target list.
- Distilled Reasoning Supervision teacher, student, and evaluation instructions.

Insert appendix references from the Stage 2 input, Sequential Dialogue Prediction, Ontology-Guided Prompting, and Distilled Reasoning Supervision subsections once labels exist.

## B. Instrument-tip context heuristic

- Stepwise distal-tip estimation procedure.
- Definition of the circular region with radius 12.5% of the smaller image dimension.
- Candidate-radius selection note.
- The representative image is now included in the main chapter; the appendix may add further examples if they provide distinct information.
- EndoViT class-ranking and textual-prior construction example.

Insert an appendix reference from the Anatomical Context Priors subsection once the representative image is supplied.

## C. Training configuration summary

- Compact table of the common QLoRA and optimisation settings.
- Adaptation-specific deviations: dialogue structure, temporal input, anatomical text, ontology text, and supervision mixture.
- Visual-token budget statement for single-frame and shared-budget temporal inputs.

## D. Distilled rationale examples and quality-control scope

- One or more complete teacher-generated examples.
- Explicit statement that approximately ten rationales were inspected informally without clinician validation.
- Explanation of equal rationale/answer token weighting.

## E. Secondary and optimisation results

- Completed: the full five-configuration optimisation-sensitivity study has been moved from the main chapter to `appendix_body.tex`, including all metrics and the warning that several variables change simultaneously.
- Candidate confusion matrices, explicitly excluded from the main chapter. Their final appendix selection will be decided during appendix drafting.
- Optional secondary negative-result table if the main chapter is later shortened for journal submission.

## F. Additional qualitative material

- Carefully selected outputs illustrating successful and failed predictions, if an existing defensible set can be recovered.
- Any available examples of malformed or omitted outputs should be labelled qualitative only because their frequency was not measured systematically.
