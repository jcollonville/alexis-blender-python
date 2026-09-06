# Étape 03 — Tourner, grossir

## Objectif

Faire tourner ton objet (`rotation_euler`) et le faire grossir (`scale`), avec une petite boucle `for` — une image-clé (keyframe) après l’autre.

## Notion

**Angle & échelle** : tourner (degrés → radians), grandir / rétrécir.

Un **angle**, c’est *combien* tu tournes, pas *où* tu es. Un tour complet = **360°**. Un demi-tour = **180°**. Un quart de tour = **90°**.

Toi, tu penses en **degrés**. Blender compte en **radians** : un autre cadran, où un demi-tour vaut ≈ `3.14` (π) et un tour ≈ `6.28`. Pas besoin d’apprendre la formule. `math.radians(90)` veut dire : « prends mes 90° et traduis-les ».

Dans Blender, **Z pointe vers le haut**. Tourner autour de Z, c’est tourner **sur place**, comme une toupie sur le sol : le haut reste le haut.

L’**échelle** (`scale`) est un **facteur** : on multiplie la taille. `1` = normal, `2` = deux fois plus gros, `0.5` = deux fois plus petit.

Ce n’est pas un déplacement : l’objet reste au même point. Seul son volume change.

Un angle et une échelle, ce n’est pas la même famille de nombres : l’un tourne, l’autre multiplie.

Mini-exemple : `MonObjet` est à l’échelle `1`, face vers toi. `ANGLE_DEGREES = 90` autour de Z : un quart de tour, tu le vois de profil. `TAILLE = 2` : le même objet, deux fois plus grand, au même endroit. Il n’a pas « marché ». Il a **tourné** et **grandi**.

## Voir

Avant le code, on sent le mouvement à la main — **angle** d’un côté, **échelle** de l’autre.

1. En bas de l’écran, clique une image de la barre du temps.
2. Tourne un peu l’objet (pense en degrés : un petit 30°, un quart de 90°…). Pose une **image-clé** (keyframe).
3. Avance de quelques images. Change encore l’angle, **ou** la taille (`scale`). Pose une autre image-clé.
4. Deux ou trois, ça suffit. Appuie sur lecture (Espace).

Regarde : quand tu tournes, le **point** (les coordonnées) peut rester le même. Quand tu changes l’échelle, l’objet reste au même endroit, mais son volume change. Ce n’est plus un vecteur. C’est un angle, ou un facteur.

Tu viens de faire une mini-anim sans une ligne de Python. Le script fera la même chose, en plus régulier.

## Toucher

Ouvre `tourner_grossir.py` : Scripting → Open → Run Script.

En haut : `NOM_OBJET`, plus `ANGLE_DEGREES` et `TAILLE`.

Tu vas toucher à trois choses — et aux deux idées de la Notion :

- `rotation_euler` — l’**angle**. Souvent autour de **Z**, l’axe vertical. Toi tu donnes des **degrés** ; `math.radians(...)` traduit pour Blender.
- `scale` — l’**échelle**. `1` = normal, `2` = deux fois plus gros.
- une boucle `for` qui pose des **keyframes**, image par image. Ici : `frame * 9` degrés → 40 images × 9° = **360°** = un tour.

Lance, appuie sur Espace, ajuste un nombre, relance.

En bas du fichier : zone **À toi de jouer**.

## À toi de jouer

Choisis **ton** angle en degrés **avant** de lancer. Un quart de tour (90) ? Un demi (180) ? Un tour (360) ?

Prédis ce que tu vas voir, puis change `ANGLE_DEGREES` — ou le `9` dans `frame * 9` (plus grand = plus vite, plus petit = plus lent).

Puis joue avec l’échelle : un pulse gros-petit-gros (idée « respiration » en bas du script), ou une toupie qui grandit.

Combine léger. C’est **ton** mouvement. Pas de bonne chorégraphie.

## Astuce

Si tu vois un **Oups !**, `NOM_OBJET` ne colle pas au nom dans Blender. Rien ne tourne tant que ça n’est pas pareil.
