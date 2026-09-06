# hello_blender.py
# Étape 1 — Hello Blender
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : retrouver TON objet par son nom, puis afficher
# quelques infos. On ne change encore rien dans la scène.

import bpy

# Mets ici le vrai nom de TON objet (celui que tu as créé à partir du cube).
# Astuce : clique l'objet, le nom apparaît en haut à gauche de la vue 3D.
NOM_OBJET = "MonObjet"

# On récupère l'objet grâce à son nom
obj = bpy.data.objects.get(NOM_OBJET)

if obj is None:
    print("Oups ! Je ne trouve pas d'objet nommé :", NOM_OBJET)
    print("Vérifie le nom dans Blender, puis change NOM_OBJET en haut du script.")
else:
    # Fais avec moi : on dit bonjour et on lit la position actuelle
    print("Hello ! Je vois ton objet :", obj.name)
    print("Il est ici (x, y, z) :", obj.location[:])


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Il n'y a pas de bonne réponse. Change, relance, observe.
#
# 1) Change NOM_OBJET pour tester un autre objet de ta scène
#    (lampe, caméra, un deuxième cube…).
#
# 2) Décommente une ou deux lignes ci-dessous pour explorer
#    d'autres infos simples. obj.data, c'est "le contenu" de l'objet
#    (le maillage, la forme).
#
# if obj is not None:
#     print("Type de données :", obj.data)
#     print("Nom du maillage :", obj.data.name)
#     print("Position X seule :", obj.location.x)
#     print("Position Y seule :", obj.location.y)
#     print("Position Z seule :", obj.location.z)
#     print("Échelle actuelle :", obj.scale[:])
#     print("Rotation actuelle :", obj.rotation_euler[:])
