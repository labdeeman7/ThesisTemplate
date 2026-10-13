# Local and Overleaf Setup

This repository is set up around `Thesis.tex` as the main LaTeX file.

## Home-system setup (6 October 2026)

A project-local portable MiKTeX installation is available under `.tools/miktex`.
It includes pdfLaTeX and Biber. `.tools/` is ignored by Git and stays on this
computer. The official installer and standalone setup utility were downloaded
from MiKTeX and checked against the SHA-256 values on its download page.

Verified on this system: pdfLaTeX (MiKTeX 25.12 Portable), Biber 2.21,
and a successful full build of the 248-page thesis with the bibliography.

Build from the repository root with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\build-thesis.ps1
```

The execution-policy setting applies only to this invocation. The script adds
the portable executables to its own process PATH, runs pdfLaTeX, Biber, and
three final pdfLaTeX passes, and writes `.build/Thesis.pdf`. It does not require
Perl or a permanent system PATH change. Missing-package installation is enabled;
the first build needs Internet access to fetch packages beyond the basic set.

The older `latexmk` workflow below remains an option if you install Perl and
`latexmk`. It is not required by `tools/build-thesis.ps1`.

Official references: [MiKTeX downloads](https://miktex.org/download),
[portable setup options](https://docs.miktex.org/manual/miktexsetup.html),
and [automatic package installation](https://docs.miktex.org/manual/autoinstall.html).

The ten-slide talk is in `presentations/Thesis_overview_10min.pptx` and
`presentations/Thesis_overview_10min.pdf`; neither needs LaTeX to present.

## Recommended Workflow

Use GitHub as the canonical repository, and connect Overleaf to GitHub when possible. That gives three useful places to work:

- local clone: for Codex, larger edits, search, refactors, and local compilation
- GitHub fork: the durable version history and backup
- Overleaf project: for supervisor review, comments, and browser-based editing

If Overleaf GitHub sync is not available on your plan, add the Overleaf project as a second Git remote instead.

## Install Local LaTeX on Windows

Install MiKTeX:

```powershell
winget install MiKTeX.MiKTeX
```

Install Strawberry Perl, which is needed by `latexmk` on Windows:

```powershell
winget install StrawberryPerl.StrawberryPerl
```

After installation, open MiKTeX Console and enable automatic package installation:

```text
Settings > General > Install missing packages on-the-fly > Always
```

Then restart PowerShell or VS Code so the new commands are on PATH. If the current terminal has not picked up the PATH yet, a temporary workaround is:

```powershell
$env:Path="C:\Strawberry\perl\bin;$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64;$env:Path"
```

Check the installation:

```powershell
latexmk -v
pdflatex --version
biber --version
```

## Build Locally

From the repository root:

```powershell
latexmk
```

Clean generated build files:

```powershell
latexmk -c
```

Fully clean generated build files and the generated PDF:

```powershell
latexmk -C
```

## Set Up Overleaf

Option A, preferred if available:

1. Create a new blank Overleaf project.
2. In Overleaf, use GitHub synchronization to import this GitHub repository.
3. Set the main document to `Thesis.tex`.
4. Set the compiler to `pdfLaTeX`.
5. Share the Overleaf project with supervisors.

Option B, if using Overleaf Git directly:

1. Create a new blank Overleaf project.
2. Copy its Overleaf Git URL.
3. Add it locally:

```powershell
git remote add overleaf https://git.overleaf.com/PROJECT_ID
git push overleaf main
```

Then sync carefully:

```powershell
git pull overleaf main
git push origin main
git push overleaf main
```

## Notes

- The template uses `biblatex`, so `biber` must be installed locally.
- `latexmk` needs Perl on Windows.
- `latexmkrc` makes `latexmk` build `Thesis.tex` by default.
- Avoid committing generated auxiliary files such as `.aux`, `.log`, `.bcf`, `.run.xml`, and `.synctex.gz`.
- Decide whether to keep committing `Thesis.pdf`. It is currently tracked in the template, but committing generated PDFs often creates noisy diffs.
