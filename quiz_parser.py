import re

def extraire_quiz_markdown(contenu_markdown):
    pattern = r"\[QUIZ\](.*?)\[/QUIZ\]"
    blocs = re.findall(pattern, contenu_markdown, re.DOTALL)

    quiz_list = []

    for bloc in blocs:
        question_match = re.search(r"question:\s*(.*)", bloc)
        answer_match = re.search(r"answer:\s*(.*)", bloc)
        explanation_match = re.search(r"explanation:\s*(.*)", bloc)

        options_match = re.search(r"options:\s*(.*?)(answer:|explanation:)", bloc, re.DOTALL)

        if not question_match or not answer_match or not options_match:
            continue

        question = question_match.group(1).strip()
        answer = answer_match.group(1).strip()

        explanation = ""
        if explanation_match:
            explanation = explanation_match.group(1).strip()

        options_brutes = options_match.group(1).strip().splitlines()
        options = []

        for ligne in options_brutes:
            ligne = ligne.strip()
            if ligne.startswith("- "):
                options.append(ligne[2:].strip())

        quiz_list.append({
            "question": question,
            "options": options,
            "reponse": answer,
            "explication": explanation
        })

    return quiz_list