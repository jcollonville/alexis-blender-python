# Étape 03 — Tourner, grossir

## Objectif

Faire tourner ton objet (`rotation_euler`) et le faire grossir (`scale`), avec une petite boucle `for` — une image après l’autre.

## Voir

Avant le code, on sent le mouvement à la main.

1. En bas de l’écran, clique une image de la barre du temps.
2. Tourne un peu l’objet, ou change sa taille. Pose une **image-clé** (keyframe).
3. Avance de quelques images. Change encore. Pose une autre image-clé.
4. Deux ou trois, ça suffit. Appuie sur lecture.

Tu viens de faire une mini-anim sans une ligne de Python. Le script fera la même chose, en plus régulier.

## Toucher

Un fichier `tourner_grossir.py` arrivera dans ce dossier.

Tu vas toucher à trois choses :

- `rotation_euler` — l’angle. Un demi-tour, c’est environ **3.14** (Blender compte en radians ; 3.14 ≈ 180°).
- `scale` — la taille. `1` = normal, `2` = deux fois plus gros.
- une boucle `for` — « pour chaque image, change un peu ».

Lance, regarde, ajuste un nombre, relance.

## À toi de jouer

Un spin qui n’en finit plus ? Un pulse de taille (gros-petit-gros) ? Un peu des deux ?

Combine léger. C’est **ton** mouvement. Pas de bonne chorégraphie.

## Astuce

Garde un œil sur le nom de l’objet (étape 1). Si le script ne le trouve pas, rien ne tourne.
