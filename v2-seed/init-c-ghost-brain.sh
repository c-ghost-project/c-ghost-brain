#!/usr/bin/env bash
# ==============================================================================
# 🌱 init-c-ghost-brain.sh — Sembrador Automático del Cerebro C://GHOST
# Uso: ./init-c-ghost-brain.sh /ruta/al/nuevo-proyecto "Nombre del Proyecto"
# ==============================================================================
set -euo pipefail

TARGET_DIR="${1:-.}"
PROJECT_NAME="${2:-Nuevo Ecosistema}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TODAY="$(date +%Y-%m-%d)"

mkdir -p "$TARGET_DIR"
mkdir -p "$TARGET_DIR/docs/pilar-7-whitepaper"

echo ">>> [1/3] Sembrando archivos troncales de conciencia en: $TARGET_DIR"
sed "s/\[NOMBRE_DEL_PROYECTO\]/$PROJECT_NAME/g" "$SCRIPT_DIR/AGENTS.template.md" > "$TARGET_DIR/AGENTS.md"
sed -e "s/\[NOMBRE_DEL_PROYECTO\]/$PROJECT_NAME/g" -e "s/YYYY-MM-DD/$TODAY/g" "$SCRIPT_DIR/STATUS.template.md" > "$TARGET_DIR/STATUS.md"
sed "s/YYYY-MM-DD/$TODAY/g" "$SCRIPT_DIR/IDEAS.template.md" > "$TARGET_DIR/IDEAS.md"
sed "s/YYYY-MM-DD/$TODAY/g" "$SCRIPT_DIR/CHANGELOG.template.md" > "$TARGET_DIR/CHANGELOG.md"

echo ">>> [2/3] Creando estructura de Divulgación Progresiva (.agents/skills/)..."
SKILLS=(
  "sso-jwt-auth"
  "wordpress-cpanel-dev"
  "cloudflare-edge-backend"
  "ux-ui-design-system"
  "cloudflare-frontend-dev"
  "vault-zero-trust"
  "hybrid-cloud-vps"
  "whitepaper-living-docs"
)

for s in "${SKILLS[@]}"; do
  mkdir -p "$TARGET_DIR/.agents/skills/$s"
  if [ ! -f "$TARGET_DIR/.agents/skills/$s/SKILL.md" ]; then
    sed "s/nombre-de-la-skill/$s/g" "$SCRIPT_DIR/SKILL.template.md" > "$TARGET_DIR/.agents/skills/$s/SKILL.md"
  fi
done

echo ">>> [3/3] Copiando Prompt Maestro de Inicio desde Cero..."
cp "$SCRIPT_DIR/00_PROMPT_INICIO_DESDE_CERO.md" "$TARGET_DIR/PROMPT_INICIO_PROYECTO.md"

echo "✅ Cerebro C://GHOST sembrado con éxito en: $TARGET_DIR"
