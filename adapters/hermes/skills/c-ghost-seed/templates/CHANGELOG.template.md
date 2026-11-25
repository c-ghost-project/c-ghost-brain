# CHANGELOG.md — Histórico de hitos

Proyecto: {{PROJECT_NAME}}
Organización: {{ORG}}
Inicio: {{DATE}}

Aquí se archiva lo que sale de `STATUS.md` cuando un hito se cierra. El histórico no se poda. Las fechas van en formato ISO `AAAA-MM-DD`.

## Formato de entrada

```text
## [AAAA-MM-DD] — Título del hito

- Pilar:
- Objetivo:
- Cambios:
- Decisión:
- Verificación:
- Rollback:
```

## Hitos

## [{{DATE}}] — Arranque del proyecto

- Pilar: Core Domain
- Objetivo: inicializar el cerebro C://GHOST v2.0.
- Cambios: `.hermes.md`, `AGENTS.md`, `STATUS.md`, `IDEAS.md`, `CHANGELOG.md`, skill `01-core-domain` y whitepaper.
- Decisión: adoptar la pirámide de 4 niveles y la exclusividad de escritura.
- Verificación: estructura creada y archivos legibles.
- Rollback: eliminar los archivos generados por la semilla.

## Convenciones

- Un hito por bloque, del más reciente al más antiguo dentro de "Hitos".
- Nunca se edita un hito cerrado; si cambia una decisión, se añade uno nuevo que la sustituye.
- Cada entrada debe responder: qué cambió, por qué y cómo se comprobó.
