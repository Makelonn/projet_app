from ursina import *
from os import path

app = Ursina()
window.title = 'My fucking game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
# Show the FPS (Frames per second) counter
window.fps_counter.enabled = True

root_folder = Path(__file__).parent.parent
asset_folder = root_folder / 'asset/'
texture_folder = asset_folder / 'texture/'

girl = load_model("girl_OBJ.obj", path=asset_folder, file_types=(
    '.bam', '.ursinamesh', '.obj', '.glb', '.gltf', '.blend'))

my_texture = load_texture("bot color.jgp", path=texture_folder)

player = Entity(model=girl, position=0,
                scale=10, double_sided=True)  # , texture='white_cube')

ground = Entity(model=Terrain('heightmap_1'),
                scale=(20, 5, 20), texture='heightmap_1')

EditorCamera()
camera.orthographic = True

pivot = Entity()
DirectionalLight(parent=pivot, x=0, y=.15, z=0, shadows=True)


def update():   # update gets automatically called.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['q'] * .1
    player.y += held_keys['z'] * .1
    player.y -= held_keys['s'] * .1

    # et ça tourne tourne toune c'est ta façon  d'aimer.
    player.rotation_y = player.rotation_y + time.dt*100

app.run()   # opens a window and starts the game.
