import streamlit as st
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="Diabestfreind", page_icon="apple-touch-icon.png")

components.html("""
    <link rel="apple-touch-icon" sizes="512x512" href="apple-touch-icon.png">
""", height=0)

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .st-emotion-cache-z5fcl4 {display: none;}  /* logo Streamlit */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Profile")
sexe = st.radio("Sexe", ["Homme", "Femme", "Autre"])
nom = st.text_input("Nom")
prenom = st.text_input("Prénom ")
dateNaissance = st.date_input("Date de naissance")
poid = st.text_input("Poids")
taille = st.text_input("Taille")
type = st.radio("Type de diabète",["Type 1", "Type 2"])
#st.write(f"Bonjour {x}")
