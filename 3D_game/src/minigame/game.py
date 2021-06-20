import ursina as ur
from player import Player

app = ur.Ursina()


title = ur.Text(text='Welcome to the game !', origin=(0,-19))

player = Player()

# A thing to go with player that will shout listen every 2 microsecond
tv = ur.Entity(model='sphere', texture="../asset/video.mp4", scale=0.4, parent=player, origin=(1.5,-2,1.5))
# A surface ?
ground = ur.Entity(model=ur.Grid(25,25), scale=50, rotation_x=-90, texture='brick', color=ur.color.orange)
wall = ur.Entity(model='cube', collider='box', scale_y=3, origin_y=-.5, color=ur.color.azure, x=-4)
ground.collider='box'
ground.collider.show()


ur.EditorCamera()
ur.camera.y = 2

def update():   # update gets automatically called.
    player.update()
    # We want the sphere to revolve 
    tv.rotation_y += 60 * ur.time.dt
    

def input(key):
    if key == 'b':
        tv.fade_out()
    elif key =='n':
        tv.fade_in()
    elif key=='space':
        player.in_air = True

app.run()   # opens a window and starts the game.