CHAPITRES_ECRIT = {
    "Analyse fonctionnelle": "analyse_fonctionnelle.md",
    "Modélisation des données (MCD / UML)": "uml.md",
    "SQL": "sql.md",
    "Algorithme / pseudo-code": "algorithme.md",
    "Modélisation des processus": "processus.md",
    "Architecture SI / API": "architecture_si.md",
    "Conduite de projet": "conduite_projet.md",
}

CHAPITRES_ORAL = {
    "Technique de l'analyse": "technique_analyse.md",
    "Logiciel": "logiciel.md",
    "Matériel": "materiel.md",
    "Centre de traitement de l'information": "centre_traitement.md",
    "Environnement juridique et administratif": "environnement_juridique.md",
}
QUIZ_QUESTIONS = [
    {
        "theme": "SQL",
        "question": "Que signifie SQL ?",
        "options": [
            "Structured Query Language",
            "Simple Query Logic",
            "System Quality Language"
        ],
        "reponse": "Structured Query Language",
        "explication": "SQL est le langage standard pour interroger et manipuler des bases de données relationnelles."
    },
    {
        "theme": "Modélisation des données",
        "question": "À quoi sert un MCD ?",
        "options": [
            "À modéliser les données",
            "À coder une interface",
            "À tester une API"
        ],
        "reponse": "À modéliser les données",
        "explication": "Le MCD permet de représenter les entités, attributs et relations d’un système."
    }
]
PROGRESSION_INIT = {
    "quiz_faits": 0,
    "bonnes_reponses": 0,
    "mauvaises_reponses": 0,
    "themes": {
        "Analyse fonctionnelle": {"bonnes": 0, "mauvaises": 0},
        "Modélisation des données": {"bonnes": 0, "mauvaises": 0},
        "SQL": {"bonnes": 0, "mauvaises": 0},
        "Algorithme": {"bonnes": 0, "mauvaises": 0},
        "Architecture SI / API": {"bonnes": 0, "mauvaises": 0},
        "Conduite de projet": {"bonnes": 0, "mauvaises": 0},
        "Technique de l’analyse": {"bonnes": 0, "mauvaises": 0},
        "Logiciel": {"bonnes": 0, "mauvaises": 0},
        "Matériel": {"bonnes": 0, "mauvaises": 0},
        "Centre de traitement de l'information": {"bonnes": 0, "mauvaises": 0},
        "Environnement juridique et administratif": {"bonnes": 0, "mauvaises": 0},
    }
}