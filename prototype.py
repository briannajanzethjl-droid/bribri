# streamlit_app.py

import streamlit as st
import pandas as pd

def main():
    st.title("Próximas Elecciones Generales en Perú")

    st.markdown("""
    Información actualizada sobre el calendario electoral, fechas importantes y contexto político de las próximas elecciones generales en Perú.
    """)

    # Datos básicos
    st.header("Datos Básicos")
    data_basicos = {
        "Concepto": [
            "Fecha de las elecciones generales (1ª vuelta)",
            "Fecha posible de la segunda vuelta presidencial",
            "Número de diputados a elegir",
            "Número de senadores a elegir",
            "Padrón electoral cierra",
            "Calificativo de desaprobación presidencial reciente"
        ],
        "Valor": [
            "12 de abril de 2026",  # elección general primera vuelta :contentReference[oaicite:0]{index=0}
            "7 de junio de 2026 (si hay balotaje presidencial) :contentReference[oaicite:1]{index=1}",
            "130 diputados :contentReference[oaicite:2]{index=2}",
            "60 senadores :contentReference[oaicite:3]{index=3}",
            "14 de octubre de 2025 :contentReference[oaicite:4]{index=4}",
            "≈ 93% de desaprobación para la Presidenta Dina Boluarte (marzo 2025) :contentReference[oaicite:5]{index=5}"
        ]
    }
    df_basicos = pd.DataFrame(data_basicos)
    st.table(df_basicos)

    # Calendario electoral
    st.header("Calendario Electoral")
    calendario = {
        "Hito": [
            "Límite para solicitar formación de alianzas",
            "Fecha límite de registro de alianzas",
            "Cierre del padrón electoral",
            "Elecciones Primarias internas de los partidos",
            "Selección de candidatos (delegados)",
            "Registro oficial de candidaturas",
            "Periodo de impugnaciones/objeciones",
            "Elecciones Generales — primera vuelta",
            "Segunda vuelta presidencial (si aplica)"
        ],
        "Fecha": [
            "2 de agosto de 2025 :contentReference[oaicite:6]{index=6}",
            "1 de septiembre de 2025 :contentReference[oaicite:7]{index=7}",
            "14 de octubre de 2025 :contentReference[oaicite:8]{index=8}",
            "30 de noviembre de 2025 :contentReference[oaicite:9]{index=9}",
            "7 de diciembre de 2025 :contentReference[oaicite:10]{index=10}",
            "23 de diciembre de 2025 :contentReference[oaicite:11]{index=11}",
            "13 de marzo de 2026 (objeciones) / 14 de marzo de 2026 (registro final) :contentReference[oaicite:12]{index=12}",
            "12 de abril de 2026 :contentReference[oaicite:13]{index=13}",
            "7 de junio de 2026 :contentReference[oaicite:14]{index=14}"
        ]
    }
    df_calendario = pd.DataFrame(calendario)
    st.table(df_calendario)

    # Contexto político
    st.header("Contexto Político")
    st.markdown("""
    - La Presidenta Dina Boluarte ha anunciado que las elecciones generales serán el **12 de abril de 2026**. :contentReference[oaicite:15]{index=15}  
    - Se elegirá Presidente, Vicepresidentes, 130 diputados y 60 senadores. :contentReference[oaicite:16]{index=16}  
    - El padrón electoral cerrará el **14 de octubre de 2025**. :contentReference[oaicite:17]{index=17}  
    - Nivel de desaprobación presidencial muy alto (≈ 93 %) registrado en marzo de 2025. :contentReference[oaicite:18]{index=18}  
    """)

    # Posible sección interactiva (por ejemplo encuestas si las hay)
    st.header("Encuestas o Datos de Opinión")
    st.markdown("Hasta ahora, no hay datos definitivos de encuestas ampliamente aceptadas para los candidatos presidenciales de 2026 que estén consolidados para mostrar aquí. Este espacio puede actualizarse conforme se publiquen nuevas encuestas.")

    # Fuente de datos
    st.header("Fuentes")
    st.markdown("""
    - ANDINA (Agencia Peruana de Noticias)  
    - ONPE (Oficina Nacional de Procesos Electorales)  
    - Reniec  
    - JNE (Jurado Nacional de Elecciones)  
    - Reportes del 2025 de opinión pública y cobertura periodística nacional.  
    """)

if __name__ == "__main__":
    main()
