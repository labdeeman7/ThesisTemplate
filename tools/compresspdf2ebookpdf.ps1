[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$InputPdf = "Thesis.pdf",

    [Parameter(Position = 1)]
    [string]$OutputPdf,

    [switch]$Force
)

$ErrorActionPreference = "Stop"

$inputPath = (Resolve-Path -LiteralPath $InputPdf).Path
if ([string]::IsNullOrWhiteSpace($OutputPdf)) {
    $directory = Split-Path -Parent $inputPath
    $stem = [System.IO.Path]::GetFileNameWithoutExtension($inputPath)
    $OutputPdf = Join-Path $directory "$stem-review-compressed.pdf"
}
$outputPath = [System.IO.Path]::GetFullPath($OutputPdf)

if ($inputPath -eq $outputPath) {
    throw "The output PDF must differ from the input PDF."
}
if ((Test-Path -LiteralPath $outputPath) -and -not $Force) {
    throw "Output already exists: $outputPath`nUse -Force to replace it."
}

$ghostscript = Get-Command gswin64c.exe, gswin64c, gs.exe, gs -ErrorAction SilentlyContinue |
    Select-Object -First 1 -ExpandProperty Source

if (-not $ghostscript) {
    $searchRoots = @(
        (Join-Path $env:ProgramFiles "gs"),
        (Join-Path $env:LOCALAPPDATA "Programs\Ghostscript")
    ) | Where-Object { Test-Path -LiteralPath $_ }

    $ghostscript = Get-ChildItem -Path $searchRoots -Filter gswin64c.exe -File -Recurse -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending |
        Select-Object -First 1 -ExpandProperty FullName
}

if (-not $ghostscript) {
    throw "Ghostscript was not found. Install the 64-bit Windows release from https://ghostscript.com/releases/gsdnld.html."
}

$pdfmarks = Join-Path $PSScriptRoot "mktpdfmarks"
if (-not (Test-Path -LiteralPath $pdfmarks)) {
    throw "Required pdfmarks file not found: $pdfmarks"
}

if ($Force -and (Test-Path -LiteralPath $outputPath)) {
    Remove-Item -LiteralPath $outputPath -Force
}

$arguments = @(
    "-dCompatibilityLevel=1.4"
    "-dPDFSETTINGS=/ebook"
    "-dColorConversionStrategy=/UseDeviceIndependentColor"
    "-dDownsampleColorImages=true"
    "-dDownsampleGrayImages=true"
    "-dDownsampleMonoImages=true"
    "-dMaxSubsetPct=100"
    "-dSubsetFonts=true"
    "-dEmbedAllFonts=true"
    "-dOptimize=true"
    "-dUseFlateCompression=true"
    "-dNOPAUSE"
    "-dBATCH"
    "-sDEVICE=pdfwrite"
    "-sOutputFile=$outputPath"
    $inputPath
    $pdfmarks
)

Write-Host "Compressing PDF with Ghostscript $(& $ghostscript --version)..."
$process = Start-Process -FilePath $ghostscript -ArgumentList $arguments -NoNewWindow -Wait -PassThru
if ($process.ExitCode -ne 0 -or -not (Test-Path -LiteralPath $outputPath)) {
    throw "Ghostscript compression failed with exit code $($process.ExitCode)."
}

$inputSize = (Get-Item -LiteralPath $inputPath).Length
$outputSize = (Get-Item -LiteralPath $outputPath).Length
$reduction = (1 - ($outputSize / $inputSize)) * 100

Write-Host "Created: $outputPath"
Write-Host ("Compressed from {0:N2} MB to {1:N2} MB ({2:N1}% reduction)." -f `
    ($inputSize / 1MB), ($outputSize / 1MB), $reduction)
