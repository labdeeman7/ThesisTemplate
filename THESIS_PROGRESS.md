# Thesis Progress

## Author read-through revisions

### Front-matter milestone

- Strengthened the abstract's opening logic by connecting the visual constraints of minimally invasive surgery to the need for structured computational scene understanding.
- Removed repeated single-seed emphasis from the abstract while retaining the important scope qualification that only Direct SFT was evaluated with predicted grounding.
- Expanded the acknowledgements to recognise the supervisors' belief and encouragement and the support of the author's siblings, Tolu and Tomi.

### Chapter 2 read-through milestone

- Replaced the compressed landscape dataset summary with a portrait multipage table with repeated headers, preserving every dataset row and field while allowing descriptions and names to wrap legibly.
- Clarified in the surgical action-triplet subsection that conventional triplet recognition is semantically fine-grained but primarily frame-level rather than strongly grounded to an individual physical instrument instance.
- Added an explicit cross-reference to this distinction in the chapter conclusion, strengthening the motivation for CholecInstanceSeg and the grounded technical chapters.

## Supervisor integration pass (Chapters 2--5)

### Chapter 2 milestone

- Integrated the literature review as a thesis chapter: removed the repeated paper title block, chapter-level abstract, accepted-manuscript heading, acknowledgements, declarations, funding, ethics, and open-access boilerplate.
- Merged the thesis framing into the chapter's numbered Introduction and replaced the duplicated paper conclusion/Chapter Summary with one conclusion that establishes the literature findings and motivates Chapter 3.
- Preserved the review methodology, technical survey, datasets, figures, tables, citations, and substantive discussion unchanged.
- Verified a converged full-thesis build after the Chapter 2 integration; no LaTeX or Biber errors were introduced.

### Chapter 3 milestone

- Integrated CholecInstanceSeg as a thesis chapter: removed the repeated paper title block, chapter abstract, accepted-manuscript heading, acknowledgements, funding/open-access text, author-contribution statement, and competing-interest declaration.
- Merged the thesis framing into a single numbered Introduction and converted the Scientific Data-style unnumbered scientific headings into numbered thesis sections and subsections.
- Retained the S1--S8 annotation guidance as the end-of-chapter section `Detailed Annotation Guidelines for Challenging Cases`, followed by one thesis conclusion that motivates Chapter 4.
- Preserved the dataset construction, data records, validation experiments, code availability, figures, tables, equations, citations, and annotation guidance; the archival `abstract.tex` remains in the repository but is no longer included.
- Verified a converged full-thesis build after the Chapter 3 integration; no LaTeX or Biber errors were introduced.

### Chapter 4 milestone

- Integrated TargetFusionNet as a thesis chapter: removed the repeated paper title/authors/journal block, structured abstract, keywords, accepted-manuscript labels, declarations, interests, ethics, funding, and open-access boilerplate.
- Merged the thesis framing into the numbered Introduction and integrated the former paper appendix into the main numbered scientific narrative before the discussion and conclusion.
- Promoted the extended dataset construction and annotation protocol, additional dataset statistics, EndoViT weak-supervision details, implementation details, evaluation protocol, fusion/multitask/depth ablations, efficiency analysis, long-tail results, and failure-mode analysis.
- Replaced paper-appendix signposting with references to the relevant later chapter analyses and extended the accepted conclusion only to articulate its role in the thesis and transition to Chapter 5.
- Preserved all scientific results, numerical values, figures, tables, equations, citations, limitations, and substantive accepted-paper appendix material.
- Verified a converged full-thesis build after the Chapter 4 integration; no LaTeX or Biber errors were introduced.

### Chapter 5 milestone

- Integrated the active two-stage manuscript as a thesis chapter: removed its chapter-level abstract, separate wrapper introduction, source-note box, paper-style supplementary heading, and duplicated wrapper summary.
- Retained the existing numbered Introduction as the sole chapter opening and extended the existing Conclusion only with the transition to the thesis-level discussion.
- Promoted the complete Stage 2 QLoRA/training configuration and adaptation-specific configuration table into the main methodology, and promoted the three paired confusion-matrix analyses into the main Results section.
- Retained complete prompts and response schemas, the detailed instrument-tip heuristic, the distilled-rationale example and quality-control scope, and the optimisation-sensitivity study in the chapter-specific `Additional Methodological and Experimental Details` section before the Conclusion.
- Preserved all methods, experiments, numerical results, figures, tables, citations, limitations, future-work directions, and scientific interpretation.
- Verified a converged full-thesis build after the Chapter 5 integration; no LaTeX or Biber errors were introduced.

