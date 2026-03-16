import streamlit as st
import os
def lire_cours(fichier):
    with open(f"cours/{fichier}", "r") as f:
        contenu = f.read()
    st.markdown(contenu)
def afficher_cours():
    fichiers = [f for f in os.listdir("cours") if f.endswith(".md")]
    noms = [f.replace(".md", "").replace("_", " ").title() for f in fichiers]
    choix = st.selectbox("Choisis un cours", noms)
    index = noms.index(choix)
    fichier = fichiers[index]
    lire_cours(fichier)