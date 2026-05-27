# Local and Overleaf Setup

This repository is set up around `Thesis.tex` as the main LaTeX file.

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
