from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import (
    WindowProperties,
    DirectionalLight,
    Vec4,
    Vec3,
    CollisionTraverser,
    CollisionHandlerPusher,
    CollisionSphere,
    CollisionNode,
    CollisionTube,
    LPoint3f
)
from entity import Player, Enemy, Trap

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        properties = WindowProperties()
        properties.setTitle("Wow, a game !")
        properties.setSize(1024, 576)
        self.win.requestProperties(properties)
        # Camera not controlled by the mouse
        self.disable_mouse()
        # .egg is human readable format -> converted to .bam by panda3d
        self.environment = loader.loadModel("Sample_model/Env/environment")
        self.environment.reparentTo(render)
        # Setting camera as 3rd person
        self.camera.setPos(0, -8, 8)
        self.camera.setP(-45)
        # Lighting !
        light = DirectionalLight("main light")
        # Attaching the light to the scene:
        self.light = render.attachNewNode(light)
        self.light.setHpr(45, -45, 0)  # We set the direction we want the light to be
        render.setLight(self.light)
        render.setShaderAuto()
        # Managing events from user
        self.keyBind = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "shoot": False,
        }
        self.accept_key_act()

        # Collision manager
        # Note that the 2 names can't be changed (because its provided globally)
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()
        # pusher  Handle collision when an object try to push through another
        self.pusher.setHorizontal(True) # So the player donc go over wall
        self.init_collision_wall()
        # We create a player
        self.player = Player()
        # Enemies
        self.enemy = Enemy()
        self.trap = Trap()
        self.pusher.add_in_pattern("%fn-into-%in")
        self.accept("trap-into-wall", self.stopTrap)
        self.accept("trap-into-trapEnemy", self.stopTrap)
        self.accept("trap-into-player", self.trapHitsSomething)
        self.accept("trap-into-walkingEnemy", self.trapHitsSomething)
        # Task are routine than can be used several times
        self.updt_task = taskMgr.add(self.update, "update")

    def init_collision_wall(self):
        wall_list = [
            (-8.0, 0, 0, 8.0, 0, 0, 0.2),
            (-8.0, 0, 0, 8.0, 0, 0, 0.2),
            (0, -8.0, 0, 0, 8.0, 0, 0.2),
            (0, -8.0, 0, 0, 8.0, 0, 0.2)
        ]
        wall_pos = [
            (0,8.0,0),(0,-8.0,0),(8.0,0,0),(-8.0,0,0)
        ]
        for w in range(4) :
            solid = CollisionTube(*wall_list[w])
            node = CollisionNode("wall")
            node.addSolid(solid)
            wall = render.attachNewNode(node)   
            wall.setPos(*wall_pos[w])
            wall.show()
        

    def accept_key_act(self):
        # Managing deplacement
        self.accept("z", self.updateKeyMap, ["up", True])
        self.accept("z-up", self.updateKeyMap, ["up", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("q", self.updateKeyMap, ["left", True])
        self.accept("q-up", self.updateKeyMap, ["left", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])
        # Managing action
        self.accept("mouse1", self.updateKeyMap, ["shoot", True])
        self.accept("mouse1-up", self.updateKeyMap, ["shoot", False])

    def updateKeyMap(self, keyBindName, controlState):
        self.keyBind[keyBindName] = controlState

    def update(self, task):
        dt = globalClock.getDt()  # Same use as in ursina
        self.player.update(self.keyBind,self.camera, dt)
        self.enemy.update(self.player.actor, dt)
        self.trap.update(self.player.actor, dt)
        return task.cont  # .cont so we can run the same task several time

    def stopTrap(self, entry):
        coll = entry.getFromNodePath()
        if coll.hasPythonTag("owner"):
            its_a_trap = coll.getPythonTag("owner")
            its_a_trap.movement = 0
            its_a_trap.ignorePlayer = False

    def trapHitsSomething(self, entry):
        coll = entry.getFromNodePath()
        if coll.hasPythonTag("owner"):
            trap = coll.getPythonTag("owner")
            if trap.movement == 0:
                return
            coll = entry.getIntoNodePath()
            if coll.hasPythonTag("owner"):
                obj = coll.getPythonTag("owner")
                if isinstance(obj, Player):
                    if not trap.ignorePlayer:
                        obj.updt_Health(-1)
                        trap.ignorePlayer = True
                else:
                    obj.updt_Health(-10)

app = Game()
app.run()
