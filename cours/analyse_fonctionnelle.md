# Analyse fonctionnelle

## 1. Définition

L’analyse fonctionnelle consiste à **étudier un besoin** et à **décrire ce que le système doit faire**, sans décrire tout de suite comment il sera techniquement réalisé.

Elle permet de faire le lien entre :
- le **besoin métier**
- les **utilisateurs**
- les **règles de gestion**
- les **fonctionnalités attendues**
- la future **solution informatique**

L’objectif principal est donc de répondre à la question :

**“Quelles fonctions le système doit-il rendre pour satisfaire le besoin ?”**

---

## 2. Pourquoi faire une analyse fonctionnelle ?

L’analyse fonctionnelle est indispensable car elle permet de :

- clarifier le besoin réel
- éviter les malentendus entre métier et informatique
- recenser les fonctionnalités attendues
- identifier les contraintes
- préparer la rédaction des spécifications
- sécuriser le développement et les tests

Sans analyse fonctionnelle, on risque de développer une solution techniquement correcte mais **inadaptée au besoin réel**.

---

## 3. Besoin, fonction et solution : bien distinguer

## Le besoin
Le besoin correspond à l’attente exprimée par le métier ou l’usager.

**Exemple :**  
Un service veut pouvoir suivre les demandes déposées par les usagers.

## La fonction
La fonction décrit ce que le système doit permettre de faire pour répondre au besoin.

**Exemple :**  
- enregistrer une demande
- consulter une demande
- modifier le statut d’une demande
- produire un historique

## La solution technique
La solution technique correspond à la manière de réaliser la fonction.

**Exemple :**  
- application web
- base de données relationnelle
- API REST
- notifications automatiques

👉 En analyse fonctionnelle, on se concentre d’abord sur le **besoin** et les **fonctions**, pas sur la technique.

---

## 4. Les acteurs de l’analyse fonctionnelle

Plusieurs acteurs interviennent généralement dans l’analyse fonctionnelle :

### Le métier / maîtrise d’ouvrage (MOA)
Il exprime le besoin, les attentes, les priorités et les règles métier.

### La maîtrise d’œuvre (MOE)
Elle transforme le besoin en solution réalisable et exploitable.

### Les utilisateurs
Ils décrivent les usages réels, les difficultés rencontrées et les attentes concrètes.

### L’analyste
Il recueille, reformule, structure et formalise le besoin.  
Il joue un rôle d’interface entre le métier et l’équipe technique.

---

## 5. Les grandes étapes de l’analyse fonctionnelle

## 5.1 Recueil du besoin

Le recueil du besoin peut se faire par :
- entretiens
- ateliers
- questionnaires
- observation des pratiques
- étude de documents existants

L’objectif est de comprendre :
- qui utilise le système
- dans quel contexte
- pour faire quoi
- selon quelles règles
- avec quelles contraintes

## 5.2 Reformulation du besoin

Le besoin brut exprimé par le métier est souvent imprécis, incomplet ou trop orienté solution.  
L’analyste doit donc le reformuler clairement.

**Exemple de besoin mal formulé :**  
“Il faudrait un bouton pour tout valider plus vite.”

**Reformulation fonctionnelle :**  
“Le système doit permettre à un agent autorisé de valider plusieurs dossiers en une seule opération.”

## 5.3 Identification des fonctions attendues

On recense ensuite les services que doit rendre le système.

Exemples de fonctions :
- authentifier un utilisateur
- saisir des données
- consulter un dossier
- calculer un montant
- éditer un document
- transmettre une information
- archiver une opération

## 5.4 Identification des contraintes

Les contraintes limitent ou encadrent la future solution.

Exemples :
- respect de la réglementation
- confidentialité des données
- délais de traitement
- compatibilité avec un SI existant
- nombre d’utilisateurs
- traçabilité obligatoire

## 5.5 Validation avec le métier

L’analyse fonctionnelle doit être relue et validée avec les parties prenantes pour vérifier que :
- le besoin est bien compris
- les fonctions sont complètes
- les priorités sont cohérentes
- les oublis sont corrigés

---

## 6. Fonctions de service et contraintes

Dans l’analyse fonctionnelle, on distingue souvent :

## Les fonctions de service
Ce sont les services rendus à l’utilisateur ou au métier.

**Exemples :**
- créer une demande
- consulter l’état d’avancement
- notifier une décision
- exporter une liste

## Les contraintes
Ce ne sont pas des services rendus, mais des exigences à respecter.

**Exemples :**
- accès réservé aux agents habilités
- conservation des données pendant 5 ans
- disponibilité du service en journée ouvrée
- journalisation des actions

---

## 7. Le cahier des charges fonctionnel

