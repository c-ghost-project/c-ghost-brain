# 🛡️ Política de Seguridad — `C://GHOST Brain`

La seguridad *Zero-Trust* (Protocolos 2 y 7) es un pilar central de este repositorio, especialmente en los hooks que impiden la filtración accidental de secretos (`pre-tool-guard.sh`, `stop-gate.sh`) y en los scripts sembradores (`plant-seed.sh`, `init_c_ghost.py`).

## Versiones con Soporte de Seguridad

| Versión | Estado de Soporte |
| :--- | :---: |
| `v3.0.x` (`main`) | ✅ Soporte activo |
| `v2.1.x` (`adapters/hermes`) | ✅ Soporte activo |
| `v2.0.x` y `v1.0.x` | Archivo histórico (sin parches) |

## Cómo Reportar una Vulnerabilidad

Si descubres un fallo de seguridad —por ejemplo, una forma de evadir el bloqueo de archivos sensibles en `pre-tool-guard.sh`, una inyección de comandos en `plant-seed.sh` o un escape defectuoso en `init_c_ghost.py`— **por favor NO abras un Issue público**:

1. Utiliza la pestaña **Security → Advisories → Report a vulnerability** (*GitHub Private Vulnerability Reporting*) en este repositorio.
2. Alternativamente, envía un reporte privado a **`security@c-ghost.black`** (o el contacto de seguridad vigente del mantenedor) incluyendo:
   * Archivo y línea afectada.
   * Pasos mínimos para reproducirlo.
   * Impacto estimado y sugerencia de mitigación (si la tienes).

## Compromiso de Respuesta
* Acuse de recibo en un máximo de **72 horas**.
* Parche verificado y crédito público en el aviso de seguridad (salvo que prefieras anonimato).
