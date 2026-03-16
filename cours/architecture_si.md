# Architecture des systèmes d'information

## Introduction

L’architecture d’un système d’information (SI) décrit la manière dont les différentes composantes techniques et logicielles d’un système sont organisées et interagissent entre elles.

Elle permet de structurer les applications, les données et les infrastructures afin de garantir :

- la performance
- la maintenabilité
- la sécurité
- l’évolutivité du système

Dans un contexte administratif ou d’entreprise, l’architecture SI est essentielle pour assurer le bon fonctionnement des applications métiers.

---

## Qu’est-ce qu’un système d’information

Un **système d’information (SI)** est l’ensemble des moyens permettant de collecter, stocker, traiter et diffuser l’information au sein d’une organisation.

Il comprend :

- des **applications informatiques**
- des **bases de données**
- des **serveurs**
- des **réseaux**
- des **utilisateurs**

Le système d’information permet de soutenir les activités et les processus de l’organisation.

### Exemple

Dans une administration fiscale, le SI peut contenir :

- une application de gestion des contribuables
- une base de données contenant les déclarations fiscales
- des serveurs hébergeant les applications
- des agents utilisant ces applications pour traiter les dossiers

---

## Les couches d’un système d’information

Les systèmes d’information sont généralement organisés en **plusieurs couches**.

Cette organisation permet de séparer les responsabilités techniques.

### Couche présentation

La **couche présentation** correspond à l’interface utilisée par l’utilisateur.

Exemples :

- application web
- application mobile
- interface graphique d’une application métier

Son rôle est de permettre à l’utilisateur d’interagir avec le système.

---

### Couche logique (métier)

La **couche logique métier** contient les règles et les traitements de l’application.

Elle réalise les opérations nécessaires au fonctionnement du système.

Exemples :

- calcul d’un impôt
- validation d’une déclaration
- vérification de règles de gestion

Cette couche constitue le cœur fonctionnel de l’application.

---

### Couche données

La **couche données** assure le stockage et la gestion des informations.

Elle repose généralement sur une **base de données**.

Exemples :

- base de données SQL
- stockage des dossiers utilisateurs
- tables contenant les déclarations fiscales

Cette couche garantit la persistance des données.

---

## L’architecture trois tiers

L’architecture **trois tiers** est un modèle très répandu dans les systèmes d’information.

Elle repose sur la séparation en trois parties :

1. **Front-end** : interface utilisateur
2. **Back-end** : logique métier
3. **Base de données** : stockage des données

### Exemple

Utilisateur → Interface web → Serveur applicatif → Base de données

### Avantages

Cette architecture présente plusieurs avantages :

- meilleure organisation du système
- séparation des responsabilités
- facilité de maintenance
- possibilité de faire évoluer chaque couche indépendamment

---

## Les API dans l’architecture SI

Une **API (Application Programming Interface)** permet à différentes applications de communiquer entre elles.

Elle expose des services accessibles via des requêtes.

Par exemple :

- récupération d’informations utilisateur
- envoi de données vers un autre système
- consultation d’un service distant

Les API jouent un rôle central dans les architectures modernes.

---

## Les architectures distribuées

Dans une architecture distribuée, les différents composants du système sont répartis sur plusieurs machines ou serveurs.

Cela permet :

- d’améliorer la performance
- d’augmenter la capacité du système
- de mieux gérer la charge

Exemples :

- microservices
- systèmes cloud
- infrastructures réparties sur plusieurs serveurs

---

## Sécurité et architecture SI

La sécurité est un élément essentiel de l’architecture d’un système d’information.

Elle doit garantir :

- la **confidentialité** des données
- l’**intégrité** des informations
- la **disponibilité** des services

Les mesures de sécurité peuvent inclure :

- authentification des utilisateurs
- gestion des droits d’accès
- chiffrement des données
- surveillance du système

---

## À retenir

Un système d’information repose sur plusieurs éléments :

- des applications
- des données
- des infrastructures techniques

L’architecture du SI organise ces éléments en différentes couches afin de garantir :

- la robustesse
- la maintenabilité
- la sécurité
- l’évolutivité du système.