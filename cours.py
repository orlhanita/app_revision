import streamlit as st
def lire_cours(fichier):
    with open(f"cours/{fichier}", "r") as f:
        contenu = f.read()
    st.markdown(contenu)
def afficher_cours():
  theme = st.selectbox(
        "Choisis un thème",
        [
            "Analyse fonctionnelle",
            "SQL"
        ]
    )
  if theme == "Analyse fonctionnelle":
        lire_cours("analyse_fonctionnelle.md")
  elif theme == "SQL":
        lire_cours("sql.md")