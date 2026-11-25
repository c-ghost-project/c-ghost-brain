# AGENTS.md — Constitución C://GHOST v2.1

Proyecto: {{PROJECT_NAME}}
Organización: {{ORG}}
Stack: {{STACK}}
Vigente desde: {{DATE}}
version: {{BRAIN_VERSION}}

Este archivo es la ley operativa del proyecto. Todo agente que trabaje aquí —Antigravity CLI (`agy`), OpenCode CLI o Hermes— lo lee completo antes de escribir. Si una instrucción de sesión contradice esta constitución, gana la constitución y la contradicción se reporta.

## Bucle Cognitivo de 4 Fases

Toda tarea recorre estas fases en orden. No se salta ninguna.

1. **Fase 0 — Pre-flight (Obligatorio).** Ejecuta `./.agents/scripts/preflight_check.sh`. Solo si exit code 0 → continuar.
2. **Fase 1 — Inicio.** Lee `STATUS.md` y `.hermes.md`, detecta skill, ejecuta clasificador de intención (`./.agents/scripts/intent_classify.py`).
3. **Fase 2 — Ejecución.** Aplica Protocolos 2, 3, 5, 11 (umbral delegación, Handoff 5 campos + cuota Antigravity, background `notify_on_complete=true`, adaptación entorno). Si falta contexto, Protocolo 8.
4. **Fase 3 — Cierre.** Gate de Verificación (P7), actualiza memoria deslizante (P0, P4, P12), registra ideas (P6), autogenera artefactos visuales (P9+/N4).

## Pirámide de 5 Niveles (Automatización + Aprovechamiento Extremo de Tokens)

| Nivel | Costo | Motor / Skill | Cuándo se usa |
|-------|-------|---------------|---------------|
| **0** | 0 tokens | `preflight_check.sh` (determinístico) | **Siempre primero**: linters, typecheck, test discovery, git diff, STATUS.md ≤100 líneas |
| **1** | $0 | Nativo Hermes: `nemotron-3.5-super-vl-120b-a12b` (default), `nemotron-3-ultra-550b-a55b`, `mistral-large-4-1t-a52b`, `nemotron-3-nano-omni-30b-a3b-reasoning`, `qwen2.5:7b` (local) | ~60% trabajo: chat, análisis, redacción, razonamiento, contingencia offline |
| **2** | $0 | `opencode-cli` → `opencode/deepseek-v4.1-flash-free` | Scaffolding, refactors mecánicos, migraciones, tests (`≥3 archivos` o `>80 líneas`) |
| **3** | Cuota | `antigravity-cli` → `gemini-4-carbon-high`, `claude-sonnet-5-5-medium`, `claude-opus-5-5-medium`, `gemini-4-neon-medium`, `gemini-4-argon-medium` | Arquitectura crítica/Zero-Trust, UI/UX, WhitePapers, Full-Stack difícil, algoritmos/SQL |
| **4** | $0 | `visual_gen.py` (Chrome headless) | Autogenera Mermaid → PNG/PDF si la tarea produce arquitectura, flujo o decisión de diseño |

## Clasificador de Intención Embebido (Pre-P1)

Antes de actuar, ejecuta `intent_classify(entrada)` → devuelve JSON:
```json
{
  "tipo": "Consulta|Exploración|Arquitectura|Macro-Construcción",
  "nivel_recomendado": 0|1|2|3|4,
  "skill": "none|opencode-cli|antigravity-cli|c-ghost-seed",
  "confianza": 0.0-1.0,
  "requiere_preflight": true|false
}
```
Umbral: si `confianza < 0.75` → pregunta al Creador (no asumir).

## Los 12 Protocolos Maestros C://GHOST v2.1

### P0 — Conciencia y Exclusividad
En cualquier proyecto, lee primero `STATUS.md` (máx. 100 líneas, últimas 5 tareas + campo `cuota_antigravity_usada`). Solo tú escribes en `STATUS.md`, `IDEAS.md` y `CHANGELOG.md`; los ejecutores delegados tienen prohibido editarlos.

### P1 — Zero-Command Routing
Clasifica cada pedido automáticamente (Consulta / Exploración / Arquitectura / Macro-Construcción) vía **Clasificador de Intención Embebido** y activa la skill o nivel óptimo sin exigir comandos manuales al Creador.

### P2 — Handoff Estructurado y Zero-Trust
Toda delegación a `opencode-cli` o `antigravity-cli` debe llevar exactamente 5 campos:
- `[SKILL REQUERIDA]`
- `[OBJETIVO ATÓMICO]`
- `[RUTAS PERMITIDAS]`
- `[CONTRATO Y RESTRICCIONES]`
- `[COMANDO DE VERIFICACIÓN]`

Prohibido pasar `.env`, credenciales, llaves privadas o datos reales de clientes.

### P3 — Economía de Fuerzas + Cuota Antigravity
Micro-tareas (`≤ 2 archivos` o `< 80 líneas`) las ejecutas directamente. Macro-tareas (`≥ 3 archivos` o `> 80 líneas`) se delegan en 2.º plano y se auditan solo con `git diff --stat` + comando de verificación. **Antes de Nivel 3**, verifica `cuota_antigravity_usada` en `STATUS.md`; si > 80% → alerta y pide confirmación.

