# Chapter 5 First-Draft Editorial Record

## Structural changes

- Reframed the chapter around the two-stage system rather than the chronological development of experiments.
- Added a thesis-specific abstract and an introduction connecting Chapters 2--4 to the final technical contribution.
- Organised Methods into problem formulation, fixed Stage 1 grounding, structured Stage 2 prediction, Direct SFT, and controlled adaptations.
- Separated principal Stage 2 results from exploratory and distilled-supervision results.
- Positioned the complete predicted-grounding pipeline as a central result.
- Separated Discussion, Limitations, Future Research, and Conclusion.

## Substantive editorial decisions

- Made the two-stage formulation, not target-centric chain-of-thought, the central contribution.
- Used interaction prediction for the empirical task and reserved reasoning terminology for the established distilled-supervision concept or broad motivation.
- Treated Direct SFT as the principal baseline and retained its five-epoch configuration for controlled adaptation comparisons.
- Described Sequential Dialogue Prediction and three-frame temporal context as promising observed AP_IVT improvements, not definitive superiority.
- Reported the five-frame study as an exploratory negative result because the fixed visual budget makes it an uncontrolled temporal-window comparison.
- Reported Anatomical Context Priors as mixed and explicitly avoided claiming improved target classification.
- Added the previously omitted Ontology-Guided Prompting and multitask distilled-rationale results.
- Renamed the multitask result rows exactly as requested: `Multitask---Direct SFT` and `Multitask---Distilled Rationale`.
- Clarified that the two multitask rows are inference modes of the same trained model.
- Treated the rationale-token dominance explanation as a hypothesis rather than an established cause.
- Reduced optimisation analysis to sensitivity evidence and reserved the complete table for the appendix.
- Described the complete two-stage AP_IVT as comparable to TargetFusionNet; no improvement claim is made for the 0.07-point difference.
- Explicitly separated Stage 1 AP_I from MLLM performance.
- Referred to Chapters 3 and 4 for inherited detector and IVTMetrics details instead of duplicating them.
- Restricted immediate future work to directions arising directly from completed evidence.

## Outstanding author decisions

1. Confirm whether the centre frame was explicitly identified in the temporal prompt or inferred from its ordered position.
2. Supply the representative instrument-tip/circular-context image intended for the anatomical-prior method.
3. Decide whether to add formal citations for Qwen3-VL-8B-Instruct and the closed-weight Qwen3.7-Max service model. No suitable records currently exist in the canonical thesis bibliography.
4. Decide whether existing confusion matrices should be selected for the supplementary appendix. They are not required for the main narrative.

## Statements requiring final evidential review

- The word `viable` is supported by the completed benchmark results but remains a qualitative interpretation rather than a pre-specified acceptance threshold.
- The proposed coherence interpretation for Sequential Dialogue Prediction is plausible but untested because verb-to-target error propagation was not quantified.
- Temporal explanations involving motion or procedural progression are consistent with the task and observed metrics but were not isolated experimentally.
- Hypotheses about rationale-token dominance, prompt use of ontology information, and the anatomical representation are not causal findings.
- Component-level comparison with TargetFusionNet is numerically supported, but all cross-method interpretations remain limited by single-seed Chapter 5 evaluation.

## Terminology decisions

- `Direct SFT`, `Sequential Dialogue Prediction`, `Temporal Visual Context`, `Anatomical Context Priors`, `Ontology-Guided Prompting`, and `Distilled Reasoning Supervision` are retained from the active manuscript.
- `Multitask---Direct SFT` and `Multitask---Distilled Rationale` are the approved result labels.
- `interaction prediction` denotes the evaluated task; `multimodal interaction reasoning` is not used as a separate measured capability.
