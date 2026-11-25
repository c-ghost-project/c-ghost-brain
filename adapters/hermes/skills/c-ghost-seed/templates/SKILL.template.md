---
name: {{SKILL_NAME}}
description: "{{SKILL_DESCRIPTION}}"
version: 0.1.0
author: {{ORG}}
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    category: software-development
    tags: [{{PILAR}}, c-ghost]
    related_skills: [c-ghost-seed]
---

# {{SKILL_NAME}}

Skill del pilar {{PILAR}} para el proyecto {{PROJECT_NAME}}.

## When to Use

Usa esta skill cuando la Tarea Activa de `STATUS.md` toque el pilar {{PILAR}}: modelo, contratos, flujos o verificación asociados. No la uses para trabajo de otros pilares.

## Prerequisites

- `AGENTS.md` leído y vigente.
- Tarea Activa confirmada en `STATUS.md`.
- Acceso de lectura al código del pilar.

## How to Run

1. `read_file` sobre `STATUS.md` y esta skill.
2. `search_files` para localizar el código del pilar.
3. Aplicar el plan atómico con `patch`.
4. Verificar con `terminal` y registrar evidencia.

## Procedure

1. Comprender: mapa de entradas, salidas y efectos del cambio.
2. Decidir: alcance mínimo, verificación y rollback.
3. Ejecutar: cambio atómico y prueba dirigida.
4. Cerrar: handoff de 5 campos y propuesta de actualización de `STATUS.md`.

## Pitfalls

- Mezclar pilares en un mismo cambio.
- Escribir en `STATUS.md` sin ser el Guardián.
- Declarar éxito sin comando de verificación.
- Ampliar alcance con ideas nuevas en lugar de anotarlas en `IDEAS.md`.

## Verification

Declara aquí el comando exacto del pilar y el resultado esperado. Sin evidencia, la tarea no se cierra.
