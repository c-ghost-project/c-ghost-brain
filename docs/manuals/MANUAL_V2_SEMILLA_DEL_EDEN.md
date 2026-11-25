# 📘 Manual de Usuario `C://GHOST v2.0` — «Semilla del Edén» (De Cero a Operar Solo)

> **Audiencia:** Desarrolladores y arquitectos que desean gobernar proyectos multi-módulo o monorepos utilizando los **10 Protocolos Maestros**, memoria viva con ventana deslizante y **Skills de Divulgación Progresiva** (`.agents/skills/`).

---

## 1. Qué resuelve `C://GHOST v2.0` frente a `v1.0`

En proyectos grandes, un solo archivo `STATUS.md` que crece sin control termina saturando la ventana de contexto del modelo, y poner todas las reglas técnicas dentro de `AGENTS.md` desperdicia miles de tokens en cada turno. **`v2.0` introduce tres avances clave:**

1. **Tríada de Memoria Acotada:**
   * `STATUS.md` (≤ 100 líneas): memoria de corto plazo (*Tarea Activa* + solo las *últimas 5 tareas*).
   * `CHANGELOG.md`: archivo histórico permanente donde se desplazan las tareas antiguas.
   * `IDEAS.md` (*Fuga Cero*): estacionamiento para ideas emergentes sin distraer la tarea actual.
2. **Divulgación Progresiva (`.agents/skills/`):** Cada especialidad técnica (autenticación, backend, frontend, seguridad, base de datos) vive en su propio `SKILL.md` y solo se lee cuando se toca ese módulo.
3. **Zero-Command Routing y Handoff de 5 Campos:** El Estratega decide automáticamente si ejecuta micro-tareas (≤ 2 archivos / < 80 líneas) o si delega macro-tareas (≥ 3 archivos) con un contrato estructurado de 5 puntos.

---

## 2. Prerrequisitos (2 minutos)

* **Git** instalado (`git --version`).
* Un entorno con agente de IA compatible con archivos de workspace (Antigravity, Claude Code, Cursor, Windsurf o terminal con CLI).
* *(Opcional)* Terminal Bash (`Linux`, `macOS` o `Git Bash / WSL` en Windows) para usar el sembrador rápido.

---

## 3. Instalación Paso a Paso (De Cero hasta la Primera Tarea)

### Paso 1 — Crear la carpeta de tu proyecto
```bash
mkdir mi-proyecto && cd mi-proyecto
git init -b main
```

### Paso 2 — Sembrar la «Semilla del Edén»
Tienes dos caminos equivalentes:

* **Camino A (Automático con el script `v2.0`):**
  ```bash
  ./v2-seed/init-c-ghost-brain.sh /ruta/a/mi-proyecto "Mi Proyecto"
  ```
* **Camino B (Conversacional — copiando el Prompt Génesis):**
  Abre `v2-seed/00_PROMPT_INICIO_DESDE_CERO.md`, rellena los campos `[...]` con el nombre, visión y pilares de tu proyecto y pégalo como **primer mensaje** a tu agente.

Al finalizar este paso, verifica que existan en la raíz:
```text
mi-proyecto/
├── AGENTS.md           # Constitución con los 10 Protocolos
├── STATUS.md           # Memoria viva (≤ 100 líneas)
├── IDEAS.md            # Incubadora de ideas
├── CHANGELOG.md        # Histórico inmutable
└── .agents/skills/     # Carpetas de especialidades técnicas
```

### Paso 3 — Personalizar tus Pilares y Skills (Una sola vez)
1. Abre `AGENTS.md` y revisa la tabla de **Pilares** para que refleje los módulos reales de tu aplicación (puedes reducir a 3 pilares o expandir según necesites).
2. Revisa cada `.agents/skills/<dominio>/SKILL.md` y verifica sus **Reglas de Oro** y su **Comando de Verificación** (ej. `npm test`, `pytest`, `tsc --noEmit`).

### Paso 4 — Definir tu primera `Tarea Activa` en `STATUS.md`
Asegúrate de que la sección `## 🎯 Tarea Activa` indique un único objetivo atómico (por ejemplo: `F1-T01: Diseñar el esquema inicial de base de datos y contrato de API`).

---

## 4. Cómo Operar Solo Día a Día (El Bucle Cognitivo de 3 Fases)

Una vez sembrado el cerebro, tu trabajo como Creador del proyecto se simplifica a tres reglas de oro:

1. **Inicio de sesión (Fase 1):**  
   Solo dile al agente qué hito quieres abordar (o escribe *"Lee STATUS.md y dime cuál es el siguiente paso"*). El agente ejecutará el **Protocolo 0** (leer `STATUS.md`), activará solo la Skill correspondiente y te presentará un plan si el cambio es estructural.
2. **Ejecución y Delegación (Fase 2):**  
   * Para cambios pequeños (**≤ 2 archivos o < 80 líneas**), el agente edita directamente.
   * Para construcciones grandes (**≥ 3 archivos**), exige que use el **Handoff de 5 Campos (Protocolo 2)**:
     1. `[SKILL REQUERIDA]`
     2. `[OBJETIVO ATÓMICO]`
     3. `[RUTAS PERMITIDAS]`
     4. `[CONTRATO Y RESTRICCIONES]`
     5. `[COMANDO DE VERIFICACIÓN]`
3. **Cierre Seguro (Fase 3 — Protocolo 7):**  
   Nunca cierres una tarea sin ver pasar en verde el verificador (`typecheck` / `lint` / `test`). Luego pide al agente: *"Cierra la tarea en STATUS.md y prepara el commit"*. El Estratega actualizará `STATUS.md` (moviendo la 6.ª tarea más antigua a `CHANGELOG.md`) y ejecutará un commit limpio.

---

## 5. Solución Rápida de Problemas Frecuentes

| Síntoma | Causa | Solución Inmediata |
| :--- | :--- | :--- |
| El agente "olvida" en qué estaban al abrir un chat nuevo | No ejecutó el Protocolo 0 / 8 | Dile: *"Aplica Protocolo 8 (Caja Negra): lee `STATUS.md`, `CHANGELOG.md` y `git log -n 5`."* |
| `STATUS.md` superó las 100 líneas | Se acumularon tareas viejas | Dile: *"Aplica Protocolo 4: archiva las tareas antiguas en `CHANGELOG.md` y deja solo las últimas 5 en `STATUS.md`."* |
| Te surgió una buena idea a mitad de un bug | Riesgo de desviar el foco | Dile: *"Aplica Protocolo 6: registra esta idea en `IDEAS.md` y sigamos con la Tarea Activa."* |
| Un agente delegado tocó `STATUS.md` | Violación de jerarquía (P0) | Revierte `git checkout -- STATUS.md`; solo el Estratega Principal edita la memoria viva. |
