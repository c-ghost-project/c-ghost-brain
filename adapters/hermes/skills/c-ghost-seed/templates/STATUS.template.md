# STATUS.md — Memoria viva

Proyecto: {{PROJECT_NAME}}
Actualizado: {{DATE}}
Límite: 100 líneas. Si crece, archiva lo cerrado en `CHANGELOG.md`.

## Estado Global

- Salud: verde | ámbar | rojo
- Fase: descubrimiento | construcción | endurecimiento | mantenimiento
- Última verificación: pendiente
- Bloqueos: ninguno
- **cuota_antigravity_usada: 0**

## Tarea Activa

| Campo | Valor |
|-------|-------|
| Objetivo | Definir el primer objetivo atómico |
| Pilar | Core Domain |
| Responsable | Guardián |
| Inicio | {{DATE}} |
| Verificación | comando pendiente |
| Rollback | punto de retorno pendiente |

### Plan atómico

1. Comprender: leer `AGENTS.md`, esta tarea y el código del pilar.
2. Decidir: escribir el cambio mínimo y su verificación.
3. Ejecutar: aplicar, verificar y registrar evidencia.

## Estado por Pilar

| Pilar | Estado | Avance | Riesgo | Siguiente paso |
|-------|--------|--------|--------|----------------|
| Core Domain | pendiente | 0% | bajo | definir el modelo inicial |
| Experience | pendiente | 0% | bajo | definir el contrato de entrada |
| Platform | pendiente | 0% | bajo | definir el entorno local |

## Últimas 5 Tareas Completadas

| Fecha | Tarea | Pilar | Evidencia |
|-------|-------|-------|-----------|
| — | sin tareas archivadas | — | — |

## Backlog

| # | Tarea | Pilar | Prioridad | Dependencia |
|---|-------|-------|-----------|-------------|
| 1 | Completar el whitepaper inicial | Core Domain | alta | ninguna |
| 2 | Definir la primera skill de pilar | Core Domain | media | tarea 1 |
| 3 | Configurar verificación automatizada | Platform | media | ninguna |

## Handoff vigente

```text
Contexto:     arranque del proyecto con la semilla C://GHOST v2.1
Estado:       estructura creada, sin código de producto
Decisiones:   pilares Core Domain, Experience y Platform
Pendientes:   completar la Tarea Activa y su verificación
Verificación: pendiente de definir
```

## Reglas de este archivo

- Solo el Guardián escribe aquí.
- Máximo 100 líneas; lo cerrado se archiva en `CHANGELOG.md`.
- Cada cambio de estado actualiza la fecha de la cabecera.
- Campo `cuota_antigravity_usada` se actualiza tras cada uso de Nivel 3 (ver `quota_tracker.py`).