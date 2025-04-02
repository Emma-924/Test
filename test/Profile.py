import streamlit as st

st.title("Profile")
sexe = st.radio("Sexe", ["Homme", "Femme", "Autre"])
nom = st.text_input("Nom")
prenom = st.text_input("Prénom ")
dateNaissance = st.date_input("Date de naissance")
poid = st.text_input("Poids")
taille = st.text_input("Taille")
type = st.radio("Type de diabète",["Type 1", "Type 2"])
#st.write(f"Bonjour {x}")


