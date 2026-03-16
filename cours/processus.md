# Modélisation des processus (BPMN)

## Introduction

La modélisation des processus permet de représenter de manière graphique les activités et les étapes d’un processus métier.

Un processus décrit une suite d’actions réalisées pour atteindre un objectif.

Exemples :

- traiter une déclaration fiscale
- enregistrer un nouvel utilisateur
- valider une demande administrative

La modélisation permet de :

- comprendre le fonctionnement d’une organisation
- analyser les flux d’information
- améliorer les processus existants

---

## Qu’est-ce qu’un processus métier

Un **processus métier** est un ensemble d’activités organisées dans un ordre précis afin d’atteindre un résultat.

Un processus comprend généralement :

- des **acteurs**
- des **activités**
- des **décisions**
- des **flux d’information**

### Exemple

Processus : traitement d'une déclaration fiscale

1. réception de la déclaration
2. vérification des informations
3. calcul de l'impôt
4. validation du dossier

---

## Le langage BPMN

Le **BPMN (Business Process Model and Notation)** est un standard utilisé pour représenter les processus métier.

Il utilise des symboles graphiques pour décrire les différentes étapes d’un processus.

Les principaux éléments sont :

- les événements
- les activités
- les passerelles
- les flux

BPMN permet de représenter les processus de manière claire et compréhensible.

---

## Les événements

Les **événements** représentent un moment particulier dans le processus.

Ils indiquent le début, la fin ou une étape importante.

### Événement de début

Il indique le point de départ du processus.

Exemple :

début du traitement d’un dossier.

### Événement de fin

Il indique la fin du processus.

Exemple :

validation du dossier.

---

## Les activités

Les **activités** représentent les actions réalisées dans le processus.

Elles correspondent aux tâches effectuées par les acteurs.

### Exemple d'activités

- vérifier un dossier
- enregistrer des données
- envoyer un document

Une activité est généralement représentée par un rectangle dans un diagramme BPMN.

---

## Les passerelles (décisions)

Les **passerelles** permettent de représenter une décision dans le processus.

Elles introduisent des conditions qui orientent le déroulement du processus.

### Exemple

Après vérification d'un dossier :

- si le dossier est complet → traitement
- sinon → demande d'informations complémentaires

Les passerelles permettent de représenter ces choix.

---

## Les flux

Les **flux** représentent les enchaînements entre les activités.

Ils indiquent l’ordre dans lequel les actions sont réalisées.

Exemple :

Réception du dossier → Vérification → Validation

Les flux permettent de visualiser la circulation de l'information dans le processus.

---

## Les acteurs (pools et lanes)

Dans BPMN, les acteurs sont représentés par des **pools** et des **lanes**.

Un pool représente généralement une organisation.

Une lane représente un acteur ou un service.

### Exemple

Pool : Administration fiscale

Lanes :

- service accueil
- service contrôle
- service validation

Cela permet de visualiser qui réalise chaque activité.

---

## Exemple de processus simple

Processus : traitement d'une demande

1. réception de la demande
2. vérification du dossier
3. décision
4. validation ou rejet

Pseudo-représentation :

Début  
→ réception de la demande  
→ vérification  
→ décision  
→ validation  
→ fin

---

## Les objectifs de la modélisation des processus

La modélisation permet de :

- comprendre le fonctionnement d’un processus
- identifier les points de blocage
- améliorer l’efficacité
- faciliter la communication entre les acteurs

Elle est souvent utilisée dans les phases d’analyse des systèmes d’information.

---

## À retenir

La modélisation des processus permet de représenter les activités d’un système d’information.

Le langage BPMN utilise plusieurs éléments :

- événements
- activités
- passerelles
- flux
- acteurs

Ces représentations facilitent l’analyse et l’amélioration des processus métier.