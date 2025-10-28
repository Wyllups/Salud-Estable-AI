# -*- coding: utf-8 -*-
"""
SaludEstable AI – versión avanzada FULL AUTO
Detección automática de columnas y cálculo inteligente de riesgo financiero (EPS / IPS)
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import re
from io import BytesIO
import warnings
warnings.filterwarnings("ignore")

# === CONFIGURACIÓN DE INTERFAZ ===
st.set_page_config(page_title="SaludEstable AI", layout="wide", page_icon="💊")
st.markdown("<h1 style='text-align:center;color:#1f3a60;'>💊 SaludEstable AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#555;'>Evaluación y predicción automatizada del riesgo financiero en entidades de salud (EPS / IPS)</p>", unsafe_allow_html=True)
st.markdown("---")

# === PARÁMETROS ===
FACTORES_RIESGO = {
    "LIQUIDEZ_CORRIENTE": {"peso": 0.25, "inverso": False},
    "ENDEUDAMIENTO_TOTAL": {"peso": 0.25, "inverso": True},
    "MARGEN_NETO": {"peso": 0.20, "inverso": False},
    "ROA": {"peso": 0.15, "inverso": False},
    "ROTACION_ACTIVOS": {"peso": 0.15, "inverso": False},
}

UMBRAL_ALTO_RIESGO = 45
UMBRAL_BAJO_RIESGO = 60

# === FUNCIONES AUXILIARES ===
def limpiar(texto):
    texto = str(texto).upper().strip()
    texto = re.sub(r"\s+", " ", texto)
    return texto

def buscar_columna(df, nombre_objetivo):
    """
    Busca una columna en df que coincida o se parezca al nombre objetivo.
    Ignora mayúsculas, tildes, signos y espacios.
    """
    if not isinstance(nombre_objetivo, str): return None
    nombre_objetivo = re.sub(r"[^a-z0-9]", "", nombre_objetivo.lower())
    for col in df.columns:
        col_clean = re.sub(r"[^a-z0-9]", "", str(col).lower())
        if nombre_objetivo in col_clean or col_clean in nombre_objetivo:
            return col
    return None

def normalizar_por_percentil(valor, serie, inverso=False):
    if pd.isna(valor): return 50
    p = np.sum(serie <= valor) / len(serie) * 100
    return 100 - p if inverso else p

def clasificar_riesgo(valor):
    if valor >= UMBRAL_BAJO_RIESGO:
        return "BAJO RIESGO (Estable)"
    elif valor >= UMBRAL_ALTO_RIESGO:
        return "RIESGO MEDIO (Vigilancia)"
    else:
        return "ALTO RIESGO (Crítico)"

def predecir_riesgo(liquidez, endeudamiento, margen):
    score = (liquidez + margen - endeudamiento)
    if score > 0.05:
        return "📈 Mejora sostenida"
    elif score < -0.05:
        return "⚠️ Riesgo Financiero"
    else:
        return "➖ Estable"

def tipo_entidad(nombre):
    if "EPS" in nombre:
        return "EPS"
    elif "IPS" in nombre:
        return "IPS"
    else:
        return "OTRA"

# === CARGA DE DATOS ===
st.markdown("### 📂 Cargar archivos Excel (.xlsx)")
archivos = st.file_uploader("Sube uno o varios archivos contables", type=["xlsx"], accept_multiple_files=True)

if archivos:
    dfs = []
    for archivo in archivos:
        df = pd.read_excel(archivo)
        df["Fuente"] = archivo.name
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)
    st.success(f"✅ {len(archivos)} archivo(s) cargado(s) correctamente.")

    # === DETECTAR COLUMNAS PRINCIPALES ===
    col_entidad = buscar_columna(df, "entidad") or buscar_columna(df, "razon social") or buscar_columna(df, "eps")
    col_denom = buscar_columna(df, "denominacion")
    col_valor = buscar_columna(df, "valor")

    if not all([col_entidad, col_denom, col_valor]):
        st.error("❌ No se pudieron detectar las columnas 'entidad', 'denominacion' o 'valor'. Verifica el archivo.")
    else:
        st.info(f"✅ Columnas detectadas: Entidad → {col_entidad}, Denominación → {col_denom}, Valor → {col_valor}")

        df[col_entidad] = df[col_entidad].apply(limpiar)
        df[col_denom] = df[col_denom].apply(limpiar)
        df["Tipo_Entidad"] = df[col_entidad].apply(tipo_entidad)

        # === CÁLCULO DE INDICADORES POR ENTIDAD ===
        indicadores = []
        for entidad, grupo in df.groupby(col_entidad):
            valores = grupo.set_index(col_denom)[col_valor].to_dict()

            def buscar_valor(keyword):
                return sum(v for k, v in valores.items() if keyword in k)

            ingresos = buscar_valor("INGRESO")
            costos = buscar_valor("COSTO")
            gastos = buscar_valor("GASTO")
            activos = buscar_valor("ACTIVO")
            pasivos = buscar_valor("PASIVO")
            efectivo = buscar_valor("EFECTIVO")
            beneficios = buscar_valor("RESULTADO") + buscar_valor("BENEFICIO")

            activos, pasivos, ingresos = max(activos, 1), max(pasivos, 1), max(ingresos, 1)

            liquidez = (efectivo + activos*0.1) / pasivos
            endeudamiento = pasivos / activos
            margen = (ingresos - costos - gastos) / ingresos
            roa = beneficios / activos
            rotacion = ingresos / activos

            indicadores.append({
                "Entidad": entidad,
                "Tipo_Entidad": tipo_entidad(entidad),
                "Liquidez Corriente": liquidez,
                "Endeudamiento Total": endeudamiento,
                "Margen Neto": margen,
                "ROA": roa,
                "Rotación Activos": rotacion,
                "Ingresos": ingresos,
                "Activos": activos,
                "Pasivos": pasivos
            })

        df_eval = pd.DataFrame(indicadores)

        # === NORMALIZACIÓN AUTOMÁTICA ===
        for ind, cfg in FACTORES_RIESGO.items():
            col_real = buscar_columna(df_eval, ind)
            if col_real:
                df_eval[ind + "_PERC"] = df_eval[col_real].apply(
                    lambda x: normalizar_por_percentil(x, df_eval[col_real], inverso=cfg["inverso"])
                )
            else:
                df_eval[ind + "_PERC"] = 50

        # === CÁLCULO GLOBAL ===
        df_eval["RIESGO_GLOBAL"] = sum(
            df_eval[ind + "_PERC"] * cfg["peso"] for ind, cfg in FACTORES_RIESGO.items()
        )
        df_eval["CATEGORIA_RIESGO"] = df_eval["RIESGO_GLOBAL"].apply(clasificar_riesgo)
        df_eval["PREDICCION"] = df_eval.apply(
            lambda x: predecir_riesgo(
                x.get(buscar_columna(df_eval, "liquidez"), 0),
                x.get(buscar_columna(df_eval, "endeudamiento"), 0),
                x.get(buscar_columna(df_eval, "margen"), 0),
            ),
            axis=1
        )

        # === VISUALIZACIÓN ===
        st.markdown("## 📈 Resumen General")
        col1, col2, col3 = st.columns(3)
        col1.metric("Promedio Riesgo Global", f"{df_eval['RIESGO_GLOBAL'].mean():.2f}")
        col2.metric("Entidades Analizadas", f"{len(df_eval)}")
        col3.metric("EPS / IPS", f"{(df_eval['Tipo_Entidad']=='EPS').sum()} / {(df_eval['Tipo_Entidad']=='IPS').sum()}")

        # === TABLA DETALLADA ===
        st.dataframe(df_eval[[
            "Entidad", "Tipo_Entidad", "Liquidez Corriente", "Endeudamiento Total", "Margen Neto",
            "ROA", "Rotación Activos", "RIESGO_GLOBAL", "CATEGORIA_RIESGO", "PREDICCION"
        ]].sort_values("RIESGO_GLOBAL", ascending=False))

        # === GRAFICO GENERAL ===
        fig = px.bar(
            df_eval.sort_values("RIESGO_GLOBAL"),
            x="RIESGO_GLOBAL", y="Entidad",
            color="CATEGORIA_RIESGO",
            orientation="h",
            color_discrete_map={
                "BAJO RIESGO (Estable)": "green",
                "RIESGO MEDIO (Vigilancia)": "orange",
                "ALTO RIESGO (Crítico)": "red"
            },
            title="Evaluación de riesgo financiero"
        )
        st.plotly_chart(fig, use_container_width=True)

        # === DESCARGA ===
        buffer = BytesIO()
        df_eval.to_excel(buffer, index=False)
        st.download_button(
            "💾 Descargar resultados completos",
            data=buffer.getvalue(),
            file_name="Resultados_SaludEstableAI_Full.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.success("✅ Análisis completado correctamente.")
