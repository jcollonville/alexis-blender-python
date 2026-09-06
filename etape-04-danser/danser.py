# danser.py
# Étape 4 — Danser
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : combiner position + rotation pour faire "danser" l'objet.
# Tu choisis les 3 nombres en haut, le script pose les keyframes.

import bpy
import math

# Mets ici le vrai nom de TON objet.
NOM_OBJET = "MonObjet"

# À toi de choisir ces 3 nombres — ce sont tes "boutons" de danse.
AMPLITUDE = 1     # hauteur / largeur des pas (plus grand = plus large)
VITESSE = 10      # images entre chaque pose (plus petit = plus vite)
ANGLE = 30        # degrés de torsion à chaque pose

obj = bpy.data.objects.get(NOM_OBJET)

if obj is None:
    print("Oups ! Je ne trouve pas d'objet nommé :", NOM_OBJET)
    print("Vérifie le nom dans Blender, puis change NOM_OBJET en haut du script.")
else:
    # On mémorise le point de départ, pour ne pas perdre l'objet.
    depart_x = obj.location.x
    depart_y = obj.location.y
    depart_z = obj.location.z

    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 1 + 4 * VITESSE

    # Fais avec moi : 5 poses (gauche / haut / droite / bas / retour).
    poses = [
        (depart_x - AMPLITUDE, depart_y, depart_z, -ANGLE),
        (depart_x, depart_y, depart_z + AMPLITUDE, 0),
        (depart_x + AMPLITUDE, depart_y, depart_z, ANGLE),
        (depart_x, depart_y + AMPLITUDE, depart_z, -ANGLE),
        (depart_x, depart_y, depart_z, 0),
    ]

    for i, (x, y, z, angle) in enumerate(poses):
        frame = 1 + i * VITESSE
        scene.frame_set(frame)
        obj.location = (x, y, z)
        obj.rotation_euler.z = math.radians(angle)
        obj.keyframe_insert(data_path="location", frame=frame)
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    print(obj.name, "connaît une petite danse. Appuie sur Espace pour la voir !")


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Invente TA danse en ne touchant que AMPLITUDE, VITESSE et ANGLE
# (en haut du fichier). Relance le script, puis Espace.
#
# Exemples à tester — aucune n'est "la bonne" :
#   AMPLITUDE = 2     # pas plus grands
#   VITESSE = 5       # plus rapide
#   ANGLE = 90        # quart de tour à chaque pose
#
#   AMPLITUDE = 0.3   # tout petit tremblement
#   VITESSE = 20      # lent, presque un ballet
#   ANGLE = 180       # demi-tour à chaque pose
#
# Envie d'aller plus loin ? Ajoute aussi l'échelle dans la boucle :
#   obj.scale = (1.2, 1.2, 1.2)
#   obj.keyframe_insert(data_path="scale", frame=frame)
