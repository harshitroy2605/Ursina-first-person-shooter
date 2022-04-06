
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

set=Ursina()


class level_1_Class(Entity):
    def __init__(self,**kwargs):
        self.player = FirstPersonController()
        super().__init__(parent=self.player)
        self.blocks=[]
        self.player.position.z = 10
        window.fullscreen = True


    def environment(self):
        Sky(texture="sky_default")
        self.ground = Entity(
            model = 'plane',
            texture = 'grass',
            collider = 'mesh',
            scale= Vec3(100,1,100))

       

        self.wall1 = Entity(parent=scene,
            scale=0.02,
            position=Vec3(-50,-0.5,0),
            rotation=Vec3(0,270,0),
            model='assets\\wall1\\source\\PhotoscannedStoneWall01_Final.fbx',
            texture = 'assets\\wall1\\textures\\PhotoscannedStoneWall01_Final_Photoscanned',
            collider = 'box')


        self.ground = Entity(
            model = 'plane',
            texture = 'brick',
            collider = 'mesh',
            #scale= Vec3(100,1,100),
            position = (0,6,0),
            double_sided=True
            )





## ------------------------front wall ------------------------------------------

        self.wall2 = duplicate(self.wall1,position=Vec3(-50,-0.50,-10))
        self.wall3 = duplicate(self.wall1,position=Vec3(-50,-0.50,-20))
        self.wall4 = duplicate(self.wall1,position=Vec3(-50,-0.50,-30))
        self.wall5 = duplicate(self.wall1,position=Vec3(-50,-0.50,-40))
        self.wall6 = duplicate(self.wall1,position=Vec3(-50,-0.50,-50))       
        self.wall7 = duplicate(self.wall1,position=Vec3(-50,-0.50,0))
        self.wall8 = duplicate(self.wall1,position=Vec3(-50,-0.50,10))
        self.wall9 = duplicate(self.wall1,position=Vec3(-50,-0.50,20))
        self.wall10 = duplicate(self.wall1,position=Vec3(-50,-0.50,30))
        self.wall11 = duplicate(self.wall1,position=Vec3(-50,-0.50,40))
        self.wall11 = duplicate(self.wall1,position=Vec3(-50,-0.50,50))




