#!/usr/bin/env bash
# Change summary 1.0.0: inspect tracked/staged files for common accidental private uploads.
# This is a basic guard. A person must still review the staged diff and data flows.
set -euo pipefail
SCRIPT_VERSION="1.0.0"
REPO_ROOT="${1:-.}"
FAILURES=0
printf 'Catnap repository check %s\n' "$SCRIPT_VERSION"
git -C "$REPO_ROOT" rev-parse --show-toplevel >/dev/null
while IFS= read -r -d '' FILE_PATH; do
  case "$FILE_PATH" in
    *.example|*.example.*|*/examples/*) ;;
    .env|*/.env|*.pem|*.key|*connection.local*|*private-connection*|*dev-queue.json|*browser-profile*|*Catnap_Name_Tracker*|*inbox_export*|*/node_modules/*|*/backups/*)
      printf 'Review excluded/private filename: %s\n' "$FILE_PATH" >&2
      FAILURES=1 ;;
  esac
  [[ -f "$REPO_ROOT/$FILE_PATH" ]] || continue
  if LC_ALL=C grep -Iq . "$REPO_ROOT/$FILE_PATH"; then
    if LC_ALL=C grep -Eq -- '-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|mfa\.[A-Za-z0-9_-]{40,}' "$REPO_ROOT/$FILE_PATH"; then
      printf 'Potential credential marker in: %s\n' "$FILE_PATH" >&2
      FAILURES=1
    fi
  fi
done < <(git -C "$REPO_ROOT" ls-files -z)
[[ "$FAILURES" == 0 ]] || exit 1
printf 'Basic tracked-file checks passed; review the staged diff before publishing.\n'
