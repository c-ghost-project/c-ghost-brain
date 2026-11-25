---
name: opencode-cli
description: "Delegate heavy coding to free OpenCode CLI in background."
version: 1.0.0
author: Dugui & Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    category: autonomous-ai-agents
    tags: [Coding-Agent, OpenCode, Free-Tier, Scaffolding, Background]
    related_skills: [antigravity-cli, c-ghost-seed]
---

# OpenCode CLI Skill

Delegate repetitive scaffolding, multi-file edits (`>= 3` files or `> 80` lines), SQL migrations, and unit test suites to the free OpenCode CLI (`~/.local/bin/opencode`) running in the background via `terminal`. Follows the **OpenCode-First** policy ($0 cost) to preserve Antigravity quota.

## When to Use

- Creating or modifying `>= 3` files or `> 80` lines of boilerplate/scaffolding.
- Writing unit test suites, mocks, migrations, or repetitive refactors.
- Running iterative compile/test loops that produce heavy console output.

## Prerequisites

- Binary available at `~/.local/bin/opencode` (symlinked from `~/.opencode/bin/opencode`).
- Only free models (`-free` or `big-pickle`) may be selected — never pick paid models.

## Free Model Selection

| Task Type | `-m` Model Flag ($0) |
| :--- | :--- |
| General coding, scaffolding, tests *(default)* | `opencode/deepseek-v4.1-flash-free` |
| Multimodal / larger context refactors | `opencode/nemotron-3.5-super-vl-free` |
| Fast lightweight edits | `opencode/nemotron-3.5-lightning-free` |
| Alternative free coding model | `opencode/flint-40b-free` or `opencode/big-pickle` |

## How to Run

Always execute inside the project directory via `terminal` with `background=true` and `notify_on_complete=true`, writing stdout/stderr to a scratch log:

```bash
~/.local/bin/opencode run \
  -m opencode/deepseek-v4.1-flash-free \
  --auto \
  "<STRUCTURED_5_FIELD_HANDOFF>" \
  > "$HOME/.hermes/cache/scratch/opencode-task.log" 2>&1
```

## Procedure

0. **Puerta previa (C://GHOST v2.1, obligatoria — aplica a Nivel 2 y Nivel 3).** Desde la raíz del proyecto ejecuta `./.agents/scripts/preflight_check.sh`; solo con exit 0 procede (Protocolo 11). Adjunta su salida al handoff como `[PREFLIGHT_REPORT]`.
1. Assemble the C://GHOST **5-field Handoff**:
   - `[SKILL REQUERIDA]`
   - `[OBJETIVO ATÓMICO]`
   - `[RUTAS PERMITIDAS]` (prohibit modifying `STATUS.md`, `IDEAS.md`, `CHANGELOG.md`)
   - `[CONTRATO Y RESTRICCIONES]` (Zero-Trust: never touch `.env` or real credentials)
   - `[COMANDO DE VERIFICACIÓN]`
2. Launch with `terminal(command=..., workdir=<project>, background=true, notify_on_complete=true)`.
3. In non-async contexts (`cron`), monitor with `process_manage(action='poll')` or `process_manage(action='wait')`.
4. Upon completion, inspect `~/.hermes/cache/scratch/opencode-task.log` via `read_file` and verify via `git diff --stat` + the verification command.

## Pitfalls

- Calling bare `opencode` without `~/.local/bin/opencode` fails if `PATH` is stripped.
- Omitting `--auto` can stall waiting for interactive permission prompts in background mode.
- Never re-read every modified file in full; audit with `git diff --stat` and targeted `read_file` checks.
- Omitir el preflight antes de delegar (P11): sin `./.agents/scripts/preflight_check.sh` en exit 0 no se arma ningún handoff, ni a Nivel 2 ni a Nivel 3 — un typecheck o lint roto se propaga al delegado.

## Verification

- `read_file` on `~/.hermes/cache/scratch/opencode-task.log` shows completion without errors.
- `terminal` runs `git diff --stat` and the project's test/build command with exit code `0`.
