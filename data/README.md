# Datos de entrada

## Procedencia
Los datos provienen del archivo `EstudioPresionEdad.csv` del TP de Correlación y Regresión: datos **simulados con fines didácticos** de 50 pacientes adultos. Para este trabajo se adaptaron así:
- cada paciente recibe un código con el formato `PAC-001` … `PAC-050`;
- se agregaron **8 registros con errores**, cada uno con un único problema (código mal escrito, duplicado, valor faltante, no numérico o fuera de rango, grupo inválido).

## Archivos
`mediciones.csv` y `mediciones.json` tienen el mismo contenido (58 registros) en dos formatos.
- En el CSV todos los valores se leen como texto y un dato faltante es la cadena vacía.
- En el JSON los números son números y un dato faltante es `null`.

## Campos
| Campo | Tipo | Descripción | Rango válido |
|---|---|---|---|
| `codigo` | texto | `PAC-` seguido de tres dígitos | — |
| `edad` | número | Edad en años | 18 a 100 |
| `imc` | número | Índice de masa corporal (kg/m²) | 12 a 60 |
| `presion_sistolica` | número | Presión sistólica (mmHg) | 70 a 250 |
| `grupo` | texto | `A` (control) o `B` (intervención) | `A`, `B` |

Unidad de análisis: un registro por paciente con una medición.