L’analyse fonctionnelle alimente souvent un **cahier des charges fonctionnel** ou des **spécifications fonctionnelles**.

Ce document décrit notamment :
- le contexte
- les objectifs
- les acteurs
- les fonctionnalités attendues
- les règles de gestion
- les cas d’utilisation
- les contraintes
- les données manipulées
- les priorités éventuelles

Il doit être :
- clair
- structuré
- compréhensible par le métier
- exploitable par la MOE

---

## 8. Les règles de gestion

Les règles de gestion sont essentielles en analyse fonctionnelle.

Elles traduisent les conditions métier à respecter.

**Exemples :**
- une demande ne peut être validée que si toutes les pièces sont présentes
- seul un superviseur peut annuler une validation
- un dossier clos ne peut plus être modifié
- toute modification doit être historisée

Les règles de gestion ne décrivent pas la technique.  
Elles décrivent le **fonctionnement attendu du système du point de vue métier**.

---

## 9. Les cas d’utilisation

Les cas d’utilisation permettent de représenter les interactions entre :
- un **acteur**
- un **système**
- un **objectif**

### Exemple
**Acteur :** agent instructeur  
**Objectif :** enregistrer une demande

### Cas d’utilisation associé
**“Enregistrer une demande”**

### Intérêt
Les cas d’utilisation permettent de :
- identifier les fonctionnalités
- clarifier qui fait quoi
- préparer les scénarios détaillés
- faciliter les échanges métier / informatique

---

## 10. Le scénario fonctionnel

Un scénario fonctionnel décrit le déroulement d’une action.

### Exemple : consulter un dossier

#### Précondition
L’utilisateur est authentifié.

#### Scénario nominal
1. L’utilisateur recherche un dossier.
2. Le système affiche la liste des résultats.
3. L’utilisateur sélectionne un dossier.
4. Le système affiche le détail du dossier.

#### Cas alternatif
Si aucun dossier ne correspond, le système affiche un message d’absence de résultat.

#### Post-condition
Le dossier est consulté, sans modification.

---

## 11. Analyse fonctionnelle et analyse organique : différence

Il faut bien distinguer :

## Analyse fonctionnelle
Elle décrit :
- ce que le système doit faire
- pour qui
- dans quel cadre
- selon quelles règles

## Analyse organique / technique
Elle décrit :
- comment le système sera conçu
- quelles tables seront créées
- quels traitements seront développés
- quelles interfaces seront mises en place

👉 L’analyse fonctionnelle précède logiquement la conception technique.

---

## 12. Exemples de questions à se poser en analyse fonctionnelle

Pour bien analyser un besoin, il faut se poser des questions simples mais précises :

### Sur le contexte
- Quel est le problème à résoudre ?
- Quelle est la finalité du projet ?
- Quel est le périmètre ?

### Sur les utilisateurs
- Qui utilise le système ?
- Quels sont les profils et habilitations ?
- Quels sont les usages réels ?

### Sur les données
- Quelles informations faut-il saisir, consulter, modifier, conserver ?
- Quelles données sont obligatoires ?
- D’où viennent-elles ?

### Sur les traitements
- Quelles actions le système doit-il permettre ?
- Quels calculs ou contrôles faut-il effectuer ?
- Quelles sont les règles de décision ?

### Sur les contraintes
- Quelles obligations réglementaires existent ?
- Y a-t-il des contraintes de délai, sécurité, volumétrie, traçabilité ?
- Existe-t-il des interfaces avec d’autres applications ?

---

## 13. Qualités d’une bonne analyse fonctionnelle

Une bonne analyse fonctionnelle doit être :

### Claire
Le document doit être compréhensible par tous les acteurs.

### Complète
Les besoins majeurs, règles et exceptions doivent être couverts.

### Cohérente
Il ne doit pas y avoir de contradictions entre les différentes parties.

### Vérifiable
On doit pouvoir contrôler que les fonctions demandées ont bien été réalisées.

### Non ambiguë
Une exigence doit être interprétée d’une seule manière.

---

## 14. Erreurs fréquentes à éviter

Voici les erreurs classiques :

- confondre besoin et solution technique
- décrire trop tôt l’architecture
- oublier certains acteurs
- négliger les cas d’erreur
- mal formaliser les règles de gestion
- ne pas faire valider l’analyse par le métier
- écrire des exigences floues comme “simple”, “rapide”, “ergonomique” sans précision

**Exemple flou :**  
“Le système doit être rapide.”

**Exemple plus exploitable :**  
“Le système doit afficher le résultat d’une recherche en moins de 3 secondes dans le cas nominal.”

---

## 15. Exemple complet simplifié

