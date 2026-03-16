import random
import streamlit as st
from data import QUIZ_QUESTIONS


def initialiser_entrainement():
    if "question_index" not in st.session_state:
        st.session_state.question_index = random.randint(0, len(QUIZ_QUESTIONS) - 1)

    if "score_entrainement" not in st.session_state:
        st.session_state.score_entrainement = 0

    if "nb_questions_entrainement" not in st.session_state:
        st.session_state.nb_questions_entrainement = 0

    if "reponse_validee" not in st.session_state:
        st.session_state.reponse_validee = False

    if "resultat_deja_compte" not in st.session_state:
        st.session_state.resultat_deja_compte = False


def enregistrer_resultat(theme, est_correct):
    st.session_state.progression["quiz_faits"] += 1

    if est_correct:
        st.session_state.progression["bonnes_reponses"] += 1
        st.session_state.progression["themes"][theme]["bonnes"] += 1
    else:
        st.session_state.progression["mauvaises_reponses"] += 1
        st.session_state.progression["themes"][theme]["mauvaises"] += 1


def question_suivante():
    st.session_state.question_index = random.randint(0, len(QUIZ_QUESTIONS) - 1)
    st.session_state.reponse_validee = False
    st.session_state.resultat_deja_compte = False


def afficher_entrainement():
    initialiser_entrainement()

    st.subheader("Mode entraînement concours")

    q = QUIZ_QUESTIONS[st.session_state.question_index]

    st.write(f"**Question :** {q['question']}")

    reponse = st.radio(
        "Choisis une réponse",
        q["options"],
        key="reponse_entrainement",
        index=None
    )

    if not st.session_state.reponse_validee:
        if st.button("Valider ma réponse"):
            if reponse is None:
                st.warning("Choisis une réponse avant de valider.")
            else:
                st.session_state.reponse_validee = True
                st.session_state.nb_questions_entrainement += 1

                est_correct = reponse == q["reponse"]

                if est_correct:
                    st.session_state.score_entrainement += 1

                if not st.session_state.resultat_deja_compte:
                    enregistrer_resultat(q["theme"], est_correct)
                    st.session_state.resultat_deja_compte = True

                st.rerun()

    else:
        if reponse == q["reponse"]:
            st.success("Bonne réponse.")
        else:
            st.error("Mauvaise réponse.")
            st.write(f"**Bonne réponse :** {q['reponse']}")

        st.info(q["explication"])

        st.markdown("---")
        st.write(
            f"**Score actuel :** {st.session_state.score_entrainement} / {st.session_state.nb_questions_entrainement}"
        )

        if st.button("Question suivante"):
            question_suivante()
            st.rerun()

    st.markdown("---")
    if st.button("Réinitialiser l'entraînement"):
        st.session_state.question_index = random.randint(0, len(QUIZ_QUESTIONS) - 1)
        st.session_state.score_entrainement = 0
        st.session_state.nb_questions_entrainement = 0
        st.session_state.reponse_validee = False
        st.session_state.resultat_deja_compte = False
        st.rerun()