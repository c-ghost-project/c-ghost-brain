# IDEAS.md — Fuga cero de ideas

Proyecto: {{PROJECT_NAME}}
Actualizado: {{DATE}}

Toda idea que no pertenece a la Tarea Activa se anota aquí. No se ejecuta, no se descarta y no se pierde. Una idea registrada es deuda visible, no autorización para trabajar en ella.

## Cómo registrar una idea

1. Una fila por idea, con título corto y accionable.
2. Pilar afectado según `STATUS.md`.
3. Impacto: alto, medio o bajo, medido en valor para el usuario.
4. Dependencia: idea, tarea o decisión que debe existir antes.
5. Estado: nueva, en evaluación, aceptada, descartada o absorbida.
6. Si se acepta, pasa al Backlog de `STATUS.md` y aquí se marca como absorbida.

## Tabla de ideas

| # | Idea | Pilar | Impacto | Dependencia | Estado | Fecha |
|---|------|-------|---------|-------------|--------|-------|
| 1 | Definir métricas de éxito del producto | Core Domain | alto | whitepaper inicial | nueva | {{DATE}} |
| 2 | Automatizar la verificación en cada cambio | Platform | medio | entorno local | nueva | {{DATE}} |
| 3 | Documentar las decisiones de arquitectura | Platform | medio | primera tarea cerrada | nueva | {{DATE}} |

## Criterios de impacto

| Impacto | Significado | Cuándo se atiende |
|---------|-------------|-------------------|
| Alto | desbloquea valor central o elimina un riesgo grave | siguiente ciclo |
| Medio | mejora clara sin urgencia | cuando el pilar esté estable |
| Bajo | deseable, sin dependencias críticas | solo si sobra capacidad |

## Criterios de dependencia

- `ninguna`: puede empezar ya.
- `tarea N`: requiere que la tarea N del Backlog esté cerrada.
- `decisión X`: requiere una decisión registrada en `STATUS.md` o `CHANGELOG.md`.
- `externa`: depende de un tercero, licencia o dato que no controlamos.

## Reglas de este archivo

- Solo el Guardián escribe aquí.
- Las ideas descartadas se marcan, no se borran.
- Una idea aceptada sale de aquí solo cuando entra al Backlog.
