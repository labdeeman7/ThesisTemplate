# Thesis-Integrated Paper Sources

These files adapt accepted manuscripts for the thesis while preserving the original paper projects for independent compilation.

## Literature Review

- **Integrated file:** `chapters/papers/02_review_paper.tex`
- **Authoritative accepted source:** `phd_papers/sources/Multitask_Learning_in_Minimally_Invasive_Surgical_Vision__A_Review_submitted/main-clean.tex`
- **Source commit/version:** `bc0de77da96993e55888b45058c0dc79b7fc1b38`
- **Integration changes:** standalone class/preamble, publisher front matter, and bibliography commands omitted; wrapper supplies title/authors/abstract and figure path; citation keys harmonised. For the thesis layout only, inherited two-column `figure*` floats were converted to flexible single-column figures, narrow column-sized diagrams were enlarged for thesis readability, and the exceptionally wide dataset summary was placed on a landscape page. Local emergency line-breaking tolerance is applied by the wrapper. Captions, figure content, table rows, values, and scientific prose are unchanged.
- **Scientific-content changes:** none.
- **Canonical citation-key substitutions:**
  - `ConvLSTM` to `convLSTM`
  - `9772402` to `multi_fov`
  - `islam2019real` to `real_time_seg_adverserial`
  - `krizhevsky2017imagenet` to `alexnet`
  - `rivas2021review` to `mis_survey`

## CholecInstanceSeg

- **Thesis wrapper:** `chapters/03_cholecinstanceseg.tex`
- **Integrated manuscript components:** `chapters/papers/cholecinstanceseg/`
- **Authoritative accepted source:** `phd_papers/sources/Scientific_data_cholecInstance_seg/`
- **Source commit/version:** `bc0de77da96993e55888b45058c0dc79b7fc1b38`
- **Integration changes:** standalone `wlscirep` class/preamble, publisher author/affiliation commands, `\maketitle`, standalone document boundaries, and standalone bibliography command omitted; wrapper supplies thesis chapter context, accepted-paper title/authors, final-revision macros, and figure path. The accepted component files are copied into the thesis integration layer. The abstract environment is represented as an unnumbered thesis subsection. Canonical citation keys are harmonised only in these copied files.
- **Preserved manuscript material:** abstract; Background & Summary; Methods; Data Records; Technical Validation; Code Availability; Acknowledgements; Author Contributions; Competing Interests; all seven active figures, four active tables, three displayed equations, and 41 citation commands.
- **Supplementary material:** none incorporated. The accepted source contains no appendix or active supplementary file; its revision response records that the earlier annotation-guide supplement was removed from the manuscript.
- **Intentional omissions:** publisher class/front matter and standalone bibliography machinery; commented-out draft figures/tables; `usage_notes.tex`, whose heading and complete contents are wrapped in the accepted manuscript's deletion macro and therefore absent from the final accepted text.
- **Scientific-content changes:** none.
- **Canonical citation-key substitutions:**
  - `endovis2015` to `bodenstedt2018comparative`
  - `cheng2021mask2former` to `cheng2022masked`
  - `endonet` to `EndoNet`

## TargetFusionNet

- **Thesis wrapper:** `chapters/04_triplet_grounding.tex`
- **Integrated manuscript components:** `chapters/papers/targetfusionnet/main_body.tex` and `chapters/papers/targetfusionnet/appendix_body.tex`
- **Authoritative accepted source:** `phd_papers/sources/Surgical Action Triplet Segmentation IPCAI/`
- **Source commit/version:** `bc0de77da96993e55888b45058c0dc79b7fc1b38`
- **Integration changes:** standalone Springer `sn-jnl` class/preamble, revision-display machinery, publisher author/affiliation commands, line numbering, `\maketitle`, standalone document boundaries, and standalone bibliography commands omitted. The wrapper supplies the accepted title/authors/abstract/keywords, final-revision macros, paper macros, figure path, thesis chapter context, and thesis-written introduction and transition. `booktabs`, `bm`, and `subcaption` are loaded by the thesis for manuscript tables and appendix subfigures.
- **Preserved manuscript material:** complete accepted main body and complete written appendix, including declarations; 16 section commands, 4 subsection commands, 8 active figures, 9 active tables, 2 displayed equations, and 47 citation commands across the paper and appendix.
- **Supplementary material:** the complete written appendix is incorporated. The main paper refers to a supplementary comparison video, but no video file is present in the authoritative accepted-source directory, so it cannot be embedded in the thesis repository.
- **Intentional omissions:** publisher/template preambles and guidance, standalone title/front-matter commands, line numbers, standalone bibliography machinery, and the appendix's duplicate standalone title page. No active scientific section, figure, table, equation, citation, declaration, or written appendix content is omitted.
- **Label namespacing:** the generic `sec::introduction` label is changed to `sec:tfn:introduction` in the thesis copy to avoid a genuine collision with Chapter 2; no rendered text changes.
- **Scientific-content changes:** none. After reversing the documented citation-key and label substitutions, both integrated source bodies match the authoritative main manuscript and appendix exactly.
- **Canonical citation-key substitutions:**
  - `nwoye2020recognition` to `1nywoye_rec_action_triplets`
  - `nwoye2022rendezvous` to `NWOYE2022102433_rendevous`
  - `alabi2025cholecinstanceseg` to `cholecinstanceseg`
  - `hong2020cholecseg8k` to `cholecseg8k`
  - `he2016deep` to `resnet`
  - `yamlahi2023self` to `multi_self_distillation`
  - `sharma2023rendezvous` to `sharma2022RendezvousInTime`

## Two Stage Surgical Triplet Segmentation

- **Planned thesis chapter:** Chapter 5 (not yet integrated in this migration)
- **Chapter-specific record:** `chapters/papers/two_stage/README.md`
- **Authoritative source:** `phd_papers/sources/Two_Stage_Surgical_Triplet_Segmentation/`
- **Source commit/version:** `f04030e1832710fc66579b6ceeef2a868decb805`
- **Integration changes:** none yet. Its bibliography records have been consolidated so that the later thesis-specific integration can use the canonical bibliography without changing this authoritative project.
- **Obsolete predecessor:** preserved under `archive/chapter5/`; it is historical context only and is not a thesis source.
