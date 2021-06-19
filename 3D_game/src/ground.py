from ursina import *

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

station_folder = asset_folder / 'station_spatiale/'

EditorCamera()
camera.orthographic = True

print("\n\n station folder :", station_folder)

level = load_blender_scene('Space_Station_Scene',
                           path=station_folder)

app.run()   # opens a window and starts the game.
