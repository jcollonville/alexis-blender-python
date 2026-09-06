# Alexis — Blender + Python

Tu crées un objet 3D dans Blender. Ensuite, tu le fais bouger avec un peu de Python (`bpy`).

**Mantra** : voir → toucher → inventer.  
**Maths** : x / y / z et un angle. Rien de plus.  
**Pont** : `NOM_OBJET` → `location` / `rotation_euler` / `scale` / keyframes.  
**Libre créativité** : chaque étape finit par un défi **À toi de jouer**. Il n’y a pas de bonne réponse unique.

Chaque étape enseigne une idée de **géométrie** ou de **physique simple** — pas seulement du code à coller.

Dans Blender, **Z pointe vers le haut** (vers le ciel).

## Étapes

| # | Titre | Notion | Voir (Blender) | Toucher (Python) |
|---|--------|--------|----------------|------------------|
| 1 | [Mon objet](etape-01-mon-objet/) | **Coordonnées** — point, axes x/y/z, origine | Modeler à partir d’un cube (forme + couleur + nom) | `hello_blender.py` — retrouver l’objet |
| 2 | [Bouger](etape-02-bouger/) | **Vecteur** — un déplacement = une flèche | Poser l’objet + une lumière | `bouger.py` — `location` (x / y / z) |
| 3 | [Tourner-grossir](etape-03-tourner-grossir/) | **Angle & échelle** — tourner, grandir / rétrécir | 2–3 keyframes à la main | `tourner_grossir.py` — `rotation_euler`, `scale`, boucle `for` |
| 4 | [Danser](etape-04-danser/) | **Oscillation** — amplitude + période | 2–3 propriétés que tu choisis | `danser.py` — position + rotation |

## Dossiers

Chaque dossier a une fiche et un script. En haut du script : `NOM_OBJET` (par défaut `"MonObjet"`). En bas : une zone **À toi de jouer**.

- [etape-01-mon-objet/](etape-01-mon-objet/) — `hello_blender.py`
- [etape-02-bouger/](etape-02-bouger/) — `bouger.py`
- [etape-03-tourner-grossir/](etape-03-tourner-grossir/) — `tourner_grossir.py`
- [etape-04-danser/](etape-04-danser/) — `danser.py`

Avant de lancer un script : le nom dans Blender et `NOM_OBJET` doivent être **les mêmes**. Sinon tu verras un « Oups ! » — c’est voulu.

## Prérequis

- Blender (une version récente, ça suffit)
- L’éditeur de scripts **intégré** à Blender (pas besoin d’installer Python à part)

Ouvre Blender, suis les étapes dans l’ordre, et invente à la fin de chacune.

---

Repo du salon **Project Alexis**.
