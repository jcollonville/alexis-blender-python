# danser.py
# Étape 4 — Danser
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : faire osciller l'objet — une danse qui va et qui revient.
# Tu règles l'amplitude et la période, le script pose les keyframes.

import bpy
import math

# Mets ici le vrai nom de TON objet.
NOM_OBJET = "MonObjet"

# ---------------------------------------------------------------------------
# NOTION — Oscillation
# ---------------------------------------------------------------------------
# Une oscillation, c'est un mouvement qui va et qui revient : la "danse".
# Amplitude : jusqu'où ça va (plus grand = pas plus larges).
# Période : le temps d'un aller-retour (plus d'images = plus lent).
# Ici, l'objet part, fait 4 poses, et revient au départ : un cycle.

# Fais avec moi : ces 3 nombres, ce sont tes boutons de danse.
AMPLITUDE = 1     # jusqu'où ça va (la "taille" des pas)
PERIODE = 40      # images pour un cycle complet (plus grand = plus lent)
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

    # 4 pas + le retour = 4 intervalles dans une période
    pas = PERIODE // 4

    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 1 + PERIODE

    # Fais avec moi : 5 poses (gauche / haut / droite / avant / retour).
    # L'amplitude écarte chaque pose du point de départ.
    poses = [
        (depart_x - AMPLITUDE, depart_y, depart_z, -ANGLE),
        (depart_x, depart_y, depart_z + AMPLITUDE, 0),
        (depart_x + AMPLITUDE, depart_y, depart_z, ANGLE),
        (depart_x, depart_y + AMPLITUDE, depart_z, -ANGLE),
        (depart_x, depart_y, depart_z, 0),
    ]

    for i, (x, y, z, angle) in enumerate(poses):
        frame = 1 + i * pas
        scene.frame_set(frame)
        obj.location = (x, y, z)
        obj.rotation_euler.z = math.radians(angle)
        obj.keyframe_insert(data_path="location", frame=frame)
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    print(obj.name, "connaît une petite danse. Appuie sur Espace pour la voir !")


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Invente TA danse en changeant AMPLITUDE et PERIODE (en haut).
# Relance le script, puis Espace. Aucune danse n'est "la bonne".
#
# Exemples à tester :
#   AMPLITUDE = 2     # pas plus grands (grande amplitude)
#   PERIODE = 20      # cycle plus court = plus rapide
#
#   AMPLITUDE = 0.3   # tout petit tremblement (petite amplitude)
#   PERIODE = 80      # cycle plus long = presque un ballet
#
#   ANGLE = 90        # quart de tour à chaque pose (bonus)
#
# Envie d'aller plus loin ? Ajoute aussi l'échelle dans la boucle :
#   obj.scale = (1.2, 1.2, 1.2)
#   obj.keyframe_insert(data_path="scale", frame=frame)
