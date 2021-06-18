from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)


def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['q'] * .1
    player.y += held_keys['z'] * .1
    player.y -= held_keys['s'] * .1


app.run()   # opens a window and starts the game.
