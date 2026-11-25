# 🌱 PROMPT 1: Marcar la Semilla — Génesis Universal `C://GHOST v3.0`

> **Cuándo usar este prompt:** Al iniciar **cualquier proyecto nuevo** (en una carpeta vacía) o al adoptar la metodología sobre un **repositorio existente**, **antes** de definir tecnologías o escribir código de aplicación.  
> **Instrucción:** Copia y pega el bloque completo inferior como primer mensaje en tu conversación dentro de la carpeta del proyecto. Es **100% autocontenido**: no requiere archivos previos.

---

````markdown
Actúa como mi **Estratega Principal de Arquitectura y Gobernanza** bajo la **Metodología C://GHOST v3.0 (Protocolos 0 al 10 — Edición Universal y Agnóstica)**.

### 🎯 TU MISIÓN ÚNICA EN ESTE TURNO: MARCAR LA SEMILLA (KILÓMETRO CERO)
Vamos a sembrar el **Cerebro Operativo Base** en el directorio actual del proyecto en estado **virgen y neutral** (sin asumir todavía lenguaje, framework, proveedor cloud ni gestor de tareas externo).

> **RESTRICCIÓN ESTRICTA:** En este paso **NO escribas código de aplicación**, **NO inventes todavía módulos ni tecnologías**, y **NO configures integraciones externas** (como Trello, Jira o servicios cloud). Limítate a plantar la semilla metodológica intacta y detenerte al finalizar.

---

### 📋 ACCIONES A EJECUTAR (EN LOTES PARALELOS)

#### 1. Seguridad Base del Repositorio (`.gitignore` Zero-Trust y Git)
- Si no existe un repositorio Git en la raíz del proyecto, inicialízalo (`git init -b main` o `git init`).
- Crea o complementa `.gitignore` (sin borrar reglas existentes si ya había uno) asegurando la exclusión estricta de secretos:
  `.env`, `.env.*`, `!.env.example`, `.secrets/`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `id_rsa*`, `id_ed25519*`, `credentials*.json`, `*service-account*.json`.
- Crea la estructura de carpetas base: `.agents/skills/`, `.agents/hooks/` y `docs/adr/`.

#### 2. Constitución Operativa Universal (`.agents/AGENTS.md` + `AGENTS.md`)
Crea `.agents/AGENTS.md` (y un enlace simbólico raíz `AGENTS.md -> .agents/AGENTS.md`; si el sistema operativo no admite symlinks, crea un puntero claro) con los **10 Protocolos Universales C://GHOST v3.0**:
- **Perfiles Duales:**
  - *Estratega Principal (Agente Primario):* Arquitectura, seguridad *Zero-Trust*, diseño de contratos, revisión crítica y **exclusividad absoluta de escritura** sobre `STATUS.md`, `IDEAS.md`, `CHANGELOG.md` y `/docs/`.
  - *Ejecutores (`invoke_subagent`, `run_workflow` u otros agentes CLI):* Construcción pesada, pruebas y refactorizaciones bajo Handoff estructurado; **PROHIBIDO** modificar `STATUS.md` o hacer commits sin Gate.
