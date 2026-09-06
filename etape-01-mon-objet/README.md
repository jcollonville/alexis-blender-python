# Étape 01 — Mon objet

## Objectif

Créer **ton** objet à partir d’un cube (forme + couleur), le nommer, puis le retrouver en Python.

## Voir

**Avant de lancer le script**, le nom doit matcher. Deux façons, tu choisis :

- soit tu renommes le cube en `MonObjet` (Outliner / liste des objets, ou panneau Objet) ;
- soit tu gardes le nom que tu aimes, et tu changes `NOM_OBJET` en haut de `hello_blender.py` pour qu’il soit **exactement** le même.

Si ça ne colle pas, le script affiche un **Oups !** C’est voulu : il n’a pas trouvé ton objet. Tu corriges le nom, tu relances.

Ensuite, 3 à 5 minutes dans Blender, sans code :

1. Pars du cube de départ (ou ajoute-en un).
2. Change sa forme : étire-le, ajoute un nez, des bras, une bosse… ce que tu veux.
3. Donne-lui une couleur que tu aimes.
4. Donne-lui un **nom clair**, sans espace — `MonObjet` si tu veux zéro surprise.

Pas besoin que ce soit parfait. Juste reconnaissable, et à toi.

## Toucher

Ouvre `hello_blender.py` : Blender → **Scripting** → Open → Run Script.

En haut du fichier : `NOM_OBJET = "MonObjet"`. C’est le pont. Le script fait `import bpy`, cherche l’objet par ce nom, et affiche un hello + sa `location` s’il le trouve.

En bas : une zone **À toi de jouer** (commentaires + idées à décommenter).

## À toi de jouer

Change le nom, la couleur, la forme — ou les trois.

Une seule règle : on doit encore reconnaître **ton** objet, et `NOM_OBJET` doit toujours matcher.

Pas de bonne réponse. C’est le tien.

## Astuce

`MonObjet` et `monobjet`, ce n’est pas la même chose. Copie-colle le nom, tu gagnes du temps.
