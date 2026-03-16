import streamlit as st
def afficher_cours():
    st.header("Cours")
    st.write("Choisis un thème :")
    col1, col2, col3 = st.columns(3)
    if "theme_selectionne" not in st.session_state:
        st.session_state.theme_selectionne = "Système d'information"
    with col1:
        if st.button("Système d'information"):
            st.session_state.theme_selectionne = "Système d'information"
    with col2:
        if st.button("SQL"):
            st.session_state.theme_selectionne = "SQL"
    with col3:
        if st.button("Architecture"):
            st.session_state.theme_selectionne = "Architecture"
    st.divider()
    theme = st.session_state.theme_selectionne
    if theme == "Système d'information":
        st.subheader("Système d'information")
        with st.expander("Définition d'un système d'information"):
            st.write("""
Un système d'information est un ensemble organisé de ressources
(matériel, logiciel, données, procédures et personnes)
permettant de collecter, stocker, traiter et diffuser l'information.
""")
            with st.expander("Composants d'un SI"):
                st.write("""
Les composants d'un système d'information sont :
- le matériel
- les logiciels
- les données
- les procédures
- les utilisateurs
""")
            with st.expander("Objectif d'un SI"):
                st.write("""
Le système d'information permet de :
- soutenir les activités de l'entreprise
- faciliter la prise de décision
- améliorer la communication
""")
    elif theme == "SQL":
        st.subheader("SQL")
        st.write("Contenu du cours SQL")
    elif theme == "Architecture":
        st.subheader("Architecture")
        st.write("Contenu du cours Architecture")