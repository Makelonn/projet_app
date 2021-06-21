from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
window.title = 'My fucking game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
# Do not show the in-game red X that loses the window
window.exit_button.visible = False
# Show the FPS (Frames per second) counter
window.fps_counter.enabled = True

# root_folder = Path(__file__).parent.parent
# asset_folder = root_folder / 'asset/'
# texture_folder = asset_folder / 'texture/'

# station_folder = asset_folder / 'station_spatiale/'

# EditorCamera()
# camera.orthographic = True
# camera.z += 40

# player = FirstPersonController()
# player.x = 100
# player.y = 50
# player.z = 50

# print("\n\n station folder :", station_folder)

# level = load_blender_scene('Space_Station_Scene',
#                            path=station_folder)


# def update():   # update gets automatically called.
#     camera.x += held_keys['d'] * .1
#     camera.x -= held_keys['q'] * .1
#     camera.y += held_keys['z'] * .1
#     camera.y -= held_keys['s'] * .1
#     camera.z += held_keys['r'] * .1
#     camera.z -= held_keys['f'] * .1
#     player.x += held_keys['d'] * .1
#     player.x -= held_keys['q'] * .1
#     player.y += held_keys['z'] * .1
#     player.y -= held_keys['s'] * .1
#     player.z += held_keys['r'] * .10
#     player.z -= held_keys['f'] * .10
camera.orthographic = True
camera.fov = 10

ground = Entity(model='cube', color=color.white33,
                origin_y=.5, scale=(20, 10, 1), collider='box')
wall = Entity(model='cube', color=color.azure, origin=(-.5, .5),
              scale=(5, 10), x=10, y=.5, collider='box')
wall_2 = Entity(model='cube', color=color.white33,
                origin=(-.5, .5), scale=(5, 10), x=10, y=5, collider='box')
ceiling = Entity(model='cube', color=color.white33,
                 origin_y=-.5, scale=(1, 1, 1), y=1, collider='box')


def input(key):
    if key == 'c':
        wall.collision = not wall.collision
        print(wall.collision)


player_controller = PlatformerController2d(scale_y=2, jump_height=4, x=3)
camera.add_script(SmoothFollow(
    target=player_controller, offset=[0, 1, -30], speed=4))

EditorCamera()


app.run()   # opens a window and starts the game.
