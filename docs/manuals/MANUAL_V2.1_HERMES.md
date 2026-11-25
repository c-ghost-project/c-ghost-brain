# 🤖 Manual de Usuario `C://GHOST v2.1` para Hermes Agent (De Cero a Operar Solo)

> **Audiencia:** Usuarios de **Hermes Agent** (terminal, dashboard, Telegram o WhatsApp) que quieren operar un centro de mando multi-agente con **12 Protocolos**, **Pirámide de Costo \$0 de 5 Niveles**, **migración segura de 3 vías (`--migrate`)** y **4 scripts automáticos de Nivel 0** sin depender de librerías externas de Python.

---

## 1. Arquitectura de `Hermes × C://GHOST v2.1`

```text
  NIVEL 0 ($0 / 0 tokens) ──► preflight_check.sh + intent_classify.py + quota_tracker.py
  NIVEL 1 ($0 — Hermes)   ──► Modelos gratuitos / Ollama local (~60% del trabajo diario)
  NIVEL 2 ($0 — OpenCode) ──► Skill opencode-cli en 2.º plano (macro-scaffolding ≥ 3 archivos)
  NIVEL 3 (Cuota Premium) ──► Skill antigravity-cli (fuerzas especiales, freno al 80% de cuota)
  NIVEL 4 (Visual)        ──► visual_gen.py (Mermaid → PNG HD + PDF A4 automático)
```

> Puedes consultar los diagramas renderizados en [`adapters/hermes/skills/c-ghost-seed/docs/artifacts/`](../../adapters/hermes/skills/c-ghost-seed/docs/artifacts/) y los manuales profundos en [`adapters/hermes/skills/c-ghost-seed/docs/`](../../adapters/hermes/skills/c-ghost-seed/docs/).

---

## 2. Prerrequisitos

* **Hermes Agent** instalado (`~/.hermes/` operativo).
* **Python 3.8+** (`python3 --version`, solo biblioteca estándar).
* **Git** (`git --version`).
* *(Opcional)* **OpenCode CLI** en `~/.local/bin/opencode` (Nivel 2), **Antigravity CLI (`agy`)** en `~/.local/bin/agy` (Nivel 3), **Ollama** con `qwen2.5:7b` (offline) y **Chrome/Chromium** (para exportar PNG/PDF con `visual_gen.py`).

---

## 3. Instalación Paso a Paso en tu Hermes Agent

### Paso 1 — Respaldar tu `SOUL.md` actual (si ya tienes uno)
```bash
mkdir -p ~/.hermes/backups
[ -f ~/.hermes/SOUL.md ] && cp ~/.hermes/SOUL.md ~/.hermes/backups/SOUL.md.pre-cghost.bak
```

### Paso 2 — Instalar el Cerebro (`SOUL.md`) y las Skills
Desde la raíz de este repositorio `c-ghost-brain`:
```bash
# 1. Instalar la constitución operativa de Hermes
cp adapters/hermes/SOUL.example.md ~/.hermes/SOUL.md

# 2. Instalar la skill sembradora c-ghost-seed (Protocolos P0–P12 + 4 scripts)
mkdir -p ~/.hermes/skills/software-development
cp -r adapters/hermes/skills/c-ghost-seed ~/.hermes/skills/software-development/

# 3. (Opcional) Instalar los puentes a OpenCode CLI (Nivel 2) y Antigravity CLI (Nivel 3)
mkdir -p ~/.hermes/skills/autonomous-ai-agents
cp -r adapters/hermes/skills/opencode-cli ~/.hermes/skills/autonomous-ai-agents/
cp -r adapters/hermes/skills/antigravity-cli ~/.hermes/skills/autonomous-ai-agents/
```

