# Pipeline de control de presión arterial (Leonori-Saldías)

Programa en Python (solo biblioteca estándar) que lee mediciones de presión arterial en CSV o JSON, descarta los registros con errores dejando constancia del motivo y genera un resumen por grupo del estudio.

Flujo: leer → validar → limpiar → analizar → comunicar el resultado.

## Estructura
```text
├── data/        datos de entrada y su descripción
├── src/
│   ├── fuentes.py    FuenteDatos, FuenteCSV, FuenteJSON
│   ├── modelo.py     clase Paciente
│   ├── pipeline.py   validación, limpieza, reporte y guardado
│   └── main.py       punto de entrada
└── tests/
    └── test_pipeline.py
```

## Requisitos
Python 3.10 o superior. No hay dependencias externas.

## Uso
Desde la raíz del repositorio:
```bash
python src/main.py data/mediciones.csv
```
Genera la carpeta `outputs/` con:
- `reporte.csv`: cantidad, presión sistólica media y proporción de hipertensos por grupo;
- `rechazos.csv`: fila, código y motivo de cada registro descartado.

## Pruebas
```bash
python tests/test_pipeline.py
```
Si todo es correcto se imprime `Todas las pruebas pasaron.`

## Decisiones
- Un registro con varios problemas se rechaza con todos los motivos, separados por `;`.
- Ante un código duplicado se conserva la primera aparición.
- El umbral de hipertensión (140 mmHg) es un criterio didáctico simplificado y no un diagnóstico clínico.

## Integrantes
- Francisco Leonori
- Martina Saldías
