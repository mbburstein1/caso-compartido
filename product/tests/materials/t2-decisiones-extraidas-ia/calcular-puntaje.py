#!/usr/bin/env python3
"""T2 · decisiones-extraidas-ia — calcula las métricas y el resultado contra el umbral.

Uso: python3 calcular-puntaje.py planilla-puntaje.csv

Umbral fijado en product/tests/2026-10-06-2100-decisiones-que-no-sobreviven-la-reunion.md (T2).
No se cambia aquí.
"""
import csv
import sys
from statistics import median

N_RESERVADAS = 8
DT = {"decision", "tarea"}


def pct(n, d):
    return None if d == 0 else n / d


def fmt(x):
    return "—" if x is None else f"{x:.0%}"


def correcciones(r):
    ts, tc = r["tipo_sistema"], r["tipo_clave"]
    if tc == "excluido":
        return 0
    if not r["id_item_sistema"]:  # fila «agregar»
        return 1 if tc in DT else 0
    if ts in DT:
        if tc not in DT:  # quitar: era idea o no está en la clave
            return 1
        if ts != tc:  # retipificar decisión <-> tarea
            return 1
        mal_resp = r["responsable_sistema"] != r["responsable_clave"]
        mal_fecha = r["fecha_correcta"] == "no"
        return 1 if (mal_resp or mal_fecha) else 0
    if ts == "idea" and tc in DT:  # retipificar: era decisión o tarea
        return 1
    return 0


def metricas(rows):
    filas = [r for r in rows if r["tipo_clave"] != "excluido"]
    marc_dec = [r for r in filas if r["tipo_sistema"] == "decision"]
    prec_n = sum(r["tipo_clave"] == "decision" for r in marc_dec)
    dec_clave = [r for r in filas if r["tipo_clave"] == "decision"]
    encontradas = [r for r in dec_clave if r["tipo_sistema"] == "decision"]
    resp_ok = sum(r["responsable_sistema"] == r["responsable_clave"] for r in encontradas)
    por_tr = {}
    for r in rows:
        por_tr.setdefault(r["id_transcripcion"], 0)
        por_tr[r["id_transcripcion"]] += correcciones(r)
    return {
        "precision": pct(prec_n, len(marc_dec)),
        "precision_txt": f"{prec_n}/{len(marc_dec)}",
        "cobertura": pct(len(encontradas), len(dec_clave)),
        "cobertura_txt": f"{len(encontradas)}/{len(dec_clave)}",
        "responsable": pct(resp_ok, len(encontradas)),
        "responsable_txt": f"{resp_ok}/{len(encontradas)}",
        "correcciones": por_tr,
        "mediana_corr": median(por_tr.values()) if por_tr else None,
    }


def imprimir(nombre, m):
    print(f"\n== {nombre} ==")
    print(f"  Transcripciones:        {len(m['correcciones'])}")
    print(f"  Precisión de decisión:  {fmt(m['precision'])} ({m['precision_txt']})")
    print(f"  Cobertura de decisión:  {fmt(m['cobertura'])} ({m['cobertura_txt']})")
    print(f"  Responsable correcto:   {fmt(m['responsable'])} ({m['responsable_txt']})")
    print(f"  Correcciones por reunión: {m['correcciones']}  → mediana {m['mediana_corr']}")


def main(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if "|" not in r["conjunto"]]  # salta la fila ejemplo
    for r in rows:
        for k in r:
            r[k] = (r[k] or "").strip()

    def sel(conj, sis):
        return [r for r in rows if r["conjunto"] == conj and r["sistema"] == sis]

    ia = metricas(sel("reservada", "ia"))
    imprimir("IA · 8 reservadas (esto es lo que se lee)", ia)
    cop_rows = sel("reservada", "copilot")
    cop = metricas(cop_rows) if cop_rows else None
    if cop:
        imprimir("Copilot · mismas reservadas (comparación)", cop)
    aj = sel("ajuste", "ia")
    if aj:
        imprimir("IA · 4 de ajuste (diagnóstico, no cuenta)", metricas(aj))

    print("\n== Resultado ==")
    n = len(ia["correcciones"])
    if n != N_RESERVADAS:
        print(f"  No se lee: hay {n} transcripciones reservadas y el diseño pide {N_RESERVADAS}. "
              "Volver a /design-solution-tests.")
        return
    if None in (ia["precision"], ia["cobertura"], ia["responsable"]):
        print("  No se lee: alguna métrica no tiene denominador (no hay decisiones). Revisar la clave.")
        return
    p, c, rsp, med = ia["precision"], ia["cobertura"], ia["responsable"], ia["mediana_corr"]
    if cop and cop["precision"] is not None and not p > cop["precision"]:
        print(f"  FALLA (comparación): la precisión de la IA ({fmt(p)}) no supera la de Copilot "
              f"({fmt(cop['precision'])}). → discard")
    elif p < 0.75 or c < 0.60:
        print("  FALLA: precisión < 75% o cobertura < 60%. → discard")
    elif p >= 0.90 and c >= 0.80 and rsp >= 0.80 and med <= 2:
        print("  PASA: precisión ≥ 90%, cobertura ≥ 80%, responsable ≥ 80%, mediana de correcciones ≤ 2. → continue")
    else:
        solo_resp = p >= 0.90 and c >= 0.80 and med <= 2 and rsp < 0.80
        extra = " (pasa en todo menos responsable correcto)" if solo_resp else ""
        print(f"  ENTRE UMBRALES{extra}. → change: ajustar el prompt y volver a probar sobre un set reservado NUEVO.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
