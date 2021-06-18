from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
window.title = 'My fucking game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
# Show the FPS (Frames per second) counter
window.fps_counter.enabled = True
factor_scale = 65
camera.z -= factor_scale*40

s = Sky()
root_folder = Path(__file__).parent.parent
asset_folder = root_folder / 'asset/'
texture_folder = asset_folder / 'texture/'
sun_texture = load_texture("sun.jpg", path=texture_folder)
my_texture = load_texture("space.jpg", path=texture_folder)
s.texture = my_texture

sun = Entity(model='sphere', position=0,
             scale=factor_scale*20, double_sided=False, texture=sun_texture, shader=lit_with_shadows_shader)
rota_planet1 = Entity(position=0)
planet1 = Entity(model='sphere', position=(0, factor_scale*50, 0),
                 scale=factor_scale*5, double_sided=True, parent=rota_planet1)
rota_planet2 = Entity(position=0)
planet2 = Entity(model='sphere', position=(0, factor_scale*30, 0),
                 scale=factor_scale*3, double_sided=True, parent=rota_planet2)
rota_moon1 = Entity(position=planet1.get_position())
moon1 = Entity(model='sphere', position=planet1.get_position()+(0, factor_scale*-40, 0),
               scale=factor_scale*2, double_sided=True, parent=rota_moon1)

# circle = Entity(model='circle', position=(0, 30, 0),
#                 scale=7, double_sided=True, parent=rota_planet2, shader=lit_with_shadows_shader)
circle1 = Entity(model=Circle(50, mode='line', thickness=factor_scale*4), position=(0, factor_scale*30, 0),
                 scale=factor_scale*7, double_sided=True, parent=rota_planet2, shader=lit_with_shadows_shader)
circle1.rotation_x += 50
circle1.rotation_y += 49

EditorCamera()
camera.orthographic = True
pivot = Entity()
PointLight(parent=sun, x=0, y=0, z=0, shadows=True, color=color.yellow)


def update():   # update gets automatically called.

    rota_planet1.rotation_z = rota_planet1.rotation_z + 0.5*time.dt*100
    rota_planet2.rotation_z = rota_planet2.rotation_z + 1*time.dt*100

    rota_moon1.set_position(planet1.get_position(), relative_to=scene)
    rota_moon1.rotation_z = rota_moon1.rotation_z + 0.25*time.dt*100

    # sun.rotation_z = sun.rotation_z + time.dt*100
    planet1.rotation_z = planet1.rotation_z + time.dt*100
    planet2.rotation_z = planet2.rotation_z + time.dt*100

    camera.x += held_keys['d'] * .5
    camera.x -= held_keys['q'] * .5
    camera.y += held_keys['z'] * .5
    camera.y -= held_keys['s'] * .5


app.run()   # opens a window and starts the game.
