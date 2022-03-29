from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import keyboard



set=Ursina()



Sky(texture="sky_default")
player=FirstPersonController()

blocks=[]


player = FirstPersonController(model='cube', z=10, color=color.orange, origin_y=0.6, speed=8)

player.x += held_keys['d'] * .1
player.x -= held_keys['a'] * .1



ak47_gun_advance = Entity(
    parent=camera.ui,
    scale=0.009,
    model='assets\\ak47_upgrade\\imsource\\ak47_tactical_upgrade.fbx',
    texture = 'assets\\ak47_upgrade\\textures\\ak_Base_color',
    position = Vec3(0,-0.2,1.4),
    rotation=Vec3(10,0,0),
    visible=False)


pistol = Entity(
    parent=camera.ui,
    scale=0.0003,
    model='assets\\pistol\\source\\sketchfab.fbx',
    texture = 'assets\\pistol\\textures\\texturing_gun_Specular',
    position = Vec3(0,-.05,1),
    rotation=Vec3(0,0,0),
    visible=False)

knife = Entity(
    parent=camera.ui,
    scale=0.002,
    model='assets\\knife\\source\\M9.fbx',
    texture = 'assets\\knife\\textures\\M9-1_DefaultMaterial_BaseColor.1001',
    position = Vec3(0,-.2,1),
    rotation=Vec3(0,0,0))


for i in range (50):
    for j in range(50):
        block=Button(
            color=color.white,
            model='cube',
            position=(j,0,i),
            texture='brick',
            parent=scene,
            origin_y=0.5)
        blocks.append(block)


set.run()

