# Étape 03 — Tourner, grossir

## Objectif

Faire tourner ton objet (`rotation_euler`) et le faire grossir (`scale`), avec une petite boucle `for` — une image-clé (keyframe) après l’autre.

## Voir

Avant le code, on sent le mouvement à la main.

1. En bas de l’écran, clique une image de la barre du temps.
2. Tourne un peu l’objet, ou change sa taille. Pose une **image-clé** (keyframe).
3. Avance de quelques images. Change encore. Pose une autre image-clé.
4. Deux ou trois, ça suffit. Appuie sur lecture (Espace).

Tu viens de faire une mini-anim sans une ligne de Python. Le script fera la même chose, en plus régulier.

## Toucher

Ouvre `tourner_grossir.py` : Scripting → Open → Run Script.

En haut : `NOM_OBJET`, plus `ANGLE_DEGREES` et `TAILLE`.

Tu vas toucher à trois choses :

- `rotation_euler` — comment il tourne (souvent autour de **Z**, l’axe vertical).
- `scale` — la taille. `1` = normal, `2` = deux fois plus gros.
- une boucle `for` qui pose des **keyframes**, image par image.

Pour les angles : tu penses en degrés (90, 180…), et `math.radians(...)` traduit ça pour Blender.

Lance, appuie sur Espace, ajuste un nombre, relance.

En bas du fichier : zone **À toi de jouer**.

## À toi de jouer

Un spin qui n’en finit plus ? Un pulse de taille (gros-petit-gros) ? Un peu des deux ?

Combine léger. C’est **ton** mouvement. Pas de bonne chorégraphie.

## Astuce

Si tu vois un **Oups !**, `NOM_OBJET` ne colle pas au nom dans Blender. Rien ne tourne tant que ça n’est pas pareil.
