# Chapter 5: Two-Stage Multimodal Interaction Prediction

## Authoritative source

- Manuscript: `phd_papers/sources/Two_Stage_Surgical_Triplet_Segmentation/main.tex`
- Figures: `phd_papers/sources/Two_Stage_Surgical_Triplet_Segmentation/figures/`
- Preserved source milestone: `f04030e1832710fc66579b6ceeef2a868decb805`
- Current thesis wrapper: `chapters/05_two_stage_interaction_prediction.tex`

The authoritative project is an active manuscript rather than an accepted-paper archive. Its scientific and structural blueprint was approved before the first complete thesis-integrated draft was created.

## Thesis integration

- Integrated main body: `chapters/papers/two_stage/main_body.tex`
- Thesis wrapper: `chapters/05_two_stage_interaction_prediction.tex`
- First-draft editorial report: `chapters/papers/two_stage/EDITORIAL_DRAFT_REPORT.md`
- Supplementary appendix plan: `chapters/papers/two_stage/APPENDIX_PLAN.md`

The integrated body is a substantive editorial reconstruction rather than a preservation copy. It retains all completed experiments and numerical results while reorganising them around the approved two-stage scientific narrative. It does not modify the authoritative active-manuscript project.

## Authoritative figures reviewed

- `two_stage_pipeline.pdf`: the complete Mask2Former grounding and Qwen3-VL interaction-prediction pipeline.
- `adaptation_motivation.pdf`: anatomical ambiguity, missing temporal evidence, ontology-invalid outputs, and insufficient visual evidence.
- `sequential_dialogue_prediction.pdf`: direct prediction compared with verb-first, target-second sequential dialogue prediction.
- `distilled_reasoning_supervision.pdf`: teacher rationale generation and student supervision. This supports a compact negative-results subsection and is not the chapter's central framing.
- `instrument_tip_prior-examples.pdf`: representative successful and ambiguous cases for the heuristic instrument-tip anatomical-context extraction.

## Archived material

The previous `Qwen_work` manuscript, its PDF, the old thesis scaffold, target-centric chain-of-thought tables and prompts, and unused or unrelated assets are preserved under `archive/chapter5/`. See `archive/chapter5/README.md` for the complete inventory and rationale.

## Source-of-truth rule

Only `Two_Stage_Surgical_Triplet_Segmentation/main.tex` and its four referenced figures are authoritative for active Chapter 5 content. Archived material is historical context only and must not be copied into the chapter unless the user explicitly reinstates it.

The thesis-integrated draft additionally incorporates the scientific decisions and implementation specification agreed in the project conversation. Where that specification supersedes incomplete wording or tables in the authoritative draft, the integrated source records the completed evidence without altering the original project.
