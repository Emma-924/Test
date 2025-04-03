import streamlit as st
import pandas as pd
import os
import numpy as np
from datetime import datetime

if not os.path.exists("data.csv"):
    df = pd.DataFrame(columns=["Date", "Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)", "Notes"])
    df.to_csv("data.csv", index=False)

st.title("Suivi quotidien")

# Formulaire de saisie
date = st.date_input("Date", value=datetime.today())
glycemie = st.number_input("Glycémie (mg/dL)", min_value=0)
insuline = st.number_input("Insuline (U)", min_value=0)
glucides = st.number_input("Glucides (g)", min_value=0)
activite = st.number_input("Activité physique (min)", min_value=0)
notes = st.text_area("Notes")

if st.button("Enregistrer"):
    data = pd.read_csv("data.csv")
    date_str = date.strftime("%Y-%m-%d")
    data = data[data["Date"] != date_str]
    new_data = pd.DataFrame([{
        "Date": date_str,
        "Glycémie (mg/dL)": glycemie,
        "Insuline (U)": insuline,
        "Glucides (g)": glucides,
        "Activité physique (min)": activite,
        "Notes": notes
    }])
    updated_data = pd.concat([data, new_data])
    updated_data.to_csv("data.csv", index=False)
    st.success("Données enregistrées avec succès !")

st.markdown(
    """
    <style>
    [data-testid="stTabs"] button {
        margin-right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

data = pd.read_csv("data.csv")
onglet1, onglet2, onglet3, onglet4, onglet5, onglet6 = st.tabs(['2025', '2024', '2023', '2022', '2021', '2020'])
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")

with onglet1:
    st.subheader("Historique")
    data_2025 = data[data["Date"].dt.year == 2025].copy()
    data_2025["Date affichée"] = data_2025["Date"].dt.strftime("%A %d %B")
    st.write(data_2025[["Date affichée", "Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)", "Notes"]])
    if not data_2025.empty:
        chart_data = data_2025[["Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)"]]
        chart_data.index = data_2025["Date"]
        st.line_chart(chart_data)

with onglet2:
    st.subheader("Historique")
    data_2024 = data[data["Date"].dt.year == 2024].copy()
    data_2024["Date affichée"] = data_2024["Date"].dt.strftime("%A %d %B")
    st.write(data_2024[["Date affichée", "Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)", "Notes"]])
    if not data_2024.empty:
        chart_data = data_2024[["Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)"]]
        chart_data.index = data_2024["Date"]
        st.line_chart(chart_data)

with onglet3:
    st.subheader("Historique")
    data_2023 = data[data["Date"].dt.year == 2023].copy()
    data_2023["Date affichée"] = data_2023["Date"].dt.strftime("%A %d %B")
    st.write(data_2023[["Date affichée", "Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)", "Notes"]])
    if not data_2023.empty:
        chart_data = data_2023[["Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)"]]
        chart_data.index = data_2023["Date"]
        st.line_chart(chart_data)

with onglet4:
    st.subheader("Historique")
    data_2022 = data[data["Date"].dt.year == 2022].copy()
    data_2022["Date affichée"] = data_2022["Date"].dt.strftime("%A %d %B")
    st.write(data_2022[["Date affichée", "Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)", "Notes"]])
    if not data_2022.empty:
        chart_data = data_2022[["Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)"]]
        chart_data.index = data_2022["Date"]
        st.line_chart(chart_data)

with onglet5:
    st.subheader("Historique")
    data_2021 = data[data["Date"].dt.year == 2021].copy()
    data_2021["Date affichée"] = data_2021["Date"].dt.strftime("%A %d %B")
    st.write(data_2021[["Date affichée", "Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)", "Notes"]])
    if not data_2021.empty:
        chart_data = data_2021[["Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)"]]
        chart_data.index = data_2021["Date"]
        st.line_chart(chart_data)

with onglet6:
    st.subheader("Historique")
    data_2020 = data[data["Date"].dt.year == 2020].copy()
    data_2020["Date affichée"] = data_2020["Date"].dt.strftime("%A %d %B")
    st.write(data_2020[["Date affichée", "Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)", "Notes"]])
    if not data_2020.empty:
        chart_data = data_2020[["Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)"]]
        chart_data.index = data_2020["Date"]
        st.line_chart(chart_data)