### Paso 3 — Ajustar tus Modelos en `~/.hermes/SOUL.md`
Abre `~/.hermes/SOUL.md` y verifica la sección **"Pirámide de 5 Niveles"**:
* Si usas otros modelos en Nivel 1 (por ejemplo OpenRouter free, Groq, Gemini Flash u otro modelo local de Ollama), reemplaza sus identificadores ahí.
* Si no usas OpenCode CLI o Antigravity CLI, simplemente déjalos comentados y Hermes ejecutará todo sobre Niveles 0, 1 y 4.

### Paso 4 — Verificar que el Sembrador compila y funciona
```bash
python3 -m py_compile ~/.hermes/skills/software-development/c-ghost-seed/scripts/init_c_ghost.py
```

---

## 4. Cómo Sembrar tu Primer Proyecto (o Migrar uno Existente)

### Caso A — Proyecto Nuevo desde Cero
```bash
python3 ~/.hermes/skills/software-development/c-ghost-seed/scripts/init_c_ghost.py \
  --dir /ruta/a/mi-proyecto \
  --name "Mi Proyecto" \
  --org "Personal" \
  --stack "Python 3.12 + FastAPI + PostgreSQL"
```
Esto generará **11 archivos exactos** (`.hermes.md`, `AGENTS.md`, `STATUS.md`, `IDEAS.md`, `CHANGELOG.md`, `.agents/skills/01-core-domain/SKILL.md`, `docs/whitepaper/README.md` y los 4 scripts en `.agents/scripts/`).

### Caso B — Proyecto que ya tiene `STATUS.md` o `AGENTS.md` (Protocolo 12: `--migrate`)
Nunca uses `--force` a ciegas. Ejecuta:
```bash
python3 ~/.hermes/skills/software-development/c-ghost-seed/scripts/init_c_ghost.py \
  --dir /ruta/a/mi-proyecto \
  --name "Mi Proyecto" \
  --migrate
```
Preserva íntegra tu memoria viva (`STATUS.md`, `IDEAS.md`, `CHANGELOG.md`), muestra diffs de tres vías y actualiza de forma segura los scripts de Nivel 0.

---

## 5. Operación Diaria Autónoma (Cómo Trabajar Solo con los 4 Scripts)

Dentro de tu proyecto sembrado, tanto tú como Hermes operan siguiendo este flujo:

1. **Pre-Flight Obligatorio (Protocolo 11 — 0 tokens):**
   ```bash
   ./.agents/scripts/preflight_check.sh
   ```
   Valida linters, tipos, descubrimiento de tests, `git diff --stat` y que `STATUS.md` tenga `≤ 100` líneas. Si devuelve `exit 0`, el entorno está verde para trabajar o delegar.
2. **Clasificación Automática de Intención (Pre-P1):**
   ```bash
   echo "Refactoriza los 5 controladores de usuarios y añade pruebas" | ./.agents/scripts/intent_classify.py
   ```
   Devuelve un JSON determinista indicando el nivel recomendado (`0` a `4`), la skill y la confianza.
3. **Control de Cuota Premium (Nivel 3):**
   ```bash
   ./.agents/scripts/quota_tracker.py check
   ./.agents/scripts/quota_tracker.py add 12000 gemini-4-carbon
   ```
   Si la cuota registrada en `STATUS.md` supera el **80%**, Hermes se detiene automáticamente y pide tu autorización antes de gastar créditos de Nivel 3.
4. **Diagramas Automáticos (Nivel 4 — Protocolo 9+):**
   ```bash
   echo "flowchart LR; A[Usuario] --> B[Hermes]; B --> C[Nivel 0..3]" | ./.agents/scripts/visual_gen.py arquitectura
   ```
   Exporta `arquitectura.png` (1920px HD) y `arquitectura.pdf` (A4) dentro de `.agents/artifacts/`.

### Primer Mensaje Recomendado al Abrir Hermes sobre tu Proyecto
> *"Lee `.hermes.md` y `STATUS.md`, corre `preflight_check.sh`, ajusta los pilares del proyecto según nuestro stack real y propón la primera Tarea Activa (`F1-T01`)."*
