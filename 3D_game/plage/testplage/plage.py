from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
from ursina.shaders import colored_lights_shader

# window.vsync = False
if not application.development_mode:
    window.show_ursina_splash = True
app = Ursina()

level = load_blender_scene('castaway_island')
model_bullet = load_model('45.obj')

# ursina.mesh_importer.obj_to_ursinamesh(model_bullet)
bullet = Entity(model=model_bullet, scale=0.1,
                position=level.start_point.position - (-3, 0, 0.75), collider='mesh')

player = FirstPersonController(position=level.start_point.position, speed=10)
level.mesh_collider.collider = 'mesh'
level.mesh_collider.visible = False


def input(key):
    if key == 'left mouse up':
        player.arrow = duplicate(
            bullet, world_parent=camera, position=Vec3(-.2, 0, 0), rotation=Vec3(0, 0, 0))
        player.arrow.world_parent = scene
        player.arrow.animate('position', Vec3(
            mouse.world_point), mouse.collision.distance/500, curve=curve.linear, interrupt='kill')
        destroy(player.arrow, delay=2)

    if held_keys['control'] and key == 'r':
        player.position = level.start_point.position


app.run()