### Cross-thesis consistency milestone

- Updated the List of Publications to describe Chapters 2--5 as integrated thesis chapters that draw on the listed publications/manuscript, rather than as accepted-paper cores pasted into wrappers.
- Updated the thesis-integration provenance README to record the removed publication boilerplate, merged introductions/conclusions, promoted Chapter 4 material, retained Chapter 3 guidance, and Chapter 5 main/supplementary division.
- Confirmed that the authoritative accepted-paper source projects remain unchanged; all integration edits are confined to thesis-specific wrappers and copied chapter sources.

### Final integration verification

- Forced a complete Biber/LaTeX rebuild to convergence. The integrated thesis builds successfully at 237 pages with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Confirmed that the active Chapter 2--5 sources contain no visible `Accepted Manuscript`, `Accepted Manuscript Appendix`, `Accepted Supplementary Material`, `Chapter Supplementary Appendix`, `Chapter Introduction`, or `Chapter Summary` headings.
- Compared the active scientific-source inventory with pre-integration commit `ef12ec5`: both versions contain 51 figure environments, 30 table environments, 14 displayed equation/alignment environments, and 512 citation commands.
- Confirmed one numbered Introduction and one concluding section in each integrated chapter; Chapter 3 retains S1--S8 annotation guidance, Chapter 4 retains all promoted scientific appendix material, and Chapter 5 retains its chapter-specific methodological details before its Conclusion.
- Remaining warnings are inherited layout/template diagnostics (underfull/overfull boxes, PDF-version inclusion notices, `fancyhdr` head-height notices, and four `nag` complaints); none is a citation, reference, bibliography, or build error.

This file records the working state of the thesis. It should be updated whenever significant work is completed.

## Completed Tasks

