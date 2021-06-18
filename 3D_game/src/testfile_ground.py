from ursina import *   

app = Ursina()
window.title = 'Baj'
g_path = Path(__file__).parent.parent / "asset" / "girl"
g_model = load_model('girl OBJ.obj', path=g_path)
g_text = load_texture('girl OBJ', path=g_path)
player = Entity(model=g_model, texture=g_text)
title = Text(text='1234 56 Here is a game !123456789123456789', origin=(-.10,.5), wordwrap=1)
tv = Entity(model='sphere', texture="../asset/video.mp4", parent=player, origin_x=-2, origin_y=-2, origin_z=+2)
ground = Entity(model=Terrain('heightmap_1'), scale=(20,5,20), texture='heightmap_1')
EditorCamera()

def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['q'] * .1
    player.y += held_keys['z'] * .1
    player.y -= held_keys['s'] * .1


app.run()   # opens a window and starts the game.
