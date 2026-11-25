---
name: antigravity-cli
description: "Delegate complex coding to Antigravity CLI in background."
version: 1.0.0
author: Dugui & Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    category: autonomous-ai-agents
    tags: [Coding-Agent, Antigravity, Architecture, UI, Background]
    related_skills: [opencode-cli, c-ghost-seed]
---

# Antigravity CLI Skill

Delegate high-impact architecture, security, UI/UX, and technical writing tasks to Antigravity CLI (`~/.local/bin/agy`) running in the background via `terminal`. Reserve this skill for Nivel 3 tasks (complex design, Zero-Trust audits, pixel-accurate UI, or specs) — use `opencode-cli` first for repetitive scaffolding or large test suites.

## When to Use

- Distributed architecture, Zero-Trust audits, or critical root-cause debugging.
- Frontend/UI design systems (`React`, `Next.js`, `Tailwind`, CSS precision).
- Long-form technical specs, WhitePapers, or ADRs.
- Complex backend, concurrency, or analytical SQL tasks that exceed free Tier 1/2 models.

## Prerequisites

- Binary installed and authenticated: `~/.local/bin/agy` (`agy models` lists available models).
- Target project directory exists and preferably uses Git so changes can be audited via `git diff --stat`.

## Model Selection Matrix

Pick the exact `--model` flag by task domain:

| Task Domain | `--model` | `--mode` |
| :--- | :--- | :--- |
| Architecture, Zero-Trust, critical debugging | `gemini-4-carbon-high` | `plan` (audit) or `auto` (fix) |
| Full-Stack / Backend APIs, SQL, business logic | `gemini-4-neon-medium` | `accept-edits` or `auto` |
| UI/UX & Frontend (React, Next.js, Tailwind) | `claude-sonnet-5-5-medium` | `accept-edits` |
| WhitePapers, RFDs, executive specs | `claude-opus-5-5-medium` | `accept-edits` |
| Complex algorithms, concurrency, log analysis | `gemini-4-argon-medium` | `auto` |
| Bash/DevOps scripting, quick mocks | `gemini-4-hydrogen-medium` | `auto` |
| Unbiased second opinion / cross-check | `gpt-oss-120b-medium` | `plan` |

## How to Run

Always launch non-interactively in background using `terminal` with `background=true` and `notify_on_complete=true`, redirecting output to a log file under `~/.hermes/cache/scratch/`:

```bash
~/.local/bin/agy -p "<STRUCTURED_5_FIELD_HANDOFF>" \
  --model gemini-4-neon-medium \
  --mode accept-edits \
  --add-dir "/abs/path/to/project" \
  > "$HOME/.hermes/cache/scratch/agy-task.log" 2>&1
```

- Use `--mode plan` for read-only analysis or design plans.
- Use `--mode accept-edits` when only file edits are needed.
- Use `--mode auto` when the task must execute build/test verification commands non-interactively.
- Never pass `--dangerously-skip-permissions`.

## Procedure

0. **Puertas previas (C://GHOST v2.1, obligatorias).** Desde la raíz del proyecto: ejecuta `./.agents/scripts/preflight_check.sh` (solo exit 0 permite continuar, Protocolo 11) y `./.agents/scripts/quota_tracker.py check` (si `cuota_antigravity_usada` supera el 80%, alerta y pide confirmación explícita al Creador antes de gastar cuota). Adjunta la salida del preflight al handoff como `[PREFLIGHT_REPORT]`.
1. Build a C://GHOST **5-field Handoff** inside the `-p` prompt:
   - `[SKILL REQUERIDA]` (project skill in `.agents/skills/` if any)
   - `[OBJETIVO ATÓMICO]`
   - `[RUTAS PERMITIDAS]` (explicitly forbid editing `STATUS.md`, `IDEAS.md`, `CHANGELOG.md`)
   - `[CONTRATO Y RESTRICCIONES]` (Zero-Trust: never read or expose `.env` secrets)
   - `[COMANDO DE VERIFICACIÓN]`
2. Spawn with `terminal(command=..., workdir=<project>, background=true, notify_on_complete=true)`.
3. In non-async contexts (e.g. `cron`), wait using `process_manage(action='wait')`.
4. When notified, inspect the log with `read_file` on `~/.hermes/cache/scratch/agy-task.log` and audit changes with `git diff --stat` plus the verification command.
5. Registra el consumo de cuota: `./.agents/scripts/quota_tracker.py add <modelo-usado>` para actualizar `cuota_antigravity_usada` en `STATUS.md`.

## Pitfalls

- Launching `background=true` without `notify_on_complete=true` causes silent completion.
- Running without `--add-dir` or proper `workdir` makes `agy` miss the project's `AGENTS.md`.
- Sending huge exploratory tasks wastes premium quota; pre-scope paths first with `search_files`.
- Omitir las puertas previas de v2.1: sin `preflight_check.sh` en verde no se arma el handoff (P11), y sin revisar `cuota_antigravity_usada` en `STATUS.md` se puede agotar la cuota Antigravity sin aviso — por encima del 80% exige confirmación explícita antes de lanzar.

## Verification

- `read_file` on `~/.hermes/cache/scratch/agy-task.log` confirms clean exit without errors.
- `terminal` runs `git diff --stat` and the project's test/typecheck command with exit code `0`.
