import streamlit as st
from data import CHAPITRES_ECRIT, CHAPITRES_ORAL


def initialiser_progression():
    if "progression" not in st.session_state:
        tous_les_chapitres = list(CHAPITRES_ECRIT.keys()) + list(CHAPITRES_ORAL.keys())

        progression = {chapitre: False for chapitre in tous_les_chapitres}
        progression["quiz_faits"] = 0
        progression["quiz_reussis"] = 0

        st.session_state.progression = progression


def calculer_stats_chapitres(liste_chapitres):
    progression = st.session_state.progression
    faits = sum(1 for chapitre in liste_chapitres if progression.get(chapitre, False))
    total = len(liste_chapitres)
    ratio = faits / total if total > 0 else 0
    return faits, total, ratio


def trouver_prochain_chapitre():
    progression = st.session_state.progression

    tous_les_chapitres = list(CHAPITRES_ECRIT.keys()) + list(CHAPITRES_ORAL.keys())

    for chapitre in tous_les_chapitres:
        if not progression.get(chapitre, False):
            return chapitre

    return None


def afficher_liste_chapitres(titre, chapitres_dict):
    progression = st.session_state.progression

    st.markdown(f"### {titre}")

    for chapitre in chapitres_dict.keys():
        fait = progression.get(chapitre, False)

        if fait:
            st.markdown(
                f"""
                <div style="
                    background-color: rgba(34, 197, 94, 0.12);
                    border: 1px solid rgba(34, 197, 94, 0.35);
                    border-radius: 12px;
                    padding: 14px 16px;
                    margin-bottom: 10px;
                ">
                    <span style="font-size: 18px;">✅</span>
                    <span style="font-weight: 600; margin-left: 8px;">{chapitre}</span>
                    <span style="color: #86efac; margin-left: 8px;">— Terminé</span>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="
                    background-color: rgba(255, 255, 255, 0.03);
                    border: 1px solid rgba(255, 255, 255, 0.08);
                    border-radius: 12px;
                    padding: 14px 16px;
                    margin-bottom: 10px;
                ">
                    <span style="font-size: 18px;">⬜</span>
                    <span style="font-weight: 600; margin-left: 8px;">{chapitre}</span>
                    <span style="color: #cbd5e1; margin-left: 8px;">— Pas encore travaillé</span>
                </div>
                """,
                unsafe_allow_html=True
            )


def afficher_accueil():
    initialiser_progression()

    progression = st.session_state.progression

    chapitres_ecrit = list(CHAPITRES_ECRIT.keys())
    chapitres_oral = list(CHAPITRES_ORAL.keys())
    tous_les_chapitres = chapitres_ecrit + chapitres_oral

    faits_total, total_total, ratio_total = calculer_stats_chapitres(tous_les_chapitres)
    faits_ecrit, total_ecrit, ratio_ecrit = calculer_stats_chapitres(chapitres_ecrit)
    faits_oral, total_oral, ratio_oral = calculer_stats_chapitres(chapitres_oral)

    quiz_faits = progression.get("quiz_faits", 0)
    quiz_reussis = progression.get("quiz_reussis", 0)
    score_quiz = int((quiz_reussis / quiz_faits) * 100) if quiz_faits > 0 else 0

    prochain_chapitre = trouver_prochain_chapitre()

    st.title("🏠 Accueil")
    st.caption("Bienvenue sur ton espace de révision.")

    st.markdown("## Progression générale")
    st.progress(ratio_total)
    st.write(f"**{faits_total} chapitre(s) travaillé(s) sur {total_total}**")

    st.markdown("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Chapitres terminés", faits_total)

    with col2:
        st.metric("Progression totale", f"{int(ratio_total * 100)} %")

    with col3:
        st.metric("Partie écrite", f"{faits_ecrit}/{total_ecrit}")

    with col4:
        st.metric("Partie orale", f"{faits_oral}/{total_oral}")

    st.markdown("---")

    col_gauche, col_droite = st.columns([1.5, 1])

    with col_gauche:
        st.markdown("### Reprendre la révision")

        if prochain_chapitre:
            st.info(f"Prochain chapitre conseillé : **{prochain_chapitre}**")
        else:
            st.success("Bravo, tous les chapitres sont validés 🎉")

        col_btn1, col_btn2 = st.columns(2)

        with col_btn1:
            if st.button("📚 Aller aux cours", use_container_width=True):
                st.session_state.page = "cours"
                if prochain_chapitre:
                    st.session_state.theme_selectionne = prochain_chapitre
                st.rerun()

        with col_btn2:
            if st.button("🧠 Aller aux quiz", use_container_width=True):
                st.session_state.page = "entrainement"
                st.rerun()

    with col_droite:
        st.markdown("### Quiz")
        st.metric("Questions faites", quiz_faits)
        st.metric("Réussite", f"{score_quiz} %")

    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("## ✍️ Partie écrite")
        st.progress(ratio_ecrit)
        st.write(f"{faits_ecrit} chapitre(s) sur {total_ecrit}")
        afficher_liste_chapitres("Chapitres écrits", CHAPITRES_ECRIT)

    with col_b:
        st.markdown("## 🎤 Partie orale")
        st.progress(ratio_oral)
        st.write(f"{faits_oral} chapitre(s) sur {total_oral}")
        afficher_liste_chapitres("Chapitres oraux", CHAPITRES_ORAL)