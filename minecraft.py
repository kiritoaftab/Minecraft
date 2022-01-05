# from ursina import *
#
# class Test_cube(Entity):
#     def __init__(self):
#         super().__init__(
#             model = 'cube',
#             color =color.white,
#             texture= 'white-cube',
#             rotation= Vec3(45,45,45)
#         )
#
# class Test_button(Button):
#     def __init__(self):
#         super().__init__(
#             parent = scene,
#             model = 'cube',
#             texture = 'brick',
#             color = color.blue,
#             highlight_color = color.red,
#             pressed_color = color.lime
#         )
#     def input(self,key):
#         if self.hovered:
#             if key == 'left mouse down':
#                 print('Button pressed')
# def update():
#     # print('test')
#     if held_keys['a']:
#         test_square.x -=1* time.dt
# app=Ursina()
#
# test_square= Entity(model = 'quad',color =color.red,scale =(1,4),position=(5,1))
# ling_texture= load_texture('assets/ling.png')
# ling= Entity(model='quad', texture =ling_texture )
#
# # test_cube=Test_cube()
# test_button=Test_button()
# app.run()

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina()
grass_texture=load_texture('Minecraft_Assets/grass_block.png')
stone_texture=load_texture('Minecraft_Assets/stone_block.png')
brick_texture=load_texture('Minecraft_Assets/brick_block.png')
dirt_texture=load_texture('Minecraft_Assets/dirt_block.png')
sky_texture=load_texture('Minecraft_Assets/skybox.png')
arm_texture=load_texture('Minecraft_Assets/arm_texture.png')
punch_sound = Audio('Minecraft_Assets/punch_sound',loop = False, autoplay= False)
block_pick=1

window.fps_counter.enabled= False
window.exit_button.visible = False
def update():
    global block_pick
    if held_keys[ '1']:block_pick=1
    if held_keys['2']: block_pick =2
    if held_keys['3']: block_pick =3
    if held_keys['4']: block_pick =4
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
class Voxel(Button):
    def __init__(self,position  = (0,0,0),texture=grass_texture):
        super().__init__(
            parent= scene,
            position = position,
            model= 'Minecraft_Assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            # highlight_color = color.lime,
            scale=0.5
        )
    def input(self, key):
        if self.hovered:

            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position=self.position + mouse.normal,texture=grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture =sky_texture,
            scale = 150,
            double_sided=True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,#this is a 2-d static viewport
            model = 'Minecraft_Assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation = Vec3(150,-10,0),
            position= Vec2(0.4,-0.6)
        )
    def active(self):
        self.rotation = Vec3(150, -10, 0)
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position= Vec2(0.4,-0.6)
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky= Sky()
hand=Hand()
app.run()