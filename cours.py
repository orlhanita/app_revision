import streamlit as st
from contenu_cours import COURS
def afficher_cours():
    st.header("Cours")
    categorie = st.radio("Choisis une partie", list(COURS.keys()))
    themes = COURS[categorie]
    theme = st.selectbox("Choisis un thème", list(themes.keys()))
    contenu = themes[theme]
    if isinstance(contenu, dict):
        sous_theme = st.selectbox("Choisis un sous-thème", list(contenu.keys()))
        st.subheader(sous_theme)
        st.write(contenu[sous_theme])
    else:
        st.subheader(theme)
        st.write(contenu)