#!/usr/bin/env bash
# ==============================================================================
# C://GHOST v3.0 Universal Hook: SessionStart (cghost-cockpit-boot)
# 100% agnóstico: reporta rama Git y estado de STATUS.md al iniciar sesión.
# ==============================================================================
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
cat >/dev/null 2>&1 || true

BRANCH="sin-git"
if command -v git >/dev/null 2>&1 && [ -d "${REPO_ROOT}/.git" ]; then
  BRANCH="$(git -C "${REPO_ROOT}" branch --show-current 2>/dev/null || echo 'detached')"
fi

STATUS_LINES=0
if [ -f "${REPO_ROOT}/STATUS.md" ]; then
  STATUS_LINES="$(wc -l < "${REPO_ROOT}/STATUS.md" | tr -d ' ')"
fi

MSG="[C://GHOST v3.0 Boot] Proyecto=$(basename "${REPO_ROOT}") | Branch=${BRANCH} | STATUS.md=${STATUS_LINES}/100 líneas. Protocolo 0: lee STATUS.md antes de actuar."

python3 -c '
import json, sys
print(json.dumps({
  "injectSteps": [
    {"systemMessage": {"systemMessage": sys.argv[1]}}
  ]
}))
' "${MSG}"
