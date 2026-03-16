import re
import os
import streamlit as st
from data import CHAPITRES_ECRIT, CHAPITRES_ORAL


def initialiser_progression():
    if "progression" not in st.session_state:
        tous_les_chapitres = list(CHAPITRES_ECRIT.keys()) + list(CHAPITRES_ORAL.keys())

        progression = {chapitre: False for chapitre in tous_les_chapitres}
        progression["quiz_faits"] = 0
        progression["quiz_reussis"] = 0

        st.session_state.progression = progression


def lire_contenu_cours(fichier):
    chemin = f"cours/{fichier}"

    if os.path.exists(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            return f.read()
    return None


def nettoyer_contenu(contenu):
    return re.sub(r"\[QUIZ\](.*?)\[/QUIZ\]", "", contenu, flags=re.DOTALL).strip()


def decouper_sections_markdown(contenu):
    """
    Découpe le markdown selon les titres de niveau 2 : ## Titre
    Retourne :
    - intro : contenu avant le premier ##
    - sections : liste de tuples (titre, contenu)
    """
    pattern = r"(?m)^##\s+(.*)$"
    matches = list(re.finditer(pattern, contenu))

    if not matches:
        return contenu, []

    intro = contenu[:matches[0].start()].strip()
    sections = []

    for i, match in enumerate(matches):
        titre = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(contenu)
        bloc = contenu[start:end].strip()
        sections.append((titre, bloc))

    return intro, sections


def afficher_contenu_cours(fichier):
    contenu = lire_contenu_cours(fichier)

    if not contenu:
        st.warning("Cours en cours de rédaction...")
        return

    contenu = nettoyer_contenu(contenu)
    intro, sections = decouper_sections_markdown(contenu)

    if intro:
        with st.expander("📌 Introduction", expanded=True):
            st.markdown(intro)

    if sections:
        titres = [titre for titre, _ in sections]

        mode_affichage = st.radio(
            "Mode de lecture",
            ["Vue section par section", "Vue complète"],
            horizontal=True,
            key=f"mode_affichage_{fichier}"
        )

        if mode_affichage == "Vue section par section":
            section_choisie = st.selectbox(
                "Aller à une partie",
                titres,
                key=f"section_choisie_{fichier}"
            )

            for titre, bloc in sections:
                if titre == section_choisie:
                    st.markdown(f"## {titre}")
                    st.markdown(bloc)
                    break
        else:
            for titre, bloc in sections:
                with st.expander(f"📖 {titre}", expanded=False):
                    st.markdown(bloc)
    else:
        st.markdown(contenu)


def calculer_progression():
    progression = st.session_state.progression

    # On ne garde que les vrais chapitres (valeurs booléennes)
    chapitres_valides = [valeur for valeur in progression.values() if isinstance(valeur, bool)]

    faits = sum(chapitres_valides)
    total = len(chapitres_valides)
    ratio = faits / total if total > 0 else 0

    return faits, total, ratio


def afficher_cours():
    initialiser_progression()

    st.title("📚 Cours")

    section = st.radio(
        "Choisis une section",
        ["Écrit", "Oral"],
        horizontal=True
    )

    chapitres = CHAPITRES_ECRIT if section == "Écrit" else CHAPITRES_ORAL
    theme = st.selectbox("Choisis un chapitre", list(chapitres.keys()))

    st.session_state.theme_selectionne = theme
    st.session_state.fichier_cours_selectionne = chapitres[theme]

    faits, total, ratio = calculer_progression()

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Ta progression")
        st.progress(ratio)
        st.write(f"{faits} chapitre(s) validé(s) sur {total}")
    with col2:
        st.metric("Progression", f"{int(ratio * 100)} %")

    st.markdown("---")
    st.subheader(theme)
    afficher_contenu_cours(chapitres[theme])

    st.markdown("---")

    deja_valide = st.session_state.progression.get(theme, False)

    if not deja_valide:
        if st.button("✅ Marquer comme révisé"):
            st.session_state.progression[theme] = True
            st.success(f"Le chapitre '{theme}' a été validé.")
            st.rerun()
    else:
        st.success("Chapitre déjà validé.")
        if st.button("↩️ Retirer de la progression"):
            st.session_state.progression[theme] = False
            st.info(f"Le chapitre '{theme}' a été retiré de la progression.")
            st.rerun()

    with st.expander("📋 Voir le récapitulatif de tous les chapitres", expanded=False):
        tous_les_chapitres = list(CHAPITRES_ECRIT.keys()) + list(CHAPITRES_ORAL.keys())

        for chapitre in tous_les_chapitres:
            statut = st.session_state.progression.get(chapitre, False)
            symbole = "✅" if statut else "⬜"
            st.write(f"{symbole} {chapitre}")