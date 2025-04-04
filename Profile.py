import streamlit as st
import os

st.set_page_config(page_title="Mon App", page_icon="favicon.png")
    

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
