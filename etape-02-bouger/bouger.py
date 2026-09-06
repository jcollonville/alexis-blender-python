# bouger.py
# Étape 2 — Bouger
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : déplacer TON objet en changeant sa position (location).

import bpy

# Mets ici le vrai nom de TON objet.
NOM_OBJET = "MonObjet"

# Fais avec moi : on ajoute un peu de X (droite) et un peu de Z (haut).
# Relance le script pour re-bouger — ça s'additionne à chaque fois.
DEPLACEMENT_X = 1
DEPLACEMENT_Z = 0.5

# Dans Blender, les 3 axes sont :
#   X = gauche / droite
#   Y = avant / arrière
#   Z = haut / bas  (vers le ciel !)

obj = bpy.data.objects.get(NOM_OBJET)

if obj is None:
    print("Oups ! Je ne trouve pas d'objet nommé :", NOM_OBJET)
    print("Vérifie le nom dans Blender, puis change NOM_OBJET en haut du script.")
else:
    obj.location.x = obj.location.x + DEPLACEMENT_X
    obj.location.z = obj.location.z + DEPLACEMENT_Z
    print(obj.name, "est maintenant ici (x, y, z) :", obj.location[:])


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Invente un petit saut ou un déplacement en diagonale.
# Change 1 ou 2 nombres seulement — pas besoin d'être "juste".
#
# Idées (modifie les variables en haut, ou décommente une ligne) :
#   DEPLACEMENT_X = 0
#   DEPLACEMENT_Z = 2          # un saut plus haut
#
#   obj.location.y = obj.location.y + 1   # avance aussi → diagonale
#
# Astuce : Ctrl+Z dans Blender annule le dernier déplacement.
