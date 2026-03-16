import streamlit as st
from cours import afficher_cours
from quiz import afficher_quiz
from exercices import afficher_exercices
st.set_page_config(page_title="App révision", layout="wide")
st.title("App de révision – Analyste développeur")
menu = st.sidebar.radio(
    "Navigation",
    ["Cours", "Quiz", "Exercices"]
)
if menu == "Cours":
    afficher_cours()
elif menu == "Quiz":
    afficher_quiz()
elif menu == "Exercices":
    afficher_exercices() 