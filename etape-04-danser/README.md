# Étape 04 — Danser

## Objectif

Faire **danser** ton objet : `location` + `rotation_euler`, avec 2 ou 3 variables que **toi** tu choisis. La danse, en physique simple, c’est une **oscillation**.

## Notion

**Oscillation** : amplitude + période (la « danse »).

Une oscillation, c’est un mouvement qui **s’éloigne** d’un point de repos, puis **revient**, encore et encore. Comme une balançoire, un yoyo, ou toi qui tapes du pied en rythme.

Deux boutons commandent ça :

- l’**amplitude** : *de combien* tu t’éloignes du repos. Grande amplitude = grands pas. Petite = presque un tremblement.
- la **période** : *combien de temps* pour un aller-retour complet (revenir au départ). Période courte = danse rapide. Période longue = ballet lent.

Ce n’est plus « aller quelque part et s’arrêter » (un seul vecteur). C’est **repasser par les mêmes poses**, en boucle.

Mini-exemple : `MonObjet` part de son point. `AMPLITUDE = 1` : il s’éloigne d’**1** à gauche, d’**1** vers le ciel, d’**1** à droite… puis il rentre à la maison. Double l’amplitude : même chorégraphie, des pas **deux fois plus grands**.

`PERIODE` plus petit = moins d’images = période plus courte = danse plus rapide. `ANGLE`, lui, c’est la torsion à chaque pose — le « style » par-dessus le rythme.

## Voir

Tu connais déjà les manettes, toutes branchées sur `NOM_OBJET` :

- `location` — où il est (x / y / z, Z vers le haut)
- `rotation_euler` — comment il est tourné
- `scale` — sa taille
- les **keyframes** — les poses que Blender relie ensuite

Choisis-en **deux ou trois**. Ce sont tes leviers pour la danse.

Avant le script, une oscillation à la main : aller à gauche, retour au centre.

1. Image `1` : `I` → Location (repos).
2. Plus loin : `G` puis `X`, puis `I`.
3. Encore plus loin : reviens au centre, `I`.
4. `Espace` pour lire.

`PERIODE` dans le script = images entre les poses (pas une « vitesse »).

Pas besoin de tout utiliser. Deux, c’est déjà une chorégraphie.

## Toucher

Ouvre `danser.py` : Scripting → Open → Run Script.

En haut : `NOM_OBJET`, puis tes boutons `AMPLITUDE`, `PERIODE`, `ANGLE`.

Relie-les à la Notion :

- `AMPLITUDE` — **amplitude** : largeur / hauteur des pas
- `PERIODE` — **période** : images entre chaque pose (`PERIODE` plus petit = moins d’images = période plus courte = danse plus rapide)
- `ANGLE` — torsion à chaque pose (en degrés ; `math.radians` traduit)

Le script combine `location` et `rotation_euler`, pose les keyframes, et ramène l’objet au départ : un cycle d’oscillation.

Relance, appuie sur Espace. Si ça part dans tous les sens, baisse un peu les valeurs.

C’est normal de tâtonner. C’est comme ça qu’on trouve **sa** danse.

En bas du fichier : zone **À toi de jouer**.

## À toi de jouer

D’abord, **sépare** les deux idées de la Notion.

1. Change **seulement** `AMPLITUDE` (laisse `PERIODE` et `ANGLE`). Les pas deviennent plus grands ou plus petits — le rythme, lui, ne change pas.
2. Remets l’amplitude, change **seulement** `PERIODE`. Même dessin, autre tempo : période plus courte ou plus longue.

Ensuite, invente **ta** chorégraphie. Un rebond. Un tour sur place. Un glissement + une petite rotation. Ce que tu veux.

Il n’y a pas de « bonne » danse. S’il oscille à ta façon, c’est gagné.

## Astuce

Change **un** bouton à la fois (`AMPLITUDE`, `PERIODE` ou `ANGLE`). Tu vois tout de suite si tu as touché l’amplitude, la période, ou juste le style.
