#!/usr/bin/env bash
# Change summary 1.0.0: read-only check of the canonical workspace and legacy link.
set -euo pipefail
SCRIPT_VERSION="1.0.0"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
WORKSPACE_ROOT="${CATNAP_WORKSPACE_ROOT:-$(cd -- "$SCRIPT_DIR/../../.." && pwd -P)}"
LEGACY_ROOT="${CATNAP_LEGACY_ROOT:-$HOME/Music/Music Creation/Len-Ina/Streaming}"
printf 'Catnap workspace check %s\n' "$SCRIPT_VERSION"
for entry in Projects Documentation Reference Catnap Guest-Shows Bot TheatrePresentation Sites; do
  [[ -d "$WORKSPACE_ROOT/$entry" ]] || { printf 'Missing folder: %s\n' "$entry" >&2; exit 1; }
done
[[ -f "$WORKSPACE_ROOT/Reference/Catnap_Name_Tracker.xlsx" ]] || { printf 'Current name master is missing.\n' >&2; exit 1; }
[[ -L "$LEGACY_ROOT" ]] || { printf 'Expected legacy compatibility link is missing.\n' >&2; exit 1; }
[[ "$(cd -- "$LEGACY_ROOT" && pwd -P)" == "$(cd -- "$WORKSPACE_ROOT" && pwd -P)" ]] || { printf 'Legacy link resolves to a different workspace.\n' >&2; exit 1; }
printf 'Workspace, current name master and legacy link are available.\n'
