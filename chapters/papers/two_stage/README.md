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
- Active supplementary appendix: `chapters/papers/two_stage/appendix_body.tex` (currently contains the complete optimisation-sensitivity study; the remaining planned material will be added during the appendix milestone).
- Prompt appendix provenance: Direct SFT is derived from `phd_papers/code/prompts/baseline.py`; ontology guidance from `constraint_100.py`; the final distilled-rationale teacher instruction and schema from `cot_reasoning_target.py`; and Sequential Dialogue Prediction from the action, target, and final-triplet turns in `multi_turn_decomposition.py`, as confirmed by the author.
- Prompt-version exclusions: the unused instrument-identification turn and earlier mixed Direct-SFT/sequential dataset snapshot are not part of the reported Sequential Dialogue Prediction experiment. `reasoning.py` and `cot_reasoning_old.py` contain obsolete rationale schemas and are retained only as historical implementation artifacts.
- Anatomical-prior appendix provenance: the stepwise field-of-view, instrument-base, distal-tip, local-disk, EndoViT aggregation, and prompt-format descriptions are reconstructed from `phd_papers/code/utils/endovit_text_prior.py`. This corrected the earlier high-level statement that a separate shaft-orientation estimate was used.
- Training-configuration appendix provenance: the common Direct SFT and three-frame launch settings were recovered from the author-supplied training commands and trainers, then reconciled with the author's confirmation that the official validation split was used for checkpoint selection and that all temporal windows shared the same total visual budget. Smoke-test split naming and plaintext credentials in the archival scripts are not reproduced in the thesis.
- Distilled-rationale example provenance: the appendix reproduces the generated response for `t50_VID14_000126_reasoning` from `phd_papers/artifacts/prompts/sft_test_reasoning.jsonl`. It is included only to illustrate the final structured supervision schema and is not presented as clinically validated reasoning or an independent prediction.
- Error-analysis provenance: the appendix uses the official test-set, row-normalised action and target confusion matrices recovered from `phd_papers/artifacts/To Zijie.pptx`. The author confirmed the three configurations as Direct SFT, three-frame temporal context, and the multitask model evaluated with the Direct SFT instruction. The presentation remains an archival provenance source and is not loaded by the thesis.

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
