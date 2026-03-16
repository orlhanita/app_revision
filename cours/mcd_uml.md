# Modélisation des données (MCD / UML)

## Introduction

La modélisation des données consiste à représenter de manière structurée les informations manipulées par un système d’information.

Elle permet de :

- comprendre les données utilisées par une application
- organiser ces données de façon cohérente
- préparer la création d’une base de données

La modélisation est une étape essentielle dans la conception d’un système d’information.

Elle permet de traduire les besoins métiers en structures de données exploitables par les systèmes informatiques.

---

## Les objectifs de la modélisation des données

La modélisation des données permet de :

- structurer les informations
- éviter les redondances de données
- faciliter l’évolution du système
- améliorer la compréhension du système d’information

Elle sert également de support de communication entre :

- les experts métiers
- les analystes
- les développeurs
- les architectes du système

---

## Les différents niveaux de modélisation

La modélisation des données se fait généralement en plusieurs niveaux.

### Modèle conceptuel

Le **modèle conceptuel des données (MCD)** représente les données de manière indépendante de toute contrainte technique.

Il décrit :

- les entités
- les relations entre ces entités
- les propriétés des entités

Ce modèle est utilisé pour comprendre les besoins métier.

---

### Modèle logique

Le **modèle logique des données (MLD)** traduit le modèle conceptuel dans une structure adaptée aux bases de données.

Il précise :

- les tables
- les attributs
- les clés primaires
- les relations entre tables

---

### Modèle physique

Le **modèle physique des données (MPD)** correspond à l’implémentation réelle dans une base de données.

Il définit :

- les types de données
- les index
- les contraintes techniques

Ce modèle est directement utilisé dans les systèmes de gestion de bases de données.

---

## Les entités

Une **entité** représente un objet ou un concept du système d’information.

Exemples :

- un contribuable
- une entreprise
- une déclaration fiscale
- un agent

Chaque entité possède des **attributs** qui décrivent ses caractéristiques.

### Exemple

Entité : Contribuable

Attributs :

- identifiant
- nom
- prénom
- adresse

---

## Les relations entre entités

Les entités peuvent être reliées entre elles par des **relations**.

Une relation représente un lien logique entre deux entités.

### Exemple

Un contribuable peut déposer une déclaration.

Relation :

Contribuable → Déclaration

---

## Les cardinalités

La **cardinalité** décrit le nombre de relations possibles entre deux entités.

Elle permet de préciser combien d’occurrences d’une entité peuvent être associées à une autre.

### Exemples

1 contribuable peut avoir plusieurs déclarations.

Cardinalité :

Contribuable (1,N) — Déclaration

Un agent peut traiter plusieurs dossiers.

---

## Les clés

Dans une base de données, une **clé** permet d’identifier de manière unique un enregistrement.

### Clé primaire

La **clé primaire** identifie de manière unique une entité.

Exemple :

Table Contribuable

Clé primaire :

id_contribuable

---

### Clé étrangère

Une **clé étrangère** permet de créer un lien entre deux tables.

Elle référence la clé primaire d’une autre table.

Exemple :

Table Déclaration

clé étrangère :

id_contribuable

---

## UML et modélisation des données

Le langage **UML (Unified Modeling Language)** est souvent utilisé pour représenter les structures de données.

Le **diagramme de classes** est particulièrement utilisé.

Il permet de représenter :

- les classes
- les attributs
- les relations entre classes

Exemple de classe :

Classe Contribuable

Attributs :

- id
- nom
- adresse

---

## Normalisation des données

La normalisation consiste à organiser les données pour éviter les redondances.

Elle repose sur plusieurs règles appelées **formes normales**.

Objectifs :

- éviter la duplication des données
- améliorer la cohérence
- faciliter la maintenance des bases de données

---

## Exemple simple de modélisation

Entités :

Contribuable  
Déclaration

Relation :

Un contribuable peut déposer plusieurs déclarations.

Structure possible :

Contribuable  
- id_contribuable  
- nom  
- prénom  

Déclaration  
- id_declaration  
- date_declaration  
- id_contribuable  

---

## À retenir

La modélisation des données permet de structurer les informations utilisées par un système d’information.

Elle repose sur :

- les entités
- les relations
- les cardinalités
- les clés

Elle constitue une étape fondamentale dans la conception d’une base de données et d’un système d’information.