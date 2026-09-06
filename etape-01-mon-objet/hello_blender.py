# hello_blender.py
# Étape 1 — Hello Blender
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : retrouver TON objet par son nom, puis lire
# ses coordonnées. On ne change encore rien dans la scène.

import bpy

# Mets ici le vrai nom de TON objet (celui que tu as créé à partir du cube).
# Astuce : clique l'objet, le nom apparaît en haut à gauche de la vue 3D.
NOM_OBJET = "MonObjet"

# ---------------------------------------------------------------------------
# NOTION — Coordonnées
# ---------------------------------------------------------------------------
# Un point dans l'espace, c'est 3 nombres : x, y et z.
#   x = gauche / droite
#   y = avant / arrière
#   z = haut / bas  (vers le ciel, dans Blender)
# Le point (0, 0, 0) s'appelle l'origine : le centre du monde.
# Ici, on lit les coordonnées de TON objet — "il est ici (x, y, z)".

# On récupère l'objet grâce à son nom
obj = bpy.data.objects.get(NOM_OBJET)

if obj is None:
    print("Oups ! Je ne trouve pas d'objet nommé :", NOM_OBJET)
    print("Vérifie le nom dans Blender, puis change NOM_OBJET en haut du script.")
else:
    # Fais avec moi : on dit bonjour et on lit le point (x, y, z)
    print("Hello ! Je vois ton objet :", obj.name)
    print("C'est un point dans l'espace. Ses coordonnées :")
    print("  x =", obj.location.x, "  (gauche / droite)")
    print("  y =", obj.location.y, "  (avant / arrière)")
    print("  z =", obj.location.z, "  (haut / bas)")
    print("L'origine du monde, c'est (0, 0, 0).")


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Il n'y a pas de bonne réponse. Change, relance, observe.
#
# 1) Bouge l'objet à la souris, relance le script : les 3 nombres changent.
#    Compare avec l'origine (0, 0, 0) : tu es à droite (x > 0) ? en haut (z > 0) ?
#
# 2) Décommente une ou deux lignes ci-dessous. Chaque ligne = un axe.
#
# if obj is not None:
#     print("Position X seule :", obj.location.x)
#     print("Position Y seule :", obj.location.y)
#     print("Position Z seule :", obj.location.z)
#     print("Le point complet (x, y, z) :", obj.location[:])
#
# 3) Change NOM_OBJET pour tester un autre objet (lampe, caméra…).
#    Chaque objet a son propre point dans l'espace.
