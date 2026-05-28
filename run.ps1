$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path results | Out-Null
python test.py