## Contexte
Une administration souhaite améliorer le suivi des demandes déposées par les usagers.

## Besoin
Permettre aux agents de suivre les demandes et aux responsables de visualiser l’avancement.

## Fonctions attendues
- créer une demande
- consulter une demande
- modifier son statut
- affecter un dossier à un agent
- consulter l’historique
- produire un tableau de suivi

## Acteurs
- agent
- superviseur
- administrateur

## Règles de gestion
- toute demande reçoit un identifiant unique
- une demande clôturée ne peut plus être modifiée
- seul un superviseur peut réouvrir une demande
- chaque changement de statut est historisé

## Contraintes
- accès authentifié
- traçabilité des actions
- conservation des données
- compatibilité avec le SI existant

---

## 16. Ce qu’il faut retenir pour l’examen

Pour l’oral ou l’écrit, il faut être capable d’expliquer que l’analyse fonctionnelle :

- part du **besoin**
- décrit les **fonctions attendues**
- identifie les **acteurs**
- formalise les **règles de gestion**
- recense les **contraintes**
- sert de base aux **spécifications**
- précède la **conception technique**

Formule simple à retenir :

**Analyse fonctionnelle = comprendre et formaliser ce que le système doit faire pour répondre au besoin métier.**

---

## 17. Mini fiche de révision

### Mots-clés
- besoin
- fonction
- acteur
- règle de gestion
- contrainte
- cas d’utilisation
- scénario
- cahier des charges fonctionnel
- MOA
- MOE

### Idée centrale
On ne commence pas par coder.  
On commence par **comprendre, cadrer et formaliser le besoin**.

---

## 18. Questions de vérification

1. Quelle est la différence entre un besoin et une solution technique ?
2. Quel est le rôle de l’analyse fonctionnelle dans un projet ?
3. Qu’appelle-t-on règle de gestion ?
4. Pourquoi faut-il identifier les acteurs ?
5. Quelle différence entre analyse fonctionnelle et analyse technique ?
6. À quoi sert un cas d’utilisation ?
7. Pourquoi les contraintes sont-elles importantes ?
8. Quelles sont les qualités d’une bonne analyse fonctionnelle ?

---

[QUIZ]
[
  {
    "question": "Quel est l’objectif principal de l’analyse fonctionnelle ?",
    "options": [
      "Décrire l’architecture réseau du système",
      "Déterminer ce que le système doit faire pour répondre au besoin",
      "Choisir le langage de programmation",
      "Créer directement la base de données"
    ],
    "answer": "Déterminer ce que le système doit faire pour répondre au besoin",
    "explanation": "L’analyse fonctionnelle décrit les fonctions attendues à partir du besoin métier, sans entrer immédiatement dans les choix techniques."
  },
  {
    "question": "Une règle de gestion correspond à :",
    "options": [
      "Une contrainte matérielle",
      "Une instruction de programmation",
      "Une condition métier que le système doit respecter",
      "Un schéma de base de données"
    ],
    "answer": "Une condition métier que le système doit respecter",
    "explanation": "Une règle de gestion traduit une exigence de fonctionnement du point de vue métier."
  },
  {
    "question": "Quelle affirmation distingue correctement analyse fonctionnelle et analyse technique ?",
    "options": [
      "L’analyse fonctionnelle décrit comment coder l’application",
      "L’analyse technique exprime uniquement le besoin des utilisateurs",
      "L’analyse fonctionnelle décrit ce que le système doit faire, l’analyse technique décrit comment le réaliser",
      "Il n’y a pas de différence réelle"
    ],
    "answer": "L’analyse fonctionnelle décrit ce que le système doit faire, l’analyse technique décrit comment le réaliser",
    "explanation": "C’est la distinction fondamentale attendue dans ce type d’épreuve."
  },
  {
    "question": "Parmi les éléments suivants, lequel est une contrainte ?",
    "options": [
      "Consulter un dossier",
      "Créer une demande",
      "Historiser les actions des utilisateurs",
      "Modifier un statut"
    ],
    "answer": "Historiser les actions des utilisateurs",
    "explanation": "La traçabilité est une exigence de contrainte ou d’encadrement du système, alors que les autres propositions sont des fonctions rendues."
  },
  {
    "question": "À quoi sert un cas d’utilisation ?",
    "options": [
      "À décrire les interactions entre un acteur et le système pour atteindre un objectif",
      "À créer automatiquement le code source",
      "À définir la couleur de l’interface",
      "À remplacer les règles de gestion"
    ],
    "answer": "À décrire les interactions entre un acteur et le système pour atteindre un objectif",
    "explanation": "Le cas d’utilisation permet de représenter une fonctionnalité vue du point de vue utilisateur."
  }
]
[/QUIZ]