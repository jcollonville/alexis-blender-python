# tourner_grossir.py
# Étape 3 — Tourner / grossir
# À lancer DANS Blender : Scripting → Open → Run Script
#
# Objectif : faire tourner l'objet, changer sa taille, puis poser
# quelques images clés (keyframes) avec une boucle for.

import bpy
import math

# Mets ici le vrai nom de TON objet.
NOM_OBJET = "MonObjet"

# Fais avec moi : une petite rotation et une taille un peu plus grande.
# La rotation de Blender est en radians.
#   un demi-tour ≈ 3.14
#   un tour complet ≈ 6.28
# Plus simple : math.radians(90) veut dire "90 degrés".
ANGLE_DEGREES = 90
TAILLE = 1.3  # 1 = taille normale, 2 = deux fois plus gros

obj = bpy.data.objects.get(NOM_OBJET)

if obj is None:
    print("Oups ! Je ne trouve pas d'objet nommé :", NOM_OBJET)
    print("Vérifie le nom dans Blender, puis change NOM_OBJET en haut du script.")
else:
    obj.rotation_euler.z = math.radians(ANGLE_DEGREES)
    obj.scale = (TAILLE, TAILLE, TAILLE)
    print(obj.name, "a tourné et a changé de taille.")

    # Petite boucle : on avance image par image et on pose une keyframe.
    # Ensuite, appuie sur Espace dans la vue 3D pour lire l'anim.
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 40

    for frame in range(1, 41):
        scene.frame_set(frame)
        # À chaque image, on tourne un peu plus autour de Z (l'axe vertical).
        obj.rotation_euler.z = math.radians(frame * 9)  # 40 x 9 = 360° = 1 tour
        obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    print("Keyframes posées. Appuie sur Espace pour voir tourner", obj.name)


# ---------------------------------------------------------------------------
# À TOI DE JOUER
# ---------------------------------------------------------------------------
# Combine rotation + échelle pour un effet "respiration" ou "toupie".
# Il n'y a pas de bonne réponse — invente le tien.
#
# Idée respiration (décommente le bloc) : la taille grandit puis rétrécit.
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
# Idée toupie : change ANGLE_DEGREES ou le "9" dans frame * 9
# pour tourner plus vite (plus grand) ou plus lentement (plus petit).
