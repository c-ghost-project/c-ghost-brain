#!/usr/bin/env bash
# ==============================================================================
# 🌱 plant-seed.sh — Sembrador Universal del Cerebro C://GHOST v3.0
# Agnóstico de lenguaje, nube, usuario y gestor de tareas.
# Uso: ./plant-seed.sh [ruta-del-proyecto] [nombre-opcional]
# ==============================================================================
set -euo pipefail

TARGET_DIR="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TPL_DIR="$SCRIPT_DIR/templates"
TODAY="$(date +%Y-%m-%d)"

mkdir -p "$TARGET_DIR/.agents/hooks" "$TARGET_DIR/.agents/skills" "$TARGET_DIR/docs/adr"
TARGET_ABS="$(cd "$TARGET_DIR" && pwd)"
PROJECT_NAME="${2:-$(basename "$TARGET_ABS")}"

echo ">>> [1/4] Inicializando seguridad base (.gitignore Zero-Trust) en: $TARGET_ABS"
GITIGNORE="$TARGET_ABS/.gitignore"
touch "$GITIGNORE"
ZERO_TRUST_PATTERNS=(
  ".env"
  ".env.*"
  "!.env.example"
  ".secrets/"
  "*.pem"
  "*.key"
  "*.p12"
  "*.pfx"
  "id_rsa*"
  "id_ed25519*"
  "credentials*.json"
  "*service-account*.json"
)
for pat in "${ZERO_TRUST_PATTERNS[@]}"; do
  if ! grep -Fxq "$pat" "$GITIGNORE" 2>/dev/null; then
    printf "%s\n" "$pat" >> "$GITIGNORE"
  fi
done

if [ ! -d "$TARGET_ABS/.git" ] && command -v git >/dev/null 2>&1; then
  git -C "$TARGET_ABS" init -b main >/dev/null 2>&1 || git -C "$TARGET_ABS" init >/dev/null 2>&1 || true
fi

echo ">>> [2/4] Sembrando Constitución y Memoria Viva virgen (C://GHOST v3.0)..."
ESCAPED_NAME="$(printf '%s\n' "$PROJECT_NAME" | sed 's/[&/\]/\\&/g')"
sed "s/\[NOMBRE_DEL_PROYECTO\]/$ESCAPED_NAME/g" "$TPL_DIR/AGENTS.universal.md" > "$TARGET_ABS/.agents/AGENTS.md"
ln -sfn ".agents/AGENTS.md" "$TARGET_ABS/AGENTS.md"

if [ ! -f "$TARGET_ABS/STATUS.md" ]; then
  sed "s/YYYY-MM-DD/$TODAY/g" "$TPL_DIR/STATUS.universal.md" > "$TARGET_ABS/STATUS.md"
fi
if [ ! -f "$TARGET_ABS/IDEAS.md" ]; then
  sed "s/YYYY-MM-DD/$TODAY/g" "$TPL_DIR/IDEAS.universal.md" > "$TARGET_ABS/IDEAS.md"
fi
if [ ! -f "$TARGET_ABS/CHANGELOG.md" ]; then
  sed "s/YYYY-MM-DD/$TODAY/g" "$TPL_DIR/CHANGELOG.universal.md" > "$TARGET_ABS/CHANGELOG.md"
fi

echo ">>> [3/4] Instalando Lifecycle Hooks universales (SessionStart + PreToolUse + Stop Gate)..."
cp "$TPL_DIR/hooks.universal.json" "$TARGET_ABS/.agents/hooks.json"
cp "$TPL_DIR/hooks/session-start.sh" "$TARGET_ABS/.agents/hooks/session-start.sh"
cp "$TPL_DIR/hooks/pre-tool-guard.sh" "$TARGET_ABS/.agents/hooks/pre-tool-guard.sh"
cp "$TPL_DIR/hooks/stop-gate.sh" "$TARGET_ABS/.agents/hooks/stop-gate.sh"
chmod +x "$TARGET_ABS/.agents/hooks/"*.sh

echo ">>> [4/4] Copiando guía del Prompt 2 (Adaptación al Proyecto)..."
cp "$SCRIPT_DIR/02_PROMPT_ADAPTAR_AL_PROYECTO.md" "$TARGET_ABS/.agents/PROMPT_ADAPTAR_PROYECTO.md"

echo ""
echo "✅ Semilla C://GHOST v3.0 plantada en: $TARGET_ABS"
echo "👉 Siguiente paso: abre una conversación en '$TARGET_ABS' y pega el Prompt 2 (.agents/PROMPT_ADAPTAR_PROYECTO.md)."
