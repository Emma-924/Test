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
    if date_str not in data["Date"].astype(str).values:
        new_data = pd.DataFrame([{
            "Date": date,
            "Glycémie (mg/dL)": glycemie,
            "Insuline (U)": insuline,
            "Glucides (g)": glucides,
            "Activité physique (min)": activite,
            "Notes": notes
        }])
        new_data.to_csv("data.csv", mode='a', header=False, index=False)
        st.success("Données enregistrées avec succès !")

# Affichage des données existantes
st.subheader("Historique")
data = pd.read_csv("data.csv")
st.write(data)

if not data.empty:
    chart_data = data[["Glycémie (mg/dL)", "Insuline (U)", "Glucides (g)", "Activité physique (min)"]]
    chart_data.index = pd.to_datetime(data["Date"]).dt.date
    st.line_chart(chart_data)
