$ErrorActionPreference = "Stop"

if (Test-Path -LiteralPath results) {
    Remove-Item -LiteralPath results -Recurse -Force
}
New-Item -ItemType Directory -Force -Path results | Out-Null

$pythonCandidates = @(
    "$env:USERPROFILE\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe"
)

$pythonExe = $null
foreach ($candidate in $pythonCandidates) {
    if (Test-Path -LiteralPath $candidate) {
        $pythonExe = $candidate
        break
    }
}

if (-not $pythonExe) {
    $command = Get-Command python -ErrorAction SilentlyContinue
    if ($command -and ($command.Source -notlike "*WindowsApps*")) {
        $pythonExe = $command.Source
    }
}

if (-not $pythonExe) {
    throw "No usable Python interpreter found. Install Python or edit run.ps1 to point to a real python.exe."
}

Write-Output "Using Python: $pythonExe"
& $pythonExe test.py
