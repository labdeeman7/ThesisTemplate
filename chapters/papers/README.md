# Thesis-Integrated Paper Sources

These files adapt accepted manuscripts for the thesis while preserving the original paper projects for independent compilation.

## Literature Review

- **Integrated file:** `chapters/papers/02_review_paper.tex`
- **Authoritative accepted source:** `phd_papers/sources/Multitask_Learning_in_Minimally_Invasive_Surgical_Vision__A_Review_submitted/main-clean.tex`
- **Source commit/version:** `bc0de77da96993e55888b45058c0dc79b7fc1b38`
- **Integration changes:** standalone class/preamble, publisher front matter, abstract, acknowledgements/declarations, funding/open-access text, and bibliography commands are omitted. Thesis framing is merged into the numbered Introduction, and the accepted conclusion is extended to state the chapter's thesis-level finding and transition to Chapter 3. Citation keys are harmonised. For the thesis layout only, inherited two-column `figure*` floats were converted to flexible single-column figures, narrow column-sized diagrams were enlarged for thesis readability, and the exceptionally wide dataset summary was placed on a landscape page.
- **Scientific-content preservation:** the review methodology, survey body, datasets, figures, tables, citations, and substantive discussion are retained.
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
- **Integration changes:** standalone `wlscirep` class/preamble, publisher author/affiliation commands, `\maketitle`, abstract, acknowledgements, funding/open-access text, author contributions, competing interests, standalone document boundaries, and bibliography command are omitted. The thesis framing is merged with `Background & Summary` as one numbered Introduction; the scientific headings are numbered for thesis navigation; and a thesis conclusion connects the dataset contribution to Chapter 4. Canonical citation keys are harmonised only in the copied files.
- **Preserved manuscript material:** Introduction/Background & Summary; Methods; Data Records; Technical Validation; Code Availability; all seven active main-manuscript figures, four active tables, three displayed equations, and 41 citation commands.
- **Authoritative supplementary source:** `phd_papers/sources/CholecInstanceSEg Supplementary Materials/main.tex`, verified against `phd_papers/pdfs/CholecInstanceSEg_Supplementary_Materials.pdf`.
- **Supplementary material:** all eight substantive annotation-guideline figures are incorporated as the numbered end-of-chapter section `Detailed Annotation Guidelines for Challenging Cases`. Labels are namespaced and figures retain `S1`--`S8` numbering; the figure content and accepted captions are preserved.
- **Intentional omissions:** publisher class/front matter and standalone bibliography machinery; commented-out draft figures/tables; `usage_notes.tex`, whose heading and complete contents are wrapped in the accepted manuscript's deletion macro and therefore absent from the final accepted text; the supplementary PDF's final empty title page, headed `More Evaluation metrics for baseline models`, because it contains no scientific content, table, figure, metric, or accompanying text.
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
- **Integration changes:** standalone Springer `sn-jnl` class/preamble, publisher front matter, abstract, keywords, declarations/interests, ethics/funding/open-access boilerplate, line numbering, standalone document boundaries, and bibliography commands are omitted. Thesis framing is merged into the numbered Introduction, and the accepted discussion/conclusion is extended with the thesis transition to Chapter 5.
- **Preserved manuscript material:** the complete accepted scientific main body and written scientific appendix, including 8 active figures, 9 active tables, 2 displayed equations, and 47 citation commands.
- **Promoted material:** extended dataset construction and annotation, dataset statistics, EndoViT weak supervision, implementation and metric details, fusion/multitask/depth ablations, efficiency, long-tail performance, and failure analysis are now ordinary numbered chapter sections before the discussion/conclusion. No paper-style appendix remains.
- **Intentional omissions:** publisher/template machinery, paper abstract/keywords, administrative declarations, and the appendix's duplicate standalone title page. The paper refers to a supplementary comparison video, but no video file is present in the authoritative accepted-source directory.
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

- **Thesis chapter:** Chapter 5
- **Chapter-specific record:** `chapters/papers/two_stage/README.md`
- **Authoritative source:** `phd_papers/sources/Two_Stage_Surgical_Triplet_Segmentation/`
- **Source commit/version:** `f04030e1832710fc66579b6ceeef2a868decb805`
- **Integration changes:** the chapter-level abstract and manuscript source-note box are omitted; the existing Introduction and Conclusion form the sole opening and ending. The complete Stage 2 training configuration is integrated into Methods and the confusion-matrix analysis into Results. Complete prompts, the detailed tip heuristic, the distilled-rationale example and quality-control scope, and optimisation sensitivity remain in the chapter-specific `Additional Methodological and Experimental Details` section. The canonical thesis bibliography is used without modifying the authoritative project.
- **Obsolete predecessor:** preserved under `archive/chapter5/`; it is historical context only and is not a thesis source.
