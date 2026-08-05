# Thesis Progress

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

## Current Task

- Confirm which version of each published paper is authoritative for verbatim thesis inclusion.
- Define the common integration pattern for paper-based chapters before transforming Chapter 2.

## Outstanding Issues

- Chapters 2--4 are currently adapted or condensed versions of the published papers rather than the required structure of chapter introduction, essentially unchanged paper, and chapter summary/transition.
- Chapter 5 is an obsolete Qwen-based scaffold and must be replaced by the Two Stage Surgical Triplet Segmentation chapter.
- Chapter 6 is a drafting scaffold and requires substantial writing.
- `Acknowledgments.tex` is nearly empty and the impact statement in `Thesis.tex` is placeholder text.
- `Publications.tex` still describes the obsolete Qwen-era manuscript.
- The Two Stage bibliography is not yet connected to the thesis build.
- The latest available Biber log contains duplicate keys, case-mismatched keys, undefined macros, and malformed bibliography text warnings.
- Root-level `Introduction.tex`, `Methods.tex`, and `Conclusion.tex` are not included by the current thesis and require classification before any archival decision.
- The working tree contains a pre-existing modification to `Thesis.pdf`; this must not be overwritten or included accidentally in unrelated commits.

## Decisions

- The thesis will use a paper-based structure.
- The three published or accepted papers will remain essentially unchanged.
- Each mature paper chapter will contain a thesis-specific introduction, the original paper, and a thesis-specific summary or transition.
- The Two Stage Surgical Triplet Segmentation project is authoritative and completely replaces Qwen Work.
- Obsolete material will be archived or clearly marked as obsolete, never permanently deleted without approval.
- Existing LaTeX style, labels, citations, references, figure numbering, and table numbering will be preserved unless a change is necessary.
- Work will be divided into small logical milestones with descriptive commits.

## Questions Requiring Input

- Confirm the preferred wording and required length for the impact statement.
- Provide the content or key points to include in the acknowledgements when ready.
- Confirm whether each published chapter should reproduce the accepted manuscript source or the final publisher-formatted version when these differ.
- Confirm whether supplementary material and appendices should be embedded within their corresponding paper chapters or placed in thesis appendices.
