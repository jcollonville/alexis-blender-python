# bouger.py
# Étape 2 — Bouger
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : déplacer TON objet en ajoutant une flèche (un vecteur)
# à sa position actuelle.

import bpy

# Mets ici le vrai nom de TON objet.
NOM_OBJET = "MonObjet"

# ---------------------------------------------------------------------------
# NOTION — Vecteur
# ---------------------------------------------------------------------------
# Un vecteur, c'est une flèche : elle a une direction et une distance.
# Exemple : (1, 0, 0.5) = "1 pas à droite, 0 devant, un demi-pas vers le haut".
# Bouger, c'est ajouter cette flèche à l'endroit où tu es déjà.
# Relance le script : la flèche s'ajoute encore — ça s'accumule.

# Fais avec moi : une petite flèche vers la droite et vers le haut.
DEPLACEMENT_X = 1    # direction droite, distance 1
DEPLACEMENT_Y = 0    # pas d'avant / arrière pour l'instant
DEPLACEMENT_Z = 0.5  # un peu vers le ciel

# Les 3 axes (pour viser ta flèche) :
#   X = gauche / droite
#   Y = avant / arrière
#   Z = haut / bas  (vers le ciel !)

obj = bpy.data.objects.get(NOM_OBJET)

if obj is None:
    print("Oups ! Je ne trouve pas d'objet nommé :", NOM_OBJET)
    print("Vérifie le nom dans Blender, puis change NOM_OBJET en haut du script.")
else:
    # On ajoute la flèche au point actuel
    obj.location.x = obj.location.x + DEPLACEMENT_X
    obj.location.y = obj.location.y + DEPLACEMENT_Y
    obj.location.z = obj.location.z + DEPLACEMENT_Z
    print(obj.name, "a suivi la flèche. Nouveau point (x, y, z) :", obj.location[:])


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Invente TA flèche : change les 3 nombres du vecteur (X, Y, Z).
# Direction + distance, c'est toi qui choisis. Pas de "bonne" flèche.
#
# Idées (modifie les variables en haut) :
#   DEPLACEMENT_X = 0
#   DEPLACEMENT_Y = 0
#   DEPLACEMENT_Z = 2          # flèche tout droit vers le haut = un saut
#
#   DEPLACEMENT_X = 1
#   DEPLACEMENT_Y = 1
#   DEPLACEMENT_Z = 0          # flèche en diagonale, au sol
#
#   DEPLACEMENT_X = -1         # négatif = on inverse la flèche (vers la gauche)
#
# Astuce : Ctrl+Z dans Blender annule le dernier déplacement.
