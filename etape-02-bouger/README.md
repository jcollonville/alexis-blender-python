# Étape 02 — Bouger

## Objectif

Déplacer ton objet avec `location` : trois nombres, **x** / **y** / **z**. Tu vas voir qu’un déplacement, ce n’est pas un lieu — c’est une **flèche**.

## Notion

**Vecteur** : un déplacement = une flèche (direction + distance).

Un **point**, tu le connais (étape 1) : c’est *où* est l’objet. Un **vecteur**, c’est *comment il bouge*. Une flèche a deux infos : **vers où** (la direction) et **de combien** (la distance).

On l’écrit aussi avec trois nombres. Mais ce n’est plus une adresse. C’est un **ajout** :

- `(1, 0, 0)` : 1 pas vers la droite, rien d’autre
- `(0, 0, 2)` : un saut de 2 vers le ciel (Z)
- `(1, 0, 0.5)` : en diagonale — droite **et** un peu vers le haut

Nouvelle position = ancien point + vecteur.

Mini-exemple : `MonObjet` est à `(0, 0, 0)`. Tu lui ajoutes le vecteur `(1, 0, 0.5)`. Il atterrit à `(1, 0, 0.5)` : un pas à droite, un demi-pas en l’air. Relance le même vecteur : il repart de là, et atterrit à `(2, 0, 1)`. La flèche ne change pas. C’est le point de départ qui a changé.

## Voir

Toujours dans Blender, encore sans code. Quelques minutes. Cette fois, tu ne regardes plus seulement le **point** : tu inventes une **flèche**.

1. Outliner : le nom matcher `NOM_OBJET` (souvent `MonObjet`).
2. Sol optionnel : `Shift+A` → Mesh → Plane, puis `S`.
3. Lumière : `Shift+A` → Light → Point, puis `G` puis `Z`.
4. Départ : `N` → Location.
5. Un axe : `G` puis `X` / `Y` / `Z`. Clic, ou un nombre + Entrée. `Ctrl+Z` pour annuler.

Ce geste **est** le vecteur : direction + distance.

Exemple : tu le lèves de 1. Ta flèche, c’est `(0, 0, 1)`. Direction : le ciel. Distance : 1.

Remets-le à un endroit que tu aimes. C’est ton point de départ.

## Toucher

Ouvre `bouger.py` : Scripting → Open → Run Script.

En haut : `NOM_OBJET`, puis `DEPLACEMENT_X` et `DEPLACEMENT_Z`. Ce ne sont pas des positions. Ce sont les composantes de **ton vecteur** : la flèche de la Notion.

Lance, regarde. Le script **ajoute** ces nombres à `location`. Relance : la même flèche se recolle, le point avance encore.

Pas besoin d’un grand saut. Un petit pas suffit pour voir que **toi**, tu commandes le vecteur.

Si tu vois un **Oups !** : le nom dans Blender et `NOM_OBJET` ne sont pas les mêmes.

En bas du fichier : zone **À toi de jouer**.

## À toi de jouer

Invente **une flèche**. Choisis une direction et une distance, **avant** de lancer.

Exemple : « un saut de 2 vers le ciel » → `DEPLACEMENT_X = 0`, `DEPLACEMENT_Z = 2`. Ou une diagonale : un peu de X **et** un peu de Y.

Calcule le point d’arrivée à la main (ancien point + vecteur). Lance. Compare.

Puis envoie-le ailleurs. Invente une petite série de flèches. Fais-le « téléporter » d’un coin à l’autre.

Tu choisis où il va. Il n’y a pas de bonne place.

## Astuce

Change **un seul** nombre à la fois (juste x, ou juste z). Tu vois tout de suite **quelle partie** de la flèche a changé.