## ------------------------left side wall ------------------------------------------



        self.wall6 = duplicate(self.wall1,position=Vec3(-50,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall7 = duplicate(self.wall1,position=Vec3(-40,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall8 = duplicate(self.wall1,position=Vec3(-30,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall9 = duplicate(self.wall1,position=Vec3(-20,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall10 = duplicate(self.wall1,position=Vec3(-10,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall11 = duplicate(self.wall1,position=Vec3(0,-0.50,-50),rotation=Vec3(0,180,0))
       # self.wall12 = duplicate(self.wall1,position=Vec3(10,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall13 = duplicate(self.wall1,position=Vec3(20,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall14 = duplicate(self.wall1,position=Vec3(30,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall15 = duplicate(self.wall1,position=Vec3(40,-0.50,-50),rotation=Vec3(0,180,0))
        self.wall16 = duplicate(self.wall1,position=Vec3(50,-0.50,-50),rotation=Vec3(0,180,0))


## ------------------------back wall ------------------------------------------


        self.wall17 = duplicate(self.wall1,position=Vec3(50,-0.50,0),rotation=Vec3(0,90,0))
        self.wall18 = duplicate(self.wall1,position=Vec3(50,-0.50,-10),rotation=Vec3(0,90,0))
        self.wall19 = duplicate(self.wall1,position=Vec3(50,-0.50,-20),rotation=Vec3(0,90,0))
        self.wall20 = duplicate(self.wall1,position=Vec3(50,-0.50,-30),rotation=Vec3(0,90,0))
        self.wall21 = duplicate(self.wall1,position=Vec3(50,-0.50,-40),rotation=Vec3(0,90,0))
        self.wall22 = duplicate(self.wall1,position=Vec3(50,-0.50,-50),rotation=Vec3(0,90,0))
        self.wall23 = duplicate(self.wall1,position=Vec3(50,-0.50,10),rotation=Vec3(0,90,0))
        self.wall24 = duplicate(self.wall1,position=Vec3(50,-0.50,20),rotation=Vec3(0,90,0))
        self.wall25 = duplicate(self.wall1,position=Vec3(50,-0.50,30),rotation=Vec3(0,90,0))
        self.wall26 = duplicate(self.wall1,position=Vec3(50,-0.50,40),rotation=Vec3(0,90,0))
        self.wall27 = duplicate(self.wall1,position=Vec3(50,-0.50,50),rotation=Vec3(0,90,0))


## ------------------------right side wall ------------------------------------------

        self.wall6 = duplicate(self.wall1,position=Vec3(-50,-0.50,50),rotation=Vec3(0,0,0))
        self.wall7 = duplicate(self.wall1,position=Vec3(-40,-0.50,50),rotation=Vec3(0,0,0))
        self.wall8 = duplicate(self.wall1,position=Vec3(-30,-0.50,50),rotation=Vec3(0,0,0))
        self.wall9 = duplicate(self.wall1,position=Vec3(-20,-0.50,50),rotation=Vec3(0,0,0))
        self.wall10 = duplicate(self.wall1,position=Vec3(-10,-0.50,50),rotation=Vec3(0,0,0))
        self.wall11 = duplicate(self.wall1,position=Vec3(0,-0.50,50),rotation=Vec3(0,0,0))
        self.wall12 = duplicate(self.wall1,position=Vec3(10,-0.50,50),rotation=Vec3(0,0,0))
        self.wall13 = duplicate(self.wall1,position=Vec3(20,-0.50,50),rotation=Vec3(0,0,0))
        self.wall14 = duplicate(self.wall1,position=Vec3(30,-0.50,50),rotation=Vec3(0,0,0))
        self.wall15 = duplicate(self.wall1,position=Vec3(40,-0.50,50),rotation=Vec3(0,0,0))
        self.wall16 = duplicate(self.wall1,position=Vec3(50,-0.50,50),rotation=Vec3(0,0,0))





# --------------------- room wall 1-------------------------------------------------------

        self.roomw1all1 = duplicate(self.wall1,position=Vec3(-25,-0.50,-30),double_sided=True)
        self.roomw1all2 = duplicate(self.wall1,position=Vec3(-25,-0.50,-40),double_sided=True)
        self.roomw1all3 = duplicate(self.wall1,position=Vec3(-25,-0.50,-50),double_sided=True)

        self.roomw1all4 = duplicate(self.wall1,position=Vec3(-45,-0.50,-24),rotation=Vec3(0,0,0),double_sided=True)
        self.roomw1all5 = duplicate(self.wall1,position=Vec3(-30,-0.50,-24),rotation=Vec3(0,0,0),double_sided=True)



#----------------------- room pillar -----------------------------------------------------


        self.pillarroom1 = Entity(parent=scene,
            scale=0.02,
            position=Vec3(-39,-0.70,-24),
            model='assets\\stone_pillar\\source\\ConcretePillar01.fbx',
            texture = 'assets\\stone_pillar\\textures\\ConcretePillar01_ConcretePillar01_BaseColo',
            collider = 'box',
            double_sided=True)

        self.pillarroom2 = Entity(parent=scene,
            scale=0.02,
            position=Vec3(-36,-0.70,-24),
            model='assets\\stone_pillar\\source\\ConcretePillar01.fbx',
            texture = 'assets\\stone_pillar\\textures\\ConcretePillar01_ConcretePillar01_BaseColo',
            collider = 'box',
            double_sided=True)



# -----------------------------Bed --------------------------------------------------------------

        self.bed = Entity(parent=scene,
            scale=0.03,
            position=Vec3(-30,0,-44),
            rotation=Vec3(270,270,0),
            model='assets\\bed\\source\\Bed.fbx',
            texture = 'assets\\bed\\textures\\Bed_Albedo.tga',
            collider = 'box',
            double_sided=True)


# -----------------------------Painting --------------------------------------------------------------

        self.painting = Entity(parent=scene,
            scale=0.26,
            position=Vec3(-25.6,0,-36),
            rotation=Vec3(0,270,0),
            model='assets\\ganesha_idol\\source\\mesh.obj',
            texture = 'assets\\ganesha_idol\\textures\\mesh01',
            collider = 'box',
            double_sided=True)







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

        elif key == 'scroll down':
            self.CurrentWeapon = (self.CurrentWeapon - 1) % len(self.Weapons)
            self.ChangeWeapon()

        elif key == 'a':
            self.player.x -= time.dt * .1
            #self.enemy_robot.rotation_y+= time.dt*500

        elif key == 'd':
            self.player.x += time.dt * .1
            #self.enemy_robot.rotation_y+= time.dt*500


    def enemy(self):
        self.enemy_robot = Entity(
                    scale=0.01,
                    model='assets\\robot\\source\\model',
                    texture = 'assets\\robot\\textures\\Blitztank_Texture_edit3',
                    position = Vec3(20,0,20),
                    collider = 'box')
        self.enemy_robot.add_script(SmoothFollow(target=self.player,offset=[0,1,0],speed=0.2))


def windowChoice(choice):

    if choice=="level_1":
        level1 = level_1_Class()
        level1.environment()
        level1.weapons()
        level1.enemy()



windowChoice("level_1")


set.run()

