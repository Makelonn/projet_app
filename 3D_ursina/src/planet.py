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


root_folder = Path(__file__).parent.parent
asset_folder = root_folder / 'asset/'
texture_folder = asset_folder / 'texture/'

s = Sky()
my_texture = load_texture("space.jpg", path=texture_folder)
s.texture = my_texture

sun_texture = load_texture("sun.jpg", path=texture_folder)
earth_texture = load_texture("earth.jpg", path=texture_folder)
moon_texture = load_texture("moon.jpg", path=texture_folder)

rota_sun = Entity(position=0)
sun = Entity(model='sphere', position=0,
             scale=factor_scale*20, double_sided=False, texture=sun_texture, shader=lit_with_shadows_shader, parent=rota_sun)
sun.look_at((0, 0, 1), axis='up')

rota_planet1 = Entity(position=0)
planet1 = Entity(model='sphere', position=(0, factor_scale*50, 0),
                 scale=factor_scale*5, double_sided=True, parent=rota_planet1, texture=earth_texture)
# planet1.look_at((1, 0, 0), axis='right')
# planet1.rotation_x = 90


rota_planet2 = Entity(position=0)
planet2 = Entity(model='sphere', position=(0, factor_scale*30, 0),
                 scale=factor_scale*3, double_sided=True, parent=rota_planet2)
rota_moon1 = Entity(position=planet1.get_position())
moon1 = Entity(model='sphere', position=planet1.get_position()+(0, factor_scale*-40, 0),
               scale=factor_scale*2, double_sided=True, parent=rota_moon1, texture=moon_texture)

circle1 = Entity(model=Circle(50, mode='line', thickness=factor_scale*4), position=(0, factor_scale*30, 0),
                 scale=factor_scale*7, double_sided=True, parent=rota_planet2, shader=lit_with_shadows_shader)
circle1.rotation_x += 50
circle1.rotation_y += 49

EditorCamera()
camera.orthographic = True
pivot = Entity()
PointLight(parent=sun, x=0, y=0, z=0, shadows=True, color=color.white)


def update():   # update gets automatically called.

    rota_planet1.rotation_z = rota_planet1.rotation_z + 0.5*time.dt*100
    rota_planet2.rotation_z = rota_planet2.rotation_z + 1*time.dt*100

    rota_moon1.set_position(planet1.get_position(), relative_to=scene)
    rota_moon1.rotation_z = rota_moon1.rotation_z + 0.25*time.dt*100

    rota_sun.rotation_z = rota_sun.rotation_z + 0.1*time.dt*100

    planet1.rotation_z = planet1.rotation_z + time.dt*100
    planet2.rotation_z = planet2.rotation_z + time.dt*100

    camera.x += held_keys['d'] * .5 * factor_scale
    camera.x -= held_keys['q'] * .5 * factor_scale
    camera.y += held_keys['z'] * .5 * factor_scale
    camera.y += held_keys['s'] * .5 * factor_scale
    camera.z += held_keys['r'] * .5 * factor_scale
    camera.z -= held_keys['f'] * .5 * factor_scale


app.run()   # opens a window and starts the game.
