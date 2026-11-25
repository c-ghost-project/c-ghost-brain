---
name: c-ghost-seed
description: "Bootstrap C://GHOST v2.1 brain files in any new project."
version: 2.1.0
author: José Dugarte | Dugui - Metodología C-GHOST
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    category: software-development
    tags: [Architecture, C-GHOST, Scaffolding, Governance, Automation, v2.1]
    related_skills: [antigravity-cli, opencode-cli]
---

# C://GHOST Seed Skill v2.1

Semilla del Edén. Inicializa el cerebro genérico de un proyecto nuevo con la metodología C://GHOST v2.1: constitución para agentes, memoria viva acotada con rastreo de cuota, registro de ideas, histórico de hitos, **automatización de 5 niveles** y **4 scripts de soporte** (preflight, clasificador de intención, rastreador de cuota y generador visual). El resultado funciona con Hermes, Antigravity CLI (`agy`) y OpenCode CLI sin adaptaciones.

## When to Use

Usa esta skill cuando el usuario quiera:

- Arrancar un proyecto de software desde cero con gobernanza, memoria persistente y automatización.
- Añadir el cerebro C://GHOST v2.1 a un repositorio existente (usa `--migrate`).
- Estandarizar varios proyectos bajo la misma constitución de agentes.
- Preparar un proyecto para que `agy` u OpenCode CLI trabajen sin perder contexto entre sesiones.
- Migrar un proyecto existente de v2.0 a v2.1 sin perder memoria viva.

No la uses para modificar un cerebro ya existente sin querer migrar: en ese caso edita los archivos con `patch` de forma deliberada.

## Prerequisites

- Python 3.8 o superior disponible como `python3`.
- Permiso de escritura en el directorio destino.
- El directorio de plantillas de esta skill intacto en `templates/`.
- Una decisión mínima sobre nombre del proyecto, organización y stack. Si faltan, los valores por defecto son `Personal` y `Por definir`.
- Para `visual_gen.py`: Chrome/Chromium instalado (opcional, solo para artefactos visuales).

## How to Run

Ejecución directa con valores explícitos:

```bash
python3 scripts/init_c_ghost.py \
  --dir /ruta/al/proyecto \
  --name "Nombre del Proyecto" \
  --org "Mi Organización" \
  --stack "Python 3.12 + SQLite"
```

Ejecución mínima:

```bash
python3 scripts/init_c_ghost.py --dir ./mi-proyecto --name "Mi Proyecto"
```

**Migración de proyecto existente (v2.0 → v2.1):**

```bash
python3 scripts/init_c_ghost.py --dir ./mi-proyecto --name "Mi Proyecto" --migrate
```

Esto preserva `STATUS.md`, `IDEAS.md`, `CHANGELOG.md`, `.hermes.md` y `AGENTS.md`, muestra diffs de tres vías y solo crea/actualiza los scripts nuevos en `.agents/scripts/`.

Reemplazar archivos existentes de forma consciente:

```bash
python3 scripts/init_c_ghost.py --dir ./mi-proyecto --name "Mi Proyecto" --force
```

Antes de ejecutar, verifica el destino con `terminal("ls -la /ruta/al/proyecto")` y confirma que no hay trabajo previo que se pueda perder.

## Procedure

1. **Inspeccionar el destino.** Usa `terminal` para listar el directorio y `search_files` para detectar un `STATUS.md` o `AGENTS.md` previo. Si existen y no quieres migrar, detente y pregunta antes de usar `--force`.
2. **Confirmar los datos.** Nombre, organización y stack. El nombre se usa en todas las plantillas; la organización firma la constitución; el stack describe la realidad técnica, no la deseada.
3. **Ejecutar la semilla.** Lanza `scripts/init_c_ghost.py` con `terminal`. El script solo usa la biblioteca estándar y no toca nada fuera de `--dir`.
4. **Revisar el resumen.** Deben aparecer once rutas: `.hermes.md`, `AGENTS.md`, `STATUS.md`, `IDEAS.md`, `CHANGELOG.md`, `.agents/skills/01-core-domain/SKILL.md`, `docs/whitepaper/README.md` y los 4 scripts en `.agents/scripts/`. Cualquier `omitido` indica un archivo preexistente.
5. **Ajustar los pilares.** Lee `.hermes.md` con `read_file` y adapta la tabla de pilares al proyecto real con `patch`. Si renombras el pilar 01, renombra también su carpeta en `.agents/skills/`.
6. **Definir la Tarea Activa.** Edita `STATUS.md` con `patch`: objetivo, pilar, responsable, verificación y rollback. Sin este paso el cerebro queda en estado de arranque.
7. **Verificar preflight.** Ejecuta `./.agents/scripts/preflight_check.sh` para confirmar que el entorno está verde.
8. **Entregar el handoff.** Comunica al usuario los cinco campos del Protocolo 2: `[SKILL REQUERIDA]`, `[OBJETIVO ATÓMICO]`, `[RUTAS PERMITIDAS]`, `[CONTRATO Y RESTRICCIONES]`, `[COMANDO DE VERIFICACIÓN]`.

## Scripts Generados (Nivel 0)

