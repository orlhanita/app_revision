import streamlit as st
from cours import lire_contenu_cours
from quiz_parser import extraire_quiz_markdown

def afficher_quiz():
    st.subheader("Quiz automatique")

    fichier = st.session_state.get("fichier_cours_selectionne", None)
    theme = st.session_state.get("theme_selectionne", None)

    if not fichier or not theme:
        st.warning("Va d'abord dans l'onglet Cours et sélectionne un chapitre.")
        return

    contenu = lire_contenu_cours(fichier)

    if not contenu:
        st.warning("Impossible de lire le cours.")
        return

    questions = extraire_quiz_markdown(contenu)

    if not questions:
        st.info("Aucune question trouvée dans ce cours.")
        return

    st.write(f"**Chapitre sélectionné :** {theme}")
    st.write(f"**Nombre de questions détectées :** {len(questions)}")

    if "quiz_reponses" not in st.session_state:
        st.session_state.quiz_reponses = {}

    if "quiz_corrige" not in st.session_state:
        st.session_state.quiz_corrige = False

    for i, q in enumerate(questions):
        st.session_state.quiz_reponses[i] = st.radio(
            q["question"],
            q["options"],
            key=f"quiz_auto_{theme}_{i}",
            index=None
        )

    if st.button("Corriger le quiz"):
        st.session_state.quiz_corrige = True

    if st.session_state.quiz_corrige:
        st.markdown("---")
        st.subheader("Résultats")

        score = 0

        for i, q in enumerate(questions):
            reponse_user = st.session_state.quiz_reponses.get(i)
            bonne_reponse = q["reponse"]

            if reponse_user == bonne_reponse:
                score += 1
                st.success(f"Question {i + 1} : Bonne réponse")
            else:
                st.error(f"Question {i + 1} : Mauvaise réponse")
                st.write(f"**Ta réponse :** {reponse_user}")
                st.write(f"**Bonne réponse :** {bonne_reponse}")

            if q["explication"]:
                st.info(q["explication"])

            st.markdown("---")

        st.subheader(f"Score : {score} / {len(questions)}")