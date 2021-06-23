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
    CollisionTube
)


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
        # Actor = animated model
        self.myActor = Actor(
            "Sample_model/p3d/models/act_p3d_chan",
            {"idle": "Sample_model/p3d/models/a_p3d_chan_idle"},
        )
        self.myActor.reparentTo(render)
        # No we set position and camera : setPos, setScale, setHpr (rotation) can be usefull
        self.myActor.setY(0)
        self.myActor.setScale(0.75)
        self.myActor.loop("idle")
        # Setting camera as 3rd person
        self.camera.setPos(0, -8, 8)
        self.camera.setP(-45)
        # Lighting !
        light = DirectionalLight("main light")
        # Attaching the light to the scene:
        self.light = render.attachNewNode(light)
        # We set the direction we want the light to be
        self.light.setHpr(45, -45, 0)
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
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()
        # pusher  Handle collision when an object try to push through another
        # Now we create a collider for our player (we gonna use a sphere)
        colliderN = CollisionNode("player")
        colliderN.addSolid(CollisionSphere(0, 0, 0, 0.3))
        collider = self.myActor.attachNewNode(colliderN)
        collider.show()
        self.pusher.setHorizontal(True)  # So the player donc go over wall
        base.pusher.addCollider(collider, self.myActor)
        base.cTrav.addCollider(collider, self.pusher)
        self.init_collision_wall()

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
            (0, 8.0, 0), (0, -8.0, 0), (8.0, 0, 0), (-8.0, 0, 0)
        ]
        for w in range(4):
            solid = CollisionTube(*wall_list[w])
            node = CollisionNode("wall")
            node.addSolid(solid)
            wall = render.attachNewNode(node)
            wall.setPos(*wall_pos[w])

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
        key_act = {
            "up": Vec3(0, 5.0 * dt, 0),
            "down": Vec3(0, -5.0 * dt, 0),
            "left": Vec3(-5.0 * dt, 0, 0),
            "right": Vec3(5.0 * dt, 0, 0),
        }
        for k in key_act.keys():
            if self.keyBind[k]:
                self.myActor.setPos(self.myActor.getPos() + key_act[k])
                self.camera.setPos(self.camera.getPos() + key_act[k])
        if self.keyBind["shoot"]:
            print("Zap!")

        return task.cont  # .cont so we can run the same task several time


app = Game()
app.run()