- Audited the repository structure without modifying files.
- Identified `Thesis.tex` as the main LaTeX entry point.
- Mapped the existing thesis chapters to their paper sources.
- Identified the obsolete `Qwen_work` project and confirmed that `Two_Stage_Surgical_Triplet_Segmentation` replaces it.
- Identified the current front-matter placeholders, incomplete conclusion, bibliography warnings, and mismatch between the adapted chapters and the required paper-based format.
- Agreed a staged completion plan that preserves the published papers and uses small, reviewable commits.
- Created this progress tracker and corrected the thesis source map to make Two Stage Surgical Triplet Segmentation authoritative.
- Preserved the complete Two Stage manuscript source, figures, bibliography, and reference PDF in version control without altering the manuscript.
- Audited the Two Stage manuscript for thesis integration requirements. Its standalone preamble must be removed or bypassed, figure paths must be made thesis-relative, and generic macros and labels must be isolated to prevent conflicts with earlier chapters.
- Reconstructed Chapter 2 around the complete accepted manuscript of the literature review, with a thesis-specific introduction and chapter transition.
- Archived the previous condensed literature-review chapter at `archive/chapters/02_background_adapted_2026-05-29.tex` rather than deleting it.
- Verified the reconstructed review chapter with an isolated LaTeX pass; the complete thesis reached 123 pages and all review figures were found.
- Repaired the bibliography data required for a complete thesis build: removed an unused malformed abstract, replaced invalid pseudo-comments, expanded undefined bibliography macros, corrected citation-key case mismatches, and namespaced duplicate manuscript entries without discarding them.
- Verified a complete converged `latexmk`/Biber/LaTeX build in an external temporary directory. The resulting thesis is 153 pages with no undefined citations, undefined references, LaTeX errors, or fatal Biber errors.
- Migrated the thesis to a single authoritative `ThesisBibliography.bib`, containing 317 canonical records consolidated from 377 source records without aliases or chapter-specific key suffixes.
- Recorded bibliography provenance, duplicate-key resolution, metadata differences, and canonical-record decisions in `THESIS_BIBLIOGRAPHY_PROVENANCE.md`.
- Restored the accepted-paper source directories and their local bibliographies to their archival source versions, preserving their independent compilation structure.
- Created a thesis-only accepted-review source at `chapters/papers/02_review_paper.tex` and documented all integration and citation-key substitutions in `chapters/papers/README.md`.
- Verified the consolidated thesis build to convergence: 152 pages, zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no Biber warnings or errors.
- Verified accepted-review fidelity: 59 sections, 16 figures, 11 tables, 8 equation environments, and 413 citation commands are preserved; after the five documented key substitutions, the accepted body and thesis-integrated body match exactly.
- Built the accepted literature-review and CholecInstanceSeg projects independently. TargetFusionNet remains independently structured but its build is blocked locally by the missing MiKTeX package `cuted.sty`, not by bibliography changes.
- Reviewed the completed Chapter 2 integration. Its accepted body remains an exact match after documented citation-key substitutions, and its thesis introduction and transition correctly establish the thesis narrative without rewriting the paper.
- Adopted a reusable paper-integration standard: a concise thesis wrapper plus copied manuscript components under `chapters/papers/<paper>/`, explicit source-version and exclusion records, thesis-only canonical-key substitutions, and an archived copy of any superseded adapted chapter.
- Recorded deferred Chapter 2 and Chapter 3 float, wide-table, page-break, and inherited display-math observations in `LAYOUT_TODO.md`; no formatting changes were made during the scientific-content integration.
- Reconstructed Chapter 3 from the authoritative accepted CholecInstanceSeg manuscript. The integrated copy preserves 5 substantive manuscript sections, 8 subsections, 21 subsubsections, 7 active figures, 4 active tables, 3 displayed equations, and 41 citation commands, plus the abstract and manuscript end matter.
- Archived the superseded adapted Chapter 3 at `archive/chapters/03_cholecinstanceseg_adapted_2026-08-05.tex`.
- Verified the complete Chapter 3 thesis build to convergence at 165 pages with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Reconstructed Chapter 4 from the authoritative accepted TargetFusionNet manuscript using the Chapter 3 integration architecture, with separate thesis wrapper and isolated accepted-paper components.
- Incorporated the complete accepted TargetFusionNet appendix, including extended dataset construction, statistics, weak-supervision details, evaluation definitions, ablations, efficiency analysis, long-tail analysis, and failure modes.
- Verified TargetFusionNet preservation: after reversing seven documented canonical citation-key substitutions and one necessary label namespace change, the integrated main body and appendix each match their authoritative accepted sources exactly.
- Preserved 16 section commands, 4 subsection commands, 8 active figures, 9 active tables, 2 displayed equations, and 47 citation commands across the accepted TargetFusionNet paper and appendix.
- Archived the superseded adapted Chapter 4 at `archive/chapters/04_triplet_grounding_adapted_2026-08-05.tex`.
- Verified the complete Chapter 4 thesis build to convergence at 182 pages with zero undefined citations, zero undefined references, zero duplicate labels or bibliography keys, and no LaTeX or Biber errors.
- Approved the Chapter 5 scientific blueprint centred on two-stage multimodal interaction prediction, with Direct SFT as the principal baseline and sequential dialogue prediction and three-frame temporal context treated as promising single-seed observations.
- Archived the complete obsolete `Qwen_work` project, its historical PDF, the old `05_target_reasoning.tex` scaffold, and snapshots of thesis files containing the superseded target-centric framing under `archive/chapter5/`.
- Removed obsolete target-centric reasoning wording from the active thesis abstract, introduction, publications list, Chapter 4 transition, Chapter 5 wrapper, and Chapter 6 scaffold without beginning the Chapter 5 manuscript rewrite.
- Reviewed all four authoritative Chapter 5 figures and documented their intended roles in `chapters/papers/two_stage/README.md`.
- Archived the unused LNCS sample `fig1.eps` and an unrelated SSH `config.txt` that were present in the authoritative manuscript directory but were not referenced by the manuscript.
- Verified the cleanup with a converged 184-page thesis build in a temporary output directory: zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors. The pre-existing root `Thesis.pdf` modification was not overwritten.
- Completed the first full editorial draft of Chapter 5 under `chapters/papers/two_stage/main_body.tex`, preserving the authoritative manuscript and incorporating the approved blueprint, completed experiment inventory, and Methods specification.
- Restored all completed Stage 2 evidence to the integrated results, including Ontology-Guided Prompting and both multitask evaluation modes, and separated principal results from compact exploratory negative results.
- Documented the Chapter 5 editorial decisions and outstanding author decisions in `chapters/papers/two_stage/EDITORIAL_DRAFT_REPORT.md` and created the running supplementary appendix plan in `chapters/papers/two_stage/APPENDIX_PLAN.md`.
- Verified the first complete Chapter 5 draft in a converged 201-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors. Layout warnings were left for the dedicated formatting pass.
- Resolved the outstanding Chapter 5 author decisions: documented explicit temporal centre-frame prompting, incorporated the instrument-tip prior figure, added and cited the Qwen3-VL technical report, reserved confusion matrices for appendix selection, and renamed `Reasoning Only` to `Distilled Rationale Only`.
- Verified the resolved Chapter 5 draft in a converged 203-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Expanded the publications list to distinguish the three accepted articles and active manuscript that form the thesis from six additional publications produced during the doctoral period; excluded earlier undergraduate and master's work and consolidated the duplicated radiology-preprint listing into one publication record.
- Verified the expanded publications list in a converged 203-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Removed all mention of earlier-degree publications from the thesis and added doctoral academic-service records for LM-SURG at ISBI 2026, the King's--Obafemi Awolowo surgical data science partnership, and the AGES Nigeria 2025 conference.
- Verified the revised publications and academic-service pages in a converged 205-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Moved the complete Chapter 5 optimisation-sensitivity study out of the main scientific narrative and into a dedicated chapter supplementary appendix, retaining all five configurations, metrics, and the necessary single-seed and multi-variable caveats.
- Verified the initial Chapter 5 appendix integration in a converged 205-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Reconciled the recovered prompt artifacts with the final Chapter 5 experiment history: Sequential Dialogue Prediction is documented as the three retained action, target, and final-triplet turns; the earlier instrument-identification turn and mixed-training version are excluded; and the final structured Qwen3.7-Max generation template is treated as authoritative for distilled-rationale supervision.
- Drafted the Chapter 5 prompt and response-schema appendix covering Direct SFT, Sequential Dialogue Prediction, Ontology-Guided Prompting, Distilled Reasoning Supervision, and both multitask evaluation modes.
- Verified the prompt appendix in a converged 211-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors; prompt listings introduced no new overfull boxes.
- Removed the obsolete target-centric wording from the rendered Chapter 5 source note and distilled-rationale prompt appendix so that it does not distract from the chapter's two-stage interaction-prediction framing.
- Corrected the Chapter 5 Anatomical Context Prior method to reflect the implemented boundary-contact and furthest-mask-point tip estimator rather than an unsupported separate shaft-orientation calculation.
- Drafted the corresponding appendix section with the complete field-of-view, base/tip, disk construction, EndoViT aggregation, failure-handling, and textual-prior procedure.
- Verified the instrument-tip appendix in a converged 213-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors; the new section introduced no overfull boxes.
- Recovered the final Stage 2 training protocol from the supplied launch records, confirmed that official validation rather than test data was used for checkpoint selection, and standardised validation every 5% of planned steps with patience five across Direct SFT and temporal training.
- Drafted the Chapter 5 training-configuration appendix with common QLoRA/optimisation settings, adaptation-specific changes, and the author-confirmed shared total visual-token budget; unsupported numerical pixel limits and an unenforced sequence-length argument were omitted.
- Verified the Stage 2 training-configuration appendix in a converged 215-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors; the new material introduced no overfull boxes.
- Added an unedited final-schema distilled-rationale example to the Chapter 5 appendix, explicitly distinguishing label-conditioned supervision generation from independent prediction and recording the limited informal inspection, absence of clinical validation, and equal token weighting.
- Verified the distilled-rationale example appendix milestone in a converged 217-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors; the example introduced no overfull boxes.
- Recovered and integrated the official test-set, row-normalised action and target confusion matrices for Direct SFT, three-frame temporal context, and Multitask---Direct SFT evaluation into the Chapter 5 appendix.
- Added a restrained supplementary error analysis that treats the matrices as single-seed descriptive diagnostics and does not infer systematic annotation errors. A provisional blank qualitative panel was initially reserved but was subsequently removed from the active appendix.
- Verified the supplementary error-analysis milestone in a converged 225-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors; the matrices are presented as full-width figures for print legibility.
- Completed the first full 4,579-word draft of Chapter 6, synthesising the review, CholecInstanceSeg, CholecTriplet-Seg, TargetFusionNet, and two-stage MLLM work into a single thesis conclusion.
- Added thesis-level discussion of why complete-triplet AP is comparatively low, why exact evaluation treats errors of different severity equally, and why future top-k measures should complement rather than replace strict grounded AP.
- Established cross-procedure evaluation using the external ProstaTD prostatectomy dataset as the principal future direction and added it to the canonical bibliography.
- Replaced the provisional ProstaTD preprint record with the final ICLR 2026 publication metadata and linked the official dataset repository from the Chapter 6 future-work section.
- Corrected the thesis-integrated Chapter 5 future-work section to name and cite ProstaTD as the external prostatectomy benchmark proposed for cross-procedure evaluation; the authoritative active-manuscript source remains unchanged.
- Verified the first Chapter 6 draft in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Revised Chapter 1 into a complete thesis-level introduction centred on spatially grounded surgical interaction understanding, with multitask learning positioned as a supporting methodology rather than the thesis's core contribution.
- Strengthened the cumulative narrative from the literature review through CholecInstanceSeg, CholecTriplet-Seg, TargetFusionNet, and two-stage multimodal interaction prediction, and revised the first research question accordingly.
- Revised the thesis-written entrances and exits of Chapters 2--5 into a continuous scientific narrative: the review identifies the missing instance-level link, CholecInstanceSeg supplies spatial supervision, CholecTriplet-Seg connects instances to interactions, and Chapter 5 evaluates specialised grounding followed by multimodal interaction prediction.
- Removed repository-process language from the Chapter 4 transition, moderated the prominence of multitask learning in the Chapter 2 wrapper, and added a Chapter 5 appendix-to-conclusion transition into the thesis-wide synthesis.
- Verified the revised Chapter 2--5 narrative in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Standardised the Chapter 2--4 wrapper statements to identify each accepted paper by its full title and publication venue/status, and added the missing journal details to the Chapter 3 and Chapter 4 accepted-manuscript title blocks.
- Added the recovered Chapter 5 prompt, anatomical-prior, and training utilities as scientific provenance while excluding generated Python caches and thesis build outputs; removed hard-coded Hugging Face credentials from the supplied launch scripts before versioning them.
- Completed a thesis-wide scientific consistency audit covering dataset statistics and splits, repeated numerical results, research-question alignment, terminology, publication metadata, contribution attribution, obsolete claims, and abstract alignment.
- Corrected the Chapter 5 predicted-grounding comparison, which had combined one mask-segmentation value with five bounding-box detection values for TargetFusionNet; the table now reproduces the complete Chapter 4 mask-segmentation row and compares AP$_{IVT}=13.52$ with 13.47.
- Updated the three thesis-forming journal records to their final publication metadata, including the final 2026 TargetFusionNet volume, issue, pages, and DOI, while retaining the accepted manuscript as the authoritative Chapter 4 source.
- Strengthened the abstract with the verified dataset sizes and principal quantitative outcomes, and made the conditional answer to the fourth research question explicit in Chapter 6.
- Verified the scientific-consistency milestone in a fresh converged 239-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Completed the first dedicated layout milestone for the front matter, Chapter 1, and Chapter 2. Suppressed the draft-date footer in the thesis source while leaving the title and page style unchanged.
- Adapted the accepted review only within the thesis integration layer: converted inherited two-column figure floats to the single-column thesis float stream, enlarged column-sized diagrams for readability, and restored Figures 2.1--2.16 to pages near their corresponding discussions instead of allowing Figures 2.3--2.16 to accumulate at the chapter end.
- Replaced the unreadably compressed Chapter 2 dataset inventory with a landscape presentation that preserves every accepted row and value, and applied local emergency line-breaking tolerance without rewriting accepted prose.
- Verified the Chapter 2 layout milestone in a converged 241-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors. Remaining diagnostics are inherited/scaled-table or template warnings and will be categorised in the final warning audit.
- Completed the Chapter 3 layout review against the published Scientific Data paper. All seven figures and four tables are already positioned near their corresponding discussion, so no float order was changed.
- Corrected the two visible Chapter 3 margin failures by proportionally fitting Tables 3.1 and 3.2 to the thesis text block. All columns, rows, captions, and numerical values are preserved; wrapper-local emergency line breaking reduced the chapter's remaining visible overflow to sub-2-point diagnostics.
- Verified the Chapter 3 layout milestone in a converged 241-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Completed the Chapter 4 visual review against the accepted TargetFusionNet paper. All eight figures and nine tables remain close to their first discussion, including the appendix subfigure groups.
- Proportionally fitted four wide appendix ablation tables to the thesis text block and introduced a short running-header form for the long-tailed-performance section, eliminating the collision between its header and page number while retaining the full printed section title.
- Verified the Chapter 4 layout milestone in a converged 241-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors. Only two small chapter-level overfull diagnostics remain for the final warning audit.
- Completed the Chapter 5 layout review. The five main methodological figures, three main result tables, appendix tables, and six confusion matrices are readable and remain near the intended discussion; the matrices retain separate float pages for print legibility.
- Replaced the stale Chapter 5 appendix running header inherited from the main-text conclusion with a dedicated `Chapter Supplementary Appendix` mark and applied local line-breaking tolerance without changing scientific content.
- Completed the Chapter 6 and bibliography layout review. Chapter 6 requires no float changes; its mini-table-of-contents is now limited to section level, removing the page-number collision caused by the unusually deep subsection listing. The complete bibliography was visually sampled from first to last page and given local line-breaking tolerance for long identifiers.
- Verified the Chapters 5--6 and bibliography layout milestone in a converged 241-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, no LaTeX or Biber errors, and no overfull-box warnings within Chapter 5, Chapter 6, or the bibliography.
- Replaced the placeholder acknowledgement with a complete first draft thanking supervisors Tom Vercauteren and Miaojing Shi, colleagues Charlie Budd and Meng Wei, and the author's parents.
- Reviewed the title page and originality declaration against the Lucas Fidon reference thesis. Both already follow the same King's College London thesis format, so no unnecessary structural changes were made.
- Reviewed the publications, relationship-to-thesis, and academic-service material. The current page consistently excludes pre-doctoral publications and records the thesis papers, other doctoral publications, ISBI workshop organisation, the King's--Obafemi Awolowo University collaboration, and AGES Nigeria 2025.
- Verified the acknowledgement and front-matter review in a successful 241-page thesis build with no LaTeX or Biber errors and no undefined citations or references.
- Removed the blank provisional Chapter 5 qualitative error-analysis figure from the active appendix. The six evidence-backed confusion matrices remain, and no underlying source images or historical material were deleted.
- Verified the removal in a converged 241-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Moved the impact statement from an unfinished front-matter placeholder to a substantive final section of Chapter 6, following the reference thesis architecture. The statement distinguishes demonstrated scientific and community impact from potential future clinical impact.
- Renamed the publications subsection `Preprints and challenge reports` to `Preprints`. Current primary and author-affiliated records were checked for SurgPIS, the radiology-report manuscript, and the SurgToolLoc/SurgVU report; all three remain publicly documented as preprints, so no unsupported venue acceptance was added.
- Verified the impact-statement and publications milestone in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors. The new impact statement introduced no overfull-box warnings.
- Corrected the Chapter 5 supplementary appendix hierarchy by making it numbered Section 5.10. Its six constituent sections now appear as Sections 5.10.1--5.10.6 rather than misleadingly appearing beneath the Chapter 5 conclusion.
- Verified the corrected appendix hierarchy in a converged 239-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Corrected the academic-service record for the King's--OAUTHC collaboration by distinguishing initiation and Global Engagement Partnership Fund support from the subsequent deployment of research infrastructure, data-governance workflows, team training, video collection, and clinical annotation planning at OAUTHC.
- Verified the revised OAUTHC contribution record in a converged 239-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Aligned the thesis title with the approved RD1 title: `Towards Fine-Grained Surgical Scene Understanding through Grounded Instrument--Tissue Interaction Modelling`.
- Verified the RD1-aligned title in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors; the longer title introduced no title-page overflow warning.
- Renamed the front-matter chapter `Publications arising from this thesis` to the broader and more conventional `List of Publications`, while retaining the distinctions between thesis-forming papers, other doctoral publications, preprints, chapter relationships, and research engagement.
- Verified the renamed publications chapter in a converged 239-page build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Standardised formal triplet and pair notation in thesis-authored material: \ivttriplet is used for the benchmark tuple and \vtpair for the Stage 2 interaction pair, while broader instrument--tissue terminology and natural-language component descriptions are retained. Accepted-paper bodies were not altered.
- Verified the notation changes in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Renamed the thesis-authored closing sections in Chapters 2--5 from `Chapter Summary and Transition` to the cleaner `Chapter Summary`; their transition prose remains intact and continues to connect the scientific narrative implicitly.
- Verified the revised summary headings in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Added a thesis-specific Chapter 5 introduction that connects the two-stage formulation to Chapters 3 and 4, summarises the reported evidence without presenting the active manuscript as unfinished, and distinguishes its thesis-specific structure from the accepted-paper chapters. The existing Chapter Summary remains in place.
- Verified the Chapter 5 introduction in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Lightly compressed four repetitive passages in Chapter 1 while preserving the two-grasper example, the conjunctive grounded-triplet evaluation explanation, the full contribution statements, thesis scope, and chapter guide.
- Verified the lightly compressed introduction in a converged 239-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Recovered the separate CholecInstanceSeg supplementary material and integrated all eight substantive annotation-guideline figures into Chapter 3 with supplementary numbering. The authoritative supplementary project remains unchanged; only its empty trailing evaluation-metrics title page is intentionally omitted and documented.
- Verified the recovered Chapter 3 supplement in a converged 247-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors. The eight figures occupy seven pages, matching the accepted supplement's grouping of the final two examples.
- Reviewed the rendered Chapter 3 supplement page by page: all figures are readable, uncropped, and appropriately scaled. Tightened the opening-page placement, shortened the supplementary running header, and restored the Chapter Summary running header without altering supplementary content.
- Verified the final supplementary layout visually and in a converged 245-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors. Figure S1 now shares the introductory page, Figures S2--S6 each retain a readable full page, and Figures S7--S8 remain clearly grouped on one page.
- Clarified in the Chapter 5 thesis introduction, manuscript introduction, and problem formulation that Stage 2 performs instance-specific, spatially grounded interaction prediction rather than conventional frame-level triplet recognition. Each \vtpair prediction remains linked to a supplied instrument mask and identifier.
- Verified the Chapter 5 grounding clarification in a converged 245-page thesis build with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.
- Consolidated the six Chapter 5 error-analysis matrices into three method-level figures, pairing action and target diagnostics for Direct SFT, three-frame temporal context, and Multitask---Direct SFT. Expanded the temporal interpretation to distinguish reduced irrigation-to-aspiration collapse from unresolved bidirectional confusion.
- Visually verified the three paired error-analysis figures: all matrices and labels remain legible, each method occupies one figure page, and the figures appear consecutively immediately before the Chapter Summary. The converged thesis is 243 pages with zero undefined citations, zero undefined references, zero duplicate bibliography keys, and no LaTeX or Biber errors.

