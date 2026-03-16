import streamlit as st
import copy

from data import PROGRESSION_INIT
from accueil import afficher_accueil
from cours import afficher_cours
from entrainement import afficher_entrainement

st.set_page_config(page_title="Révision certification", layout="wide")

if "progression" not in st.session_state:
    st.session_state.progression = copy.deepcopy(PROGRESSION_INIT)

if "page" not in st.session_state:
    st.session_state.page = "Accueil"

menu = st.sidebar.radio(
    "Navigation",
    ["Accueil", "Cours", "Entraînement"],
    index=["Accueil","Cours","Entraînement"].index(st.session_state.page)
)

st.session_state.page = menu

if menu == "Accueil":
    afficher_accueil()

elif menu == "Cours":
    afficher_cours()

elif menu == "Entraînement":
    afficher_entrainement()