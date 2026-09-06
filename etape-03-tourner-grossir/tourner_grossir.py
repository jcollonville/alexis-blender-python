# tourner_grossir.py
# Étape 3 — Tourner / grossir
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : faire tourner l'objet (un angle) et changer sa taille
# (une échelle), puis poser quelques images clés avec une boucle for.

import bpy
import math

# Mets ici le vrai nom de TON objet.
NOM_OBJET = "MonObjet"

# ---------------------------------------------------------------------------
# NOTION — Angle et échelle
# ---------------------------------------------------------------------------
# Tourner : on pense en degrés (90 = un quart de tour, 360 = un tour).
# Blender, lui, parle en radians. math.radians(90) fait la traduction.
# Grandir / rétrécir : l'échelle. 1 = taille normale, 2 = deux fois plus gros,
# 0.5 = deux fois plus petit.
# Ici : on tourne autour de Z (l'axe vertical) et on change la taille.

# Fais avec moi : un quart de tour, et un peu plus grand.
ANGLE_DEGREES = 90   # 90 degrés = un quart de tour
TAILLE = 1.3         # 1 = normal, plus grand = on grandit, plus petit = on rétrécit

obj = bpy.data.objects.get(NOM_OBJET)

if obj is None:
    print("Oups ! Je ne trouve pas d'objet nommé :", NOM_OBJET)
    print("Vérifie le nom dans Blender, puis change NOM_OBJET en haut du script.")
else:
    # math.radians traduit tes degrés pour Blender
    obj.rotation_euler.z = math.radians(ANGLE_DEGREES)
    obj.scale = (TAILLE, TAILLE, TAILLE)
    print(obj.name, "a tourné de", ANGLE_DEGREES, "degrés et a changé d'échelle.")

    # Petite boucle : on avance image par image et on pose une keyframe.
    # Ensuite, appuie sur Espace dans la vue 3D pour lire l'anim.
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 40

    for frame in range(1, 41):
        scene.frame_set(frame)
        # À chaque image, l'angle grandit un peu : 9 degrés de plus.
        # 40 images × 9 = 360 degrés = un tour complet.
        obj.rotation_euler.z = math.radians(frame * 9)
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    print("Keyframes posées. Appuie sur Espace pour voir tourner", obj.name)


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Joue avec l'angle et l'échelle. Il n'y a pas de bonne réponse.
#
# 1) Change ANGLE_DEGREES : 45 (petit coup), 180 (demi-tour), 360 (un tour).
# 2) Change TAILLE : 0.5 pour rétrécir, 2 pour grandir beaucoup.
#
# Idée respiration (décommente le bloc) : l'échelle grandit puis rétrécit.
#
# if obj is not None:
#     for frame in range(1, 41):
#         bpy.context.scene.frame_set(frame)
#         if frame <= 20:
#             s = 1 + frame / 20 * 0.4      # grandit
#         else:
#             s = 1.4 - (frame - 20) / 20 * 0.4  # rétrécit
#         obj.scale = (s, s, s)
#         obj.keyframe_insert(data_path="scale", frame=frame)
#
# Idée toupie : dans la boucle, remplace le 9 par 18 (plus vite)
# ou par 4 (plus lentement). C'est encore un angle, en degrés.