## Current Task

- Author read-through notes implemented and verified; continue with the remaining author-led full-thesis reading and submission-specific front matter.

## Author Read-through Milestones

- Chapter 2: replaced the compressed landscape dataset inventory with a readable multipage portrait table, and made the distinction between frame-level triplet recognition and instance-grounded interaction prediction explicit in the review and conclusion.
- Chapter 3: compressed the repeated general motivation for minimally invasive computer assistance into a direct transition from the Chapter 2 gap to instrument instance segmentation, without changing the dataset motivation or accepted technical content.
- Chapter 5 structure: clarified that each index denotes one physical instrument instance, moved the adaptation-motivation figure directly after Direct SFT, and placed the consolidated implementation/training configuration after all adaptation methods.
- Chapter 5 emphasis: archived the uncontrolled optimisation-sensitivity study, reduced repetitive seed-related caveats, made complete predicted-grounding evaluation the immediate research priority, and added a measured discussion of why dense anatomical-target annotation is valuable but difficult to scale.
- Chapter 6: aligned the synthesis with Chapter 5 by prioritising complete predicted-grounding evaluation, reducing repeated uncertainty language, and carrying the anatomical-target annotation scalability argument into the thesis-level discussion.
- Final read-through verification: completed a forced Biber/LaTeX rebuild to convergence (239 pages), confirmed zero undefined citations or references, zero duplicate bibliography keys, and no LaTeX or Biber errors. Figure and equation inventories are unchanged; the only active table removed is the deliberately archived Chapter 5 optimisation-sensitivity table, while Chapter 2's former single landscape table is now one multipage `longtable`.
- Chapter 2 scope framing: retained the complete accepted review and its generic MTL background, while stating explicitly in the opening and conclusion that the review supplied the broader lesson of connecting complementary scene information and that the thesis subsequently narrowed its technical focus to spatial grounding and instrument--tissue interaction modelling.
- Abstract opening: adopted the clearer Chapter 2 progression from the benefits of minimally invasive surgery, through the challenge of indirect restricted vision, to the motivation for computer-aided intervention before introducing recent surgical-AI advances.

