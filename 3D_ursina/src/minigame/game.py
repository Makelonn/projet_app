import ursina as ur
from ursina.collider import BoxCollider
from player import Player

app = ur.Ursina()


title = ur.Text(text='Welcome to the game !', origin=(0,-19))

player = Player()

# A thing to go with player that will shout listen every 2 microsecond
tv = ur.Entity(model='sphere', texture="../asset/video.mp4", scale=0.4, parent=player, origin=(2,-2,2))
# A surface ?
ground = ur.Entity(model=ur.Grid(25,25), collider='box', scale=50, rotation_x=-90, texture='brick', color=ur.color.orange)
wall = ur.Entity(model='cube', scale_y=3, origin_y=-.5, color=ur.color.azure, x=-4)

wall.collider = BoxCollider(wall, center=ur.Vec3(0,+.5,0))
wall.collider.show()


ur.EditorCamera()

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