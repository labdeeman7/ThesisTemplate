param([string]$OutputDirectory = '.build')
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $projectRoot
$portableBin = Join-Path $projectRoot '.tools\miktex\texmfs\install\miktex\bin\x64'
if (Test-Path -LiteralPath (Join-Path $portableBin 'pdflatex.exe')) {
    $env:Path = "$portableBin;$env:Path"
}
foreach ($program in @('pdflatex', 'biber')) {
    if (-not (Get-Command $program -ErrorAction SilentlyContinue)) {
        throw "$program is unavailable. Install MiKTeX or restore the project-local portable installation."
    }
}
New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $OutputDirectory 'chapters') | Out-Null
$texArguments = @('-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-synctex=1', "-output-directory=$OutputDirectory", 'Thesis.tex')
& pdflatex @texArguments
if ($LASTEXITCODE -ne 0) { throw 'Initial pdfLaTeX pass failed. See the output directory Thesis.log.' }
& biber "--input-directory=$OutputDirectory" "--output-directory=$OutputDirectory" Thesis
if ($LASTEXITCODE -ne 0) { throw 'Biber failed. See the output directory Thesis.blg.' }
foreach ($pass in 1..3) {
    & pdflatex @texArguments
    if ($LASTEXITCODE -ne 0) { throw "pdfLaTeX pass $pass failed." }
}
Write-Output "Built $(Join-Path $OutputDirectory 'Thesis.pdf')"
