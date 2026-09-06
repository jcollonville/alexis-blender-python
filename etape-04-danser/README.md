# Étape 04 — Danser

## Objectif

Faire **danser** ton objet : `location` + `rotation_euler`, avec 2 ou 3 variables que **toi** tu choisis.

## Voir

Tu connais déjà les manettes, toutes branchées sur `NOM_OBJET` :

- `location` — où il est (x / y / z, Z vers le haut)
- `rotation_euler` — comment il est tourné
- `scale` — sa taille
- les **keyframes** — les poses que Blender relie ensuite

Choisis-en **deux ou trois**. Ce sont tes leviers pour la danse.

Pas besoin de tout utiliser. Deux, c’est déjà une chorégraphie.

## Toucher

Ouvre `danser.py` : Scripting → Open → Run Script.

En haut : `NOM_OBJET`, puis tes boutons `AMPLITUDE`, `VITESSE`, `ANGLE`. Le script combine `location` et `rotation_euler`, pose les keyframes, et convertit l’angle avec `math.radians` (toi tu restes en degrés).

Relance, appuie sur Espace. Si ça part dans tous les sens, baisse un peu les valeurs.

C’est normal de tâtonner. C’est comme ça qu’on trouve **sa** danse.

En bas du fichier : zone **À toi de jouer**.

## À toi de jouer

Grande liberté, ici.

Invente **ta** chorégraphie. Un rebond. Un tour sur place. Un glissement + une petite rotation. Ce que tu veux.

Il n’y a pas de « bonne » danse. S’il bouge à ta façon, c’est gagné.

## Astuce

Change **un** bouton à la fois (`AMPLITUDE`, `VITESSE` ou `ANGLE`). Tu vois tout de suite ce que ça fait à la danse.