### P4 — Cierre y Ventana Deslizante
Al cerrar una tarea verificada, actualiza `STATUS.md` (incluye `cuota_antigravity_usada` actualizado) y desplaza lo anterior a las últimas 5 tareas hacia `CHANGELOG.md`.

### P5 — Bifurcación de Entornos
Adapta criterio y tono según entorno: Serverless/Cloud (TypeScript estricto y BD compartimentada), VPS/Hosting (RAM/CPU/inodos), Directivo/WhitePaper (ROI y gobernanza) y Móvil (concisión en WhatsApp/Telegram).

### P6 — Fuga Cero de Ideas y WhitePaper
Registra ideas futuras en `IDEAS.md` sin contaminar `STATUS.md`; sincroniza hitos arquitectónicos en `/docs/whitepaper/`.

### P7 — Gate de Verificación (Zero-Broken-Commits)
Prohibido cerrar tareas o hacer commits (`Conventional Commits`) si typecheck, lint o tests fallan. Toda alteración SQL requiere migración numerada.

### P8 — La Caja Negra
Si falta contexto entre sesiones, inspecciona `STATUS.md`, `CHANGELOG.md`, `git log` y manifiestos (`package.json`/`pyproject.toml`) antes de asumir esquemas o rutas.

### P9 — Activos Visuales
Imágenes web optimizadas a `.webp` con carga diferida (`loading="lazy"`) y estética limpia sin fondo ruidoso.

### P10 — Semilla del Edén y Autoridad
Todo proyecto nuevo nace mediante la skill `c-ghost-seed` con `.hermes.md`, `AGENTS.md`, `STATUS.md`, `IDEAS.md`, `CHANGELOG.md` y `.agents/skills/` íntegros. El Creador conserva autoridad directa para priorizar o ajustar cualquier flujo bajo instrucción explícita.

### P11 — Hook Pre-Delegación (Nivel 0 Obligatorio)
Antes de armar cualquier handoff (Nivel 2 o 3), ejecuta `./.agents/scripts/preflight_check.sh` en el directorio del proyecto. Solo si exit code 0 → procede. Salida se adjunta al handoff como `[PREFLIGHT_REPORT]`.

### P12 — Migración de Semilla y Versionado
Si `c-ghost-seed` detecta `STATUS.md`/`AGENTS.md` preexistentes → **no usa `--force`**. En su lugar: `c-ghost-seed --migrate` genera diff de tres vías (plantilla vs actual vs proyecto) y propone merge interactivo. Versión de cerebro en `.hermes.md#version` (ej: `v2.1.0`).

## Handoff de 5 Campos (Formato Obligatorio)

```text
[SKILL REQUERIDA]       opencode-cli | antigravity-cli | c-ghost-seed
[OBJETIVO ATÓMICO]      Qué se debe lograr (una frase, verificable)
[RUTAS PERMITIDAS]      Archivos/directorios que PUEDE tocar (excluye STATUS.md, IDEAS.md, CHANGELOG.md, .env)
[CONTRATO Y RESTRICCIONES]  Qué NO hacer, convenciones, tests requeridos, estilo
[COMANDO DE VERIFICACIÓN]   Comando exacto que debe pasar para dar la tarea por buena
```

## Pirámide de 4 Niveles (Legado — mantener para compatibilidad)

- **Vértice — Gobierno:** `AGENTS.md` y `.hermes.md`. Ley y delta del proyecto.
- **Nivel 2 — Estrategia:** `STATUS.md`. Estado global, tarea activa y backlog.
- **Nivel 3 — Ejecución:** `.agents/skills/`, `src/` y `docs/`. Trabajo real y capacidades por pilar.
- **Base — Evidencia:** `CHANGELOG.md`, `IDEAS.md` y `docs/whitepaper/`. Historia, intención y fundamento.

Un nivel no reescribe a otro. La estrategia no edita código; la ejecución no edita la ley.

## Exclusividad de Escritura

| Archivo | Escritor | Otros agentes |
|---------|----------|---------------|
| `AGENTS.md` | Guardián | solo lectura |
| `.hermes.md` | Guardián | solo lectura |
| `STATUS.md` | Guardián | proponen vía handoff |
| `IDEAS.md` | Guardián | proponen vía handoff |
| `CHANGELOG.md` | Guardián | proponen vía handoff |
| Código y skills | Agente asignado | coordinan por pilar |

El Guardián es el humano responsable o el agente líder designado en la Tarea Activa. Si no sabes quién es, pregunta antes de escribir.

## Convivencia Multiagente

- Un pilar, un agente responsable a la vez.
- Antes de empezar, confirma en `STATUS.md` que la Tarea Activa te pertenece.
- No edites archivos fuera de tu pilar sin handoff explícito.
- Al terminar, entrega los cinco campos y deja el árbol limpio y verificable.

## Checklist de Arranque

1. Leí `AGENTS.md`, `.hermes.md` y `STATUS.md`.
2. Ejecuté `./.agents/scripts/preflight_check.sh` (Fase 0).
3. Identifiqué la Tarea Activa y su verificación.
4. Ejecuté clasificador de intención (Pre-P1).
5. Revisé la skill del pilar y el código que voy a tocar.
6. Escribí un plan atómico con rollback.
7. Ejecuté, verifiqué y registré evidencia.

## Vigencia

Esta constitución se revisa al cerrar cada hito. Todo cambio se registra en `CHANGELOG.md` y se comunica con el handoff de 5 campos.