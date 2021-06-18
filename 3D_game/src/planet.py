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
antisun = Entity(position=0)

planet = Entity(model='sphere', position=(0, 50, 0),
                scale=5, double_sided=True, parent=antisun)


EditorCamera()
camera.orthographic = True


def update():   # update gets automatically called.

    antisun.rotation_x = antisun.rotation_x + time.dt*100


app.run()   # opens a window and starts the game.
