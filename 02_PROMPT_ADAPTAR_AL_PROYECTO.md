# 🦎 PROMPT 2: Adaptar el Cerebro al Proyecto (Morfogénesis `C://GHOST v3.0`)

> **Cuándo usar este prompt:** Inmediatamente **después** de haber plantado la semilla con el Prompt 1 (o con `./plant-seed.sh`).  
> **Instrucción:** Copia el bloque completo inferior y pégalo en tu conversación. Puedes rellenar la sección opcional **"Descripción de mi proyecto"** al final, o dejarla vacía si prefieres que el agente te entreviste o analice un código ya existente en la carpeta.

---

````markdown
Ejecuta ahora la **FASE DE ADAPTACIÓN (MORFOGÉNESIS)** sobre el Cerebro Universal `C://GHOST v3.0` recién sembrado en este proyecto.

### 🧠 TU MISIÓN: ADAPTAR EL CEREBRO AL ADN EXACTO DE ESTE PROYECTO
Lee primero `.agents/AGENTS.md` y `STATUS.md` (Protocolo 0), y evalúa cuál de los 3 escenarios aplica antes de modificar archivos:

1. **Escenario A — Proyecto Nuevo con Descripción Abajo:** Si rellené la sección *"Descripción de mi proyecto"* al final de este mensaje, úsala como fuente de verdad. Solo pregunta si existe alguna ambigüedad crítica de arquitectura o seguridad.
2. **Escenario B — Proyecto Nuevo sin Descripción (Modo Entrevista):** Si la sección inferior está vacía y no hay código fuente en el directorio, realiza primero una **entrevista breve y estructurada** (usando `ask_question` o máximo 5 preguntas concretas) para definir:
   - Objetivo central y tipo de producto (Web, API, Móvil, Desktop, CLI, IA/Datos, Juegos, etc.).
   - Lenguaje(s), framework(s) y base de datos preferidos (o pídeme que te recomiende el stack ideal).
   - Entorno de ejecución/despliegue (solo local, Docker/VPS, AWS, GCP, Azure, Cloudflare, móvil, etc.).
   - Nivel de criticidad de seguridad/privacidad de datos.
   - ¿Usaremos algún gestor de tareas externo opcional (GitHub Issues, Jira, Linear, Trello) o trabajaremos 100% autónomos solo con `STATUS.md`? *(Por defecto: 100% local en `STATUS.md`)*.
3. **Escenario C — Repositorio ya Existente (*Brownfield*):** Si ya existe código fuente en la carpeta, despacha primero un subagente `research` (`Model: "flash"`) para auditar el lenguaje real, dependencias (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `composer.json`, etc.), estructura de carpetas y comandos de prueba/build reales antes de proponer la adaptación.

---

### 🔧 TRANSFORMACIONES OBLIGATORIAS DEL CEREBRO (UNA VEZ DEFINIDO EL PROYECTO)

1. **Especializar `.agents/AGENTS.md` (Manteniendo intactos los 10 Protocolos):**
   - Reemplaza la sección `[PENDIENTE_DE_ADAPTACION]` con:
     - **Visión y Fronteras del Proyecto:** Qué construimos y qué queda fuera de alcance.
     - **Arquitectura y Módulos Reales (`1..N`):** Solo los módulos que este proyecto realmente necesita (no inventes módulos ni servicios que no hagan falta), definiendo cómo se comunican entre sí y sus reglas de aislamiento de datos.
     - **Stack Tecnológico y Entorno Real:** Lenguajes, frameworks, bases de datos y entorno de ejecución reales.
     - **Comandos Exactos del Gate de Verificación (Protocolo 7):** Los comandos reales de build, verificación de tipos, linter y tests de este stack (ej. `pytest`, `npm test`, `cargo test`, `go test ./...`, etc.).
     - **Gobernanza de Tareas:** Por defecto `STATUS.md` local; solo documenta sincronización con GitHub Issues / Jira / Linear / Trello si el usuario lo pidió expresamente.
     - **Tabla de Enrutamiento de Skills Progresivas:** Mapeo exacto hacia las skills creadas en el paso siguiente.

2. **Generar Skills Progresivas a Medida (`.agents/skills/<dominio>/SKILL.md`):**
   - Crea únicamente entre **3 y 7 skills especializadas** acordes al stack real del proyecto (por ejemplo: backend/API, base de datos, frontend/UI, pruebas/QA, seguridad, despliegue/CI, documentación).
   - Cada `SKILL.md` debe llevar frontmatter YAML válido (`name` y `description`), disparadores concretos, reglas de oro del stack, un patrón de código canónico de referencia y sus comandos reales de verificación.

3. **Actualizar la Memoria Viva y Registrar `ADR-001`:**
   - Crea `docs/adr/ADR-001-arquitectura-inicial.md` resumiendo la arquitectura elegida, el stack, las alternativas descartadas y los criterios de seguridad.
   - Actualiza `STATUS.md` (respetando estrictamente **≤ 100 líneas**) con:
     - Estado: `🟢 CEREBRO ADAPTADO — LISTO PARA FASE 1`.
     - Tabla de Módulos del proyecto.
     - `Tarea Activa` (`F1-T01`) y `Backlog Priorizado` en orden de dependencia.
   - Registra el hito de adaptación en `CHANGELOG.md`.

4. **Detenerse y Pedir Confirmación:**
   - Muestra un resumen ejecutivo de la arquitectura, las skills creadas y la propuesta de `F1-T01`, y **espera mi aprobación (`Procede`) antes de empezar a programar el primer módulo**.

---

### 📝 DESCRIPCIÓN DE MI PROYECTO *(Opcional — rellena aquí o déjalo en blanco para activar el Modo Entrevista / Escaneo automático)*:

- **Nombre del proyecto:** [Opcional]
- **Qué quiero construir y para quién:** [Describe tu idea con tus propias palabras]
- **Tecnologías o preferencias (si tengo alguna):** [Opcional: ej. Python + FastAPI, Flutter, Rust, o "recomiéndame tú"]
- **Dónde se ejecutará / desplegará:** [Opcional: ej. local, VPS Docker, AWS, GCP, móvil, web]
- **Gestor de tareas externo:** [Ninguno — solo STATUS.md local | GitHub Issues | Jira | Linear | Trello]
````
