# Thesis Layout TODO

These observations are deliberately deferred to the final formatting pass. They do not justify changes to accepted scientific content.

## Chapter 2: Literature Review

- Check placement of the review's large overview figures and wide comparison tables after the complete thesis pagination has stabilised; standard LaTeX float movement may separate them from their first textual mention.
- Review the long tables for overfull boxes and cramped columns in the thesis page geometry.
- Check whether the chapter title, accepted-manuscript heading, and abstract create excessive vertical repetition at the start of the chapter.
- Visually inspect page breaks around the thesis-written introduction, accepted manuscript, and chapter transition.

## Chapter 3: CholecInstanceSeg

- Check placement of the seven manuscript figures and four manuscript tables, especially the dataset-partition and baseline-results material.
- Review wide tables inherited from the accepted Scientific Data layout for fit within the thesis margins.
- Inspect the three displayed equations currently written with inherited `$$...$$` syntax; defer any typographic conversion until the final formatting pass because their scientific content is correct.
- Check the pagination of the manuscript end matter (Code Availability, Acknowledgements, Author Contributions, and Competing Interests) and its separation from the thesis-written transition.

## Chapter 4: TargetFusionNet

- Review placement of the eight accepted figures and nine accepted tables across the main paper and appendix after final pagination is stable.
- Check wide `table*` material and dense ablation tables against the thesis margins; preserve the accepted values and column structure.
- Visually inspect the appendix subfigure groups and captions under the thesis `subcaption` package.
- Check the transition from the accepted declarations to the accepted appendix, and from the appendix to the thesis-written chapter summary.
- Confirm whether the supplementary comparison video should be deposited or linked separately; the accepted source refers to it but the file is not present in the repository.

## Whole Thesis

- Address inherited overfull and underfull box warnings only after all chapters and front matter are stable.
- Perform a final float-order and first-reference check across every paper chapter.
