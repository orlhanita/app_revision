import streamlit as st
def afficher_quiz():
    st.header("Quiz")
    question = st.radio(
        "Python est :",
        [
            "un langage de programmation",
            "un navigateur",
            "un système d'exploitation"
        ]
    )
    if question == "un langage de programmation":
        st.success("Bonne réponse")
    else:
        st.error("Mauvaise réponse")