| Script | Comando | Función |
|--------|---------|---------|
| `preflight_check.sh` | `./.agents/scripts/preflight_check.sh` | Valida linters, typecheck, tests, git diff, STATUS.md ≤100 líneas. Exit 0 = verde. **Obligatorio antes de delegar (P11)** |
| `intent_classify.py` | `echo "texto" \| ./.agents/scripts/intent_classify.py` | Clasifica intención → JSON con tipo, nivel, skill, confianza |
| `quota_tracker.py` | `./.agents/scripts/quota_tracker.py read\|add\|check` | Lee/actualiza `cuota_antigravity_usada` en STATUS.md |
| `visual_gen.py` | `echo "mermaid" \| ./.agents/scripts/visual_gen.py nombre` | Genera PNG (1920px, scale 2) + PDF (A4) en `.agents/artifacts/` |

## Pitfalls

- **Sobrescribir trabajo previo.** `--force` reemplaza archivos completos. Úsalo solo tras leer el contenido actual con `read_file`. Para migración usa `--migrate`, nunca `--force`.
- **Confundir plantilla con proyecto.** Las plantillas viven en esta skill; los archivos generados viven en el proyecto. No edites las plantillas para un caso puntual.
- **Dejar `STATUS.md` sin Tarea Activa.** Un cerebro sin tarea activa no guía a ningún agente; el primer trabajo es definirla.
- **Pilares decorativos.** Si los pilares no coinciden con la arquitectura real, `STATUS.md` y `.agents/skills/` pierden valor. Ajusta ambos a la vez.
- **Romper la exclusividad de escritura.** Solo el Guardián escribe `STATUS.md`, `IDEAS.md` y `CHANGELOG.md`. Los agentes delegados leen y proponen.
- **Descripción de skill demasiado larga.** El frontmatter de cada skill de pilar admite un máximo de 60 caracteres en `description`. El script recorta automáticamente, pero revisa el resultado.
- **Ejecutar sin Python 3.** Verifica con `terminal("python3 --version")` antes de culpar al script.
- **Olvidar el preflight antes de delegar.** El Protocolo 11 es obligatorio: sin `preflight_check.sh` en verde, no armes handoffs a Nivel 2 o 3.
- **Ignorar la cuota Antigravity.** Antes de usar Nivel 3, ejecuta `quota_tracker.py check`. Si supera 80%, pide confirmación al Comandante.
- **Embeber código generado en strings no-raw.** Toda función de `init_c_ghost.py` que retorne el texto de un script embebido debe usar raw string (`r'''...'''`): un `\n`, `\s` u otro escape dentro del código generado se interpreta en el parser exterior y corrompe el archivo destino (p. ej. `SyntaxError: unterminated string literal` en el script generado). Tras sembrar, compila SIEMPRE los scripts generados, no solo el inicializador.

## Documentación de referencia (docs/)

- `docs/INFORME_EJECUTIVO_v2.1.md` — informe ejecutivo: qué cambió de v2.0 a v2.1, por qué y métricas de mejora.
- `docs/FLUJO_TRABAJO_v2.1.md` — diagramas Mermaid del bucle de 4 fases, la pirámide de 5 niveles, la secuencia de handoff y la migración segura.
- `docs/TUTORIAL_IMPLEMENTACION_v2.1.md` — tutorial paso a paso: proyecto nuevo, migración con `--migrate`, uso diario y troubleshooting.
- `docs/artifacts/` — PNG/PDF renderizados de los diagramas (generados con `visual_gen.py`).

## Verification

Comprueba la sintaxis y la estructura:

```bash
python3 -m py_compile ~/.hermes/skills/software-development/c-ghost-seed/scripts/init_c_ghost.py && ls -la ~/.hermes/skills/software-development/c-ghost-seed/templates/ ~/.hermes/skills/software-development/c-ghost-seed/scripts/
```

Comprueba una ejecución real en un directorio temporal:

```bash
python3 scripts/init_c_ghost.py --dir /tmp/c-ghost-demo --name "Demo" --org "ACME" --stack "Python"
find /tmp/c-ghost-demo -type f | sort
wc -l /tmp/c-ghost-demo/STATUS.md
cd /tmp/c-ghost-demo && ./.agents/scripts/preflight_check.sh
for f in .agents/scripts/*.py; do python3 -m py_compile "$f" || exit 1; done
bash -n .agents/scripts/preflight_check.sh
```

Criterios de éxito:

- `py_compile` termina sin errores.
- Se crean exactamente once archivos y ninguna ruta fuera del destino.
- `STATUS.md` queda por debajo de 100 líneas y contiene `cuota_antigravity_usada`.
- `AGENTS.md` contiene el Bucle Cognitivo de 4 Fases, los 12 Protocolos, el Handoff de 5 campos y la Pirámide de 5 Niveles.
- `preflight_check.sh` retorna exit code 0 en el proyecto generado (ejecutado desde la raíz del proyecto: deriva su ruta de su propia ubicación, no de argumentos posicionales).
- Los 4 scripts generados pasan `py_compile` (`.py`) y `bash -n` (`.sh`) — esto detecta strings embebidos mal escapados en las funciones generadoras de `init_c_ghost.py`.
- Ninguna plantilla contiene comentarios HTML ni instrucciones dirigidas a anular el comportamiento del agente.