from ursina import *

app = Ursina()
window.title = 'My fucking game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
# Show the FPS (Frames per second) counter
window.fps_counter.enabled = True

sun = Entity(model='sphere', position=0,
             scale=20, double_sided=True)

rota_planet1 = Entity(position=0)
planet1 = Entity(model='sphere', position=(0, 50, 0),
                 scale=5, double_sided=True, parent=rota_planet1)

rota_planet2 = Entity(position=0)
planet2 = Entity(model='sphere', position=(0, 30, 0),
                 scale=3, double_sided=True, parent=rota_planet2)

rota_moon1 = Entity(position=planet1.get_position())
moon1 = Entity(model='sphere', position=planet1.get_position()+(0, -40, 0),
               scale=2, double_sided=True, parent=rota_moon1)

EditorCamera()
camera.orthographic = True


def update():   # update gets automatically called.

    rota_planet1.rotation_z = rota_planet1.rotation_z + 0.5*time.dt*100
    rota_planet2.rotation_z = rota_planet2.rotation_z + 1*time.dt*100

    rota_moon1.set_position(planet1.get_position(), relative_to=scene)
    rota_moon1.rotation_z = rota_moon1.rotation_z + 1.5*time.dt*100

    sun.rotation_z = sun.rotation_z + time.dt*100

    planet1.rotation_z = planet1.rotation_z + time.dt*100
    planet2.rotation_z = planet2.rotation_z + time.dt*100

    print("distance :",distance(planet1.get_position(),moon1.get_position()))

    # print("moon : ", moon1.get_position())
    # print("moon posi: ", moon1.position)
    # print("planet1 : ", planet1.get_position())
    # print("planet2 : ", planet2.get_position())


app.run()   # opens a window and starts the game.
