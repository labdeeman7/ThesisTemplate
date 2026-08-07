# Thesis Layout TODO

These observations are deliberately deferred to the final formatting pass. They do not justify changes to accepted scientific content.

## Chapter 2: Literature Review

- Recheck final pagination after later chapters and front matter stabilise. The initial layout pass moved Figures 2.1--2.16 into the single-column float stream and placed them near their discussions; Figures 2.3--2.16 no longer accumulate at the chapter end.
- Recheck the landscape dataset-summary table after final pagination. It is now readable and preserves all accepted rows, but its internally scaled cells still emit inherited box diagnostics before scaling.
- Check whether the chapter title, accepted-manuscript heading, and abstract create excessive vertical repetition at the start of the chapter.
- Visually inspect page breaks around the thesis-written introduction, accepted manuscript, and chapter transition.
- Retain the accepted manuscript's obsolete `$$...$$` display unchanged until the final typographic decision.

## Chapter 3: CholecInstanceSeg

- Recheck final pagination after later material stabilises. The initial visual pass confirmed that all seven figures and four tables remain close to their discussions.
- Tables 3.1 and 3.2 have been proportionally fitted to the thesis text width; recheck their final print legibility after any global font or margin change.
- Inspect the three displayed equations currently written with inherited `$$...$$` syntax; defer any typographic conversion until the final formatting pass because their scientific content is correct.
- Check the pagination of the manuscript end matter (Code Availability, Acknowledgements, Author Contributions, and Competing Interests) and its separation from the thesis-written transition.

## Chapter 4: TargetFusionNet

- Recheck final pagination after later material stabilises. The initial visual pass confirmed that all eight figures and nine tables remain close to their discussions across the main paper and appendix.
- Four wide appendix ablation tables have been proportionally fitted to the thesis text width while preserving their accepted values and column structure.
- The appendix subfigure groups and captions render correctly under the thesis `subcaption` package.
- The long Section 4.14 title now uses a short running-header form to avoid colliding with the page number; its full printed title is unchanged.
- Check the transition from the accepted declarations to the accepted appendix, and from the appendix to the thesis-written chapter summary.
- Confirm whether the supplementary comparison video should be deposited or linked separately; the accepted source refers to it but the file is not present in the repository.

## Whole Thesis

- Continue addressing visible overfull boxes chapter by chapter; retain harmless diagnostics produced inside deliberately scaled tables and record them for the final warning audit.
- Perform a final float-order and first-reference check across every paper chapter.
