$ErrorActionPreference = "Stop"
$skillRoot = Split-Path -Parent (Split-Path -Parent $PSCommandPath)
python (Join-Path $skillRoot "scripts/validate_workflow_json.py") (Join-Path $skillRoot "tests/minimal-output.json")
