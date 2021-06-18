from ursina import *

app = Ursina()
window.title = 'My fucking game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
# Show the FPS (Frames per second) counter
window.fps_counter.enabled = True


player = Entity(model='cube', color=color.orange, scale_y=2)


def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['q'] * .1
    player.y += held_keys['z'] * .1
    player.y -= held_keys['s'] * .1

<<<<<<< HEAD
=======
    # et ça tourne tourne toune c'est ta façon  d'aimer.
    player.rotation_y = player.rotation_y + time.dt*100

>>>>>>> c90705d931ae0bb51356fe42f3bc2ef9f4e53ff4

app.run()   # opens a window and starts the game.
