# Étape 01 — Mon objet

## Objectif

Créer **ton** objet à partir d’un cube (forme + couleur), lui donner un nom clair, puis le retrouver en Python.

## Voir

On reste dans Blender, sans code. Compte 3 à 5 minutes.

1. Pars du cube de départ (ou ajoute-en un).
2. Change sa forme : étire-le, ajoute un nez, des bras, une bosse… ce que tu veux.
3. Donne-lui une couleur que tu aimes.
4. Donne-lui un **nom clair**, sans espace : `MonRobot`, `MaFusee`, `LeBlob`…

Ce nom, c’est le surnom de ton objet. Le script Python s’en servira pour le retrouver.

Pas besoin que ce soit parfait. Juste reconnaissable, et à toi.

## Toucher

Passe dans l’onglet **Scripting** de Blender (en haut).

Un fichier `hello.py` arrivera dans ce dossier. En attendant, retiens juste ça :

- `import bpy` — c’est ce qui parle à Blender.
- On récupère l’objet **par son nom** (celui que tu as choisi).
- Si Blender le trouve : un petit message de succès s’affiche.

Si rien ne se passe, regarde le nom. `MonRobot` et `monrobot`, ce n’est pas la même chose.

## À toi de jouer

Change le nom, la couleur, la forme — ou les trois.

Une seule règle : on doit encore reconnaître **ton** objet, et il doit rester nommé.

Pas de bonne réponse. C’est le tien.

## Astuce

Un nom sans espace ni accent évite les surprises dans le script. `MonRobot` plutôt que `Mon robot`.