## Outstanding Issues

- TargetFusionNet standalone compilation requires the missing local MiKTeX package `cuted.sty`.
- The converged build retains inherited layout/template warnings, including overfull and underfull boxes, PDF-version inclusion notices, one obsolete display-math warning, and the template's `\theauthor` redefinition warning.
- Root-level `Introduction.tex`, `Methods.tex`, and `Conclusion.tex` are not included by the current thesis and require classification before any archival decision.
- The working tree contains a pre-existing modification to `Thesis.pdf`; this must not be overwritten or included accidentally in unrelated commits.
- The title page currently uses `\today`; this should be replaced by the confirmed submission month/date before final submission.
- King's requires a separate RD2 generative-AI declaration at submission. This administrative declaration must accurately record the editorial and rewriting assistance used during thesis preparation and is separate from the generic originality declaration printed in the thesis.

## Decisions

- The thesis will use a paper-based structure.
- The three published or accepted papers will remain essentially unchanged.
- Each mature paper chapter will contain a thesis-specific introduction, the original paper, and a thesis-specific summary or transition.
- The Two Stage Surgical Triplet Segmentation project is authoritative and completely replaces Qwen Work.
- Obsolete material will be archived or clearly marked as obsolete, never permanently deleted without approval.
- Existing LaTeX style, labels, citations, references, figure numbering, and table numbering will be preserved unless a change is necessary.
- Work will be divided into small logical milestones with descriptive commits.
- The accepted LaTeX manuscript source is authoritative for each published paper chapter when it differs from the publisher-formatted version.
- The thesis loads only `ThesisBibliography.bib`; each publication has one canonical record and key, without BibLaTeX `ids` aliases or chapter-specific suffixes.
- Citation-key differences are harmonised only in thesis-specific chapter sources. Accepted-paper source directories retain their original keys and local bibliography files.
- Chapter 5 is framed as two-stage multimodal interaction prediction. Target-centric chain-of-thought is not a thesis contribution and the obsolete formulation is retained only under `archive/chapter5/`.
- The only authoritative Chapter 5 manuscript is `phd_papers/sources/Two_Stage_Surgical_Triplet_Segmentation/main.tex`; its four referenced PDF figures are the authoritative active figure set.
- The title page and generic originality declaration retain the King's template wording used in the reference thesis. Only submission-specific facts, such as the final date, should be changed.

## Questions Requiring Input

- Confirm the final submission month/date to print on the title page instead of `\today`.
- Confirm whether an impact statement is required and, if so, its expected length or School guidance.
- Review the acknowledgement draft for personal tone and confirm whether any additional family, friends, colleagues, funders, or clinical collaborators should be named.
