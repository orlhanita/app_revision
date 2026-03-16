# SQL (Structured Query Language)

## Introduction

SQL (Structured Query Language) est le langage utilisé pour manipuler les bases de données relationnelles.

Il permet de :

- consulter des données
- ajouter des informations
- modifier des enregistrements
- supprimer des données

SQL est utilisé dans la plupart des systèmes d'information.

Exemples de bases de données :

- PostgreSQL
- MySQL
- Oracle
- SQL Server

---

## Les tables

Dans une base de données relationnelle, les données sont organisées en **tables**.

Une table contient :

- des **colonnes** (les attributs)
- des **lignes** (les enregistrements)

### Exemple

Table : contribuable

| id | nom | ville |
|----|-----|------|
|1|Dupont|Paris|
|2|Martin|Lyon|

---

## SELECT : lire les données

La commande SELECT permet de lire les données d'une table.

### Exemple

SELECT nom  
FROM contribuable;

Cette requête affiche les noms des contribuables.

### Toutes les colonnes

SELECT *  
FROM contribuable;

---

## Filtrer avec WHERE

La clause WHERE permet de filtrer les résultats.

### Exemple

SELECT *  
FROM contribuable  
WHERE ville = 'Paris';

Cette requête affiche uniquement les contribuables vivant à Paris.

---

## Trier les résultats

La clause ORDER BY permet de trier les résultats.

### Exemple

SELECT *  
FROM contribuable  
ORDER BY nom;

### Tri décroissant

SELECT *  
FROM contribuable  
ORDER BY nom DESC;

---

## Limiter les résultats

La clause LIMIT permet de limiter le nombre de résultats.

### Exemple

SELECT *  
FROM contribuable  
LIMIT 5;

---

## INSERT : ajouter des données

La commande INSERT permet d'ajouter une ligne dans une table.

### Exemple

INSERT INTO contribuable (nom, ville)  
VALUES ('Durand','Marseille');

---

## UPDATE : modifier les données

La commande UPDATE permet de modifier un enregistrement.

### Exemple

UPDATE contribuable  
SET ville = 'Lille'  
WHERE id = 2;

---

## DELETE : supprimer des données

La commande DELETE permet de supprimer un enregistrement.

### Exemple

DELETE FROM contribuable  
WHERE id = 3;

---

## Les jointures

Les jointures permettent de combiner les données de plusieurs tables.

### Exemple

Tables :

contribuable

| id | nom |
|----|----|
|1|Dupont|

declaration

| id | id_contribuable | montant |
|----|----|----|
|1|1|2000|

### Requête

SELECT contribuable.nom, declaration.montant  
FROM contribuable  
JOIN declaration  
ON contribuable.id = declaration.id_contribuable;

Cette requête affiche les déclarations associées aux contribuables.

---

## Les fonctions d'agrégation

Les fonctions d'agrégation permettent de faire des calculs sur plusieurs lignes.

| Fonction | Rôle |
|--------|------|
|COUNT|compter|
|SUM|somme|
|AVG|moyenne|
|MAX|maximum|
|MIN|minimum|

### Exemple

SELECT COUNT(*)  
FROM contribuable;

Cette requête compte le nombre de contribuables.

---

## GROUP BY

La clause GROUP BY permet de regrouper les données.

### Exemple

SELECT ville, COUNT(*)  
FROM contribuable  
GROUP BY ville;

Cette requête compte le nombre de contribuables par ville.

---

## Exercice

On considère la table suivante :

Table : contribuable

| id | nom | ville |
|----|----|----|
|1|Dupont|Paris|
|2|Martin|Lyon|
|3|Durand|Paris|

Question :

Écrire une requête SQL permettant d'afficher les contribuables vivant à Paris.

Réponse attendue :

SELECT *  
FROM contribuable  
WHERE ville = 'Paris';

---

[QUIZ]

Question : Quelle commande SQL permet de récupérer des données ?

A. INSERT  
B. SELECT  
C. DELETE  
D. UPDATE  

Réponse : B

[/QUIZ]

[QUIZ]

Question : Quelle clause permet de filtrer les résultats ?

A. GROUP BY  
B. ORDER BY  
C. WHERE  
D. LIMIT  

Réponse : C

[/QUIZ]

[QUIZ]

Question : Quelle commande permet d'ajouter une ligne dans une table ?

A. UPDATE  
B. INSERT  
C. SELECT  
D. JOIN  

Réponse : B

[/QUIZ]

---

## À retenir

SQL permet de manipuler les données d'une base de données.

Les commandes essentielles sont :

- SELECT : lire les données
- INSERT : ajouter des données
- UPDATE : modifier les données
- DELETE : supprimer les données

Les jointures permettent de combiner plusieurs tables et les fonctions d'agrégation permettent d'analyser les données.