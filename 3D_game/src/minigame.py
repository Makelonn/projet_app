from numpy import true_divide
from ursina import *   

app = Ursina()

# Some settings
window_size = window.size

# Our player 
g_path = Path(__file__).parent.parent / "asset" / "girl"
g_model = load_model('girl OBJ.obj', path=g_path)
player = Entity(model=g_model, texture= 'brick')
player.collider = 'mesh'
player.collider.show()


title = Text(text='Welcome to the game !', origin=(0,-19))

# A thing to go with player that will shout listen every 2 microsecond
tv = Entity(model='sphere', texture="../asset/video.mp4", parent=player)
# A surface ?
ground = Entity(model=Terrain('heightmap_1'), scale=(70,5,70), texture='heightmap_1')
EditorCamera()

def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['q'] * .1
    player.z += held_keys['z'] * .1
    player.z -= held_keys['s'] * .1
    # We want the sphere to revolve 
    tv.rotation_y += 60 * time.dt
    

def input(key):
    if key == 'b':
        tv.fade_out()
    elif key =='n':
        tv.fade_in()

app.run()   # opens a window and starts the game.