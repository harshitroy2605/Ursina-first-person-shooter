from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

set=Ursina()


class level_1_Class(Entity):
    def __init__(self,**kwargs):
        self.player = FirstPersonController()
        super().__init__(parent=self.player)
        self.blocks=[]
        self.player = FirstPersonController(model='cube', z=10, color=color.orange, origin_y=0.6, speed=8)


    def environment(self):
        Sky(texture="sky_default")
        for i in range (50):
            for j in range(50):
                self.block=Button(
                    color=color.white,
                    model='cube',
                    position=(j,0,i),
                    texture='brick',
                    parent=scene,
                    origin_y=0.5)
                self.blocks.append(self.block)


    def weapons(self):
        self.ak47_gun = Entity(
            parent=camera.ui,
            scale=0.009,
            model='assets\\ak47_upgrade\\imsource\\ak47_tactical_upgrade.fbx',
            texture = 'assets\\ak47_upgrade\\textures\\ak_Base_color',
            position = Vec3(0,-0.2,1.4),
            rotation=Vec3(10,0,0),
            visible=False)


        self.pistol = Entity(
            parent=camera.ui,
            scale=0.0003,
            model='assets\\pistol\\source\\sketchfab.fbx',
            texture = 'assets\\pistol\\textures\\texturing_gun_Specular',
            position = Vec3(0,-.05,1),
            rotation=Vec3(0,0,0),
            visible=False)


        self.knife = Entity(
            parent=camera.ui,
            scale=0.002,
            model='assets\\knife\\source\\M9.fbx',
            texture = 'assets\\knife\\textures\\M9-1_DefaultMaterial_BaseColor.1001',
            position = Vec3(0,-.2,1),
            rotation=Vec3(0,0,0),
            visible=False)

        self.Weapons=[self.knife,self.pistol,self.ak47_gun]
        self.CurrentWeapon=0
        self.ChangeWeapon()


    def movement(self):
        self.player.x += held_keys['d'] * .1
        self.player.x -= held_keys['a'] * .1


    def ChangeWeapon(self):
        for x,y in enumerate(self.Weapons):
            if x == self.CurrentWeapon:
                y.visible = True
            else:
                y.visible = False

    def input(self,key):
        try:
            self.CurrentWeapon=int(key) - 1
            self.ChangeWeapon()
        except:
            pass

        if key == 'scroll up':
            self.CurrentWeapon = (self.CurrentWeapon + 1) % len(self.Weapons)
            self.ChangeWeapon()

        if key == 'scroll down':
            self.CurrentWeapon = (self.CurrentWeapon - 1) % len(self.Weapons)
            self.ChangeWeapon()

        if key == 'c':
            print("c is working")
  



def windowChoice(choice):

    if choice=="level_1":
        level1 = level_1_Class()
        level1.environment()
        level1.weapons()
        level1.movement()



windowChoice("level_1")


set.run()

