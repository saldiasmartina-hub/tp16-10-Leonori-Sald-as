import csv
import re
import statistics

from modelo import Paciente

PATRON_CODIGO = re.compile(r"PAC-\d{3}")

RANGOS = {
    "edad": (18, 100),
    "imc": (12, 60),
    "presion_sistolica": (70, 250),
}
GRUPOS_VALIDOS = {"A", "B"}


def convertir_numero(valor):
    if valor is None or str(valor).strip() == "":
        return None
    return float(valor)


def validar_registro(registro):
    motivos = []

    if not PATRON_CODIGO.fullmatch(str(registro.get("codigo", ""))):
        motivos.append("código con formato inválido")

    for campo, (minimo, maximo) in RANGOS.items():
        try:
            numero = convertir_numero(registro.get(campo))
        except ValueError:
            motivos.append(f"{campo} no numérico")
            continue
        if numero is None:
            motivos.append(f"{campo} faltante")
        elif not (minimo <= numero <= maximo):
            motivos.append(f"{campo} fuera de rango")

    if registro.get("grupo") not in GRUPOS_VALIDOS:
        motivos.append("grupo inválido")

    return motivos


def limpiar(registros):
    validos = []
    rechazos = []
    codigos_aceptados = set()

    for fila, registro in enumerate(registros, start=1):
        motivos = validar_registro(registro)

        if registro.get("codigo") in codigos_aceptados:
            motivos.append("código duplicado")

        if motivos:
            rechazos.append({
                "fila": fila,
                "codigo": registro.get("codigo"),
                "motivo": "; ".join(motivos),
            })
        else:
            codigos_aceptados.add(registro["codigo"])
            validos.append(Paciente(
                registro["codigo"],
                convertir_numero(registro["edad"]),
                convertir_numero(registro["imc"]),
                convertir_numero(registro["presion_sistolica"]),
                registro["grupo"],
            ))

    return validos, rechazos


def generar_reporte(pacientes):
    reporte = []
    for grupo in sorted(GRUPOS_VALIDOS):
        del_grupo = [p for p in pacientes if p.grupo == grupo]
        cantidad = len(del_grupo)

        if cantidad == 0:
            presion_media = None
            proporcion = None
        else:
            presion_media = round(statistics.mean(p.presion for p in del_grupo), 2)
            hipertensos = sum(1 for p in del_grupo if p.es_hipertenso())
            proporcion = round(hipertensos / cantidad, 3)

        reporte.append({
            "grupo": grupo,
            "cantidad": cantidad,
            "presion_media": presion_media,
            "proporcion_hipertensos": proporcion,
        })
    return reporte


def guardar_csv(filas, ruta):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)