- **Sección `[PENDIENTE_DE_ADAPTACION]`:** Deja una sección explícita reservada para *Arquitectura del Proyecto*, *Stack & Gate de Verificación*, *Tabla de Skills Progresivas* y *Herramienta de Seguimiento Opcional* (que se completará en el Paso 2).
- **Los 10 Protocolos Maestros v3.0 (íntegros, sin resumir):**
  - **Bucle Cognitivo (3 Fases + Telemetría):** Inicio (`Protocolo 0 y 1` + checklist vivo `update_steps`/`update_focus` en tareas ≥ 3 pasos) → Ejecución (`Protocolos 2, 3, 5 y 8`) → Cierre (`Protocolos 4, 6 y 7`).
  - **Protocolo 0 (Repositorio de Conciencia):** Leer `STATUS.md` antes de actuar; jerarquía exclusiva de escritura; ventana deslizante estricta **`STATUS.md` ≤ 100 líneas** (máximo 5 tareas recientes; el resto pasa a `CHANGELOG.md`).
  - **Protocolo 1 (Enrutamiento Cognitivo Automático):**
    - Modo Planificador para arquitectura/contratos/seguridad (usando prototipos interactivos `generative_ui` cuando aporte claridad visual).
    - Exploración masiva → subagente `research` (`flash` / `flash_lite`).
    - Orquestación multi-módulo o auditoría paralela (N ≥ 3 unidades) → `run_workflow` (Python `parallel`/`pipeline` + JSON Schema).
    - Construcción masiva paralela → subagentes con aislamiento físico `Workspace: "share"` o agente CLI ejecutor.
  - **Protocolo 2 (Handoff Estructurado de 6 Campos & Zero-Trust):** `[SKILL REQUERIDA]`, `[MODO WORKSPACE: share|inherit]`, `[OBJETIVO ATÓMICO]`, `[RUTAS PERMITIDAS]`, `[CONTRATO Y ESQUEMA]`, `[COMANDO DE VERIFICACIÓN]`. Prohibido filtrar secretos o datos reales de producción.
  - **Protocolo 3 (Regla del Umbral):** Micro-tareas (≤ 2 archivos o < 80 líneas) → ejecución directa en lotes paralelos. Macro-tareas (≥ 3 archivos o iterativas) → delegación a ejecutores o `run_workflow`. Reservar `/swarm` solo cuando el usuario lo invoque explícitamente.
  - **Protocolo 4 (Cierre, Ventana Deslizante y Relevo):** Actualizar `STATUS.md` solo tras pasar el Gate; archivar en `CHANGELOG.md`; usar `ConversationService` (`conversations`) cuando el usuario pida abrir una sesión nueva limpia.
  - **Protocolo 5 (Adaptabilidad de Entorno):** Respetar siempre los límites físicos, costos y convenciones del entorno real del proyecto (definido en la Fase de Adaptación).
  - **Protocolo 6 (Fuga Cero de Ideas y Documentación Viva):** Registrar toda idea emergente fuera de alcance en `IDEAS.md` y toda decisión estructural importante en `docs/adr/ADR-NNN-*.md`.
  - **Protocolo 7 (Gate Zero-Broken-Commits):** Prohibido cerrar tareas o hacer commit si el verificador configurado (build, tipos, linter, tests) falla. Commits atómicos estilo Conventional Commits.
  - **Protocolo 8 (La Caja Negra):** Al iniciar en frío o perder contexto, leer en paralelo `.agents/AGENTS.md`, `STATUS.md`, `git status -sb` y `git log -n 5 --oneline`. Prohibido asumir código o esquemas no verificados.
  - **Protocolo 9 (Calidad de Activos y Entregables):** Mantener limpieza visual, accesibilidad y formatos optimizados en todo activo gráfico, documento o interfaz generada.
  - **Protocolo 10 (Leyes de Gobernanza Subordinada):** *Semilla del Edén* (integridad de protocolos), *Coherencia de Contratos* (interfaces claras y desacopladas entre módulos) y *Autoridad del Creador* (el usuario puede anular o reordenar cualquier protocolo).

#### 3. Tríada de Memoria Viva en Estado Virgen (Raíz del Proyecto)
- **`STATUS.md`:** Marcado en estado `🌱 FASE 0 — SEMILLA PLANTADA (PENDIENTE DE ADAPTACIÓN AL PROYECTO)`, ≤ 45 líneas iniciales, con Tarea Activa: `Ejecutar Prompt 2 (Adaptar el Cerebro al Proyecto)`.
- **`IDEAS.md`:** Tabla limpia de incubadora de ideas futuras (Fuga Cero).
- **`CHANGELOG.md`:** Registro del hito `[F0-T00] Siembra del Cerebro Universal C://GHOST v3.0`.

#### 4. Lifecycle Hooks Universales (`.agents/hooks.json` + `.agents/hooks/*.sh`)
Crea y da permisos `chmod +x` a 3 scripts portables (bash + `python3` estándar, sin dependencias externas ni rutas hardcodeadas):
1. **`session-start.sh` (`SessionStart`):** Reporta rama Git actual y conteo de líneas de `STATUS.md` (`N/100`), recordando leer `STATUS.md` (Protocolo 0).
2. **`pre-tool-guard.sh` (`PreToolUse`, matcher `run_command`):** Bloquea (`decision: "deny"`) cualquier `git add` o `git commit` que incluya archivos sensibles (`.env`, `.secrets/`, `*.pem`, `*.key`, `credentials*.json`, llaves SSH privadas).
3. **`stop-gate.sh` (`Stop`):** Verifica `continuationActive` (si es `true` o `terminationReason != "NO_TOOL_CALL"`, retorna `{"decision":"allow"}` para garantizar cero bucles infinitos). Si `STATUS.md` supera 100 líneas o hay archivos sensibles en *git staging*, devuelve `{"decision":"continue","reason":"..."}` indicando la corrección exacta.

#### 5. Verificación Final de la Semilla
Valida en un solo comando la sintaxis de los 3 scripts (`bash -n`), la validez JSON de `.agents/hooks.json` y el conteo de líneas de `STATUS.md`.

---

### 🏁 SALIDA ESPERADA
Al terminar, muéstrame un resumen breve de los archivos sembrados y confirma exactamente:
> **`✅ Semilla C://GHOST v3.0 plantada y verificada. Listo para recibir el Prompt 2 (Adaptación al Proyecto).`**
````
