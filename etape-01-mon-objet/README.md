# Étape 01 — Mon objet

> **Tip** : le nom dans Blender et `NOM_OBJET` (en haut de `hello_blender.py`) doivent être **les mêmes**. Par défaut : `MonObjet`.

## Objectif

Créer **ton** objet à partir d’un cube (forme + couleur), le nommer, puis le retrouver en Python — et lire **où** il se trouve dans l’espace.

## Notion

**Coordonnées** : un point, trois axes, une origine.

Dans l’espace, un objet occupe un **point**. Un point, c’est trois nombres : **x**, **y**, **z**. Ce sont ses **coordonnées**.

L’**origine**, c’est `(0, 0, 0)` : le centre du monde Blender. Tous les autres points se mesurent à partir de là, comme les rues se mesurent depuis un carrefour.

Trois **axes** partent de ce carrefour :

- **x** : gauche / droite
- **y** : avant / arrière
- **z** : haut / bas — dans Blender, **Z pointe vers le ciel**

Mini-exemple : si `MonObjet` est à `(0, 0, 2)`, il n’a bougé ni à droite ni en avant. Il flotte **2 unités au-dessus de l’origine**, pile sur l’axe Z — comme un ballon accroché au plafond, droit au-dessus du centre de la pièce.

Le script de cette étape ne déplace rien. Il **lit** ces trois nombres. Avant de coder, tu dois savoir les voir.

## Voir

**Avant de lancer le script**, le nom doit matcher. Deux façons, tu choisis :

- soit tu renommes le cube en `MonObjet` (`F2` ou Outliner) ;
- soit tu gardes le nom que tu aimes, et tu changes `NOM_OBJET` en haut de `hello_blender.py` pour qu’il soit **exactement** le même.

Si ça ne colle pas, le script affiche un **Oups !** C’est voulu : il n’a pas trouvé ton objet. Tu corriges le nom, tu relances.

Ensuite, 3 à 5 minutes dans Blender, **sans code** — tu cherches les coordonnées de la Notion :

1. Cube : `Shift+A` → Mesh → Cube.
2. Forme : `Tab` → `G` / `S` / `E` (nez, bras, bosse…) → `Tab`.
3. Couleur : Properties (icône sphère) → New → Base Color.
4. Nom : `F2` → `MonObjet`.
5. Point : `N` → Location x / y / z.
6. Origine une seconde : `0`, `0`, `0` ou `Alt+G`. Puis replace-le.

Pas besoin que ce soit parfait. Juste reconnaissable, et à toi.

## Toucher

Ouvre `hello_blender.py` : Blender → **Scripting** → Open → Run Script.

En haut du fichier : `NOM_OBJET = "MonObjet"`. C’est le pont. Le script fait `import bpy`, cherche l’objet par ce nom, et affiche un hello + sa `location` s’il le trouve.

Ces trois nombres de `location`, ce sont **exactement** les coordonnées de la Notion : le point `(x, y, z)` mesuré depuis l’origine. Le script ne calcule rien de magique. Il lit le même point que toi dans le panneau.

En bas : une zone **À toi de jouer** (commentaires + idées à décommenter).

## À toi de jouer

Place ton objet à un point que **toi** tu choisis — par exemple l’origine, ou `(1, 0, 2)`.

**Avant** de lancer le script, écris les trois coordonnées que tu attends. Puis Run Script. Tes nombres et ceux de `location` doivent matcher.

Bonus : décommente `obj.location.x`, `.y`, `.z` dans la zone du script. Relie chaque nombre à un axe : lequel est la hauteur (Z) ?

Change aussi le nom, la couleur, la forme — ou les trois. Une seule règle : on doit encore reconnaître **ton** objet, et `NOM_OBJET` doit toujours matcher.

Pas de bonne réponse. C’est le tien.

## Astuce

`MonObjet` et `monobjet`, ce n’est pas la même chose. Copie-colle le nom, tu gagnes du temps.
