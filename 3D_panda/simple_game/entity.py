from direct.actor.Actor import Actor
from panda3d.core import Vec3, CollisionNode, CollisionSphere
FRICTION = 110.0

class Entity():
    def __init__(self, pos, modelType, animation, maxHealth, maxSpeed, colliderName):
        self.actor = Actor(modelType, animation)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)
        self.actor.setScale(0.75)
        # Self data
        self.m_health = maxHealth
        self.health = maxHealth 
        # movement management
        self.m_speed = maxSpeed
        self.velocity = Vec3(0,0,0)
        self.acceleration = 300.0
        self.walking = False
        # Collider
        c_node = CollisionNode(colliderName)
        c_node.addSolid(CollisionSphere(0,0,0,0.3))
        self.collider = self.actor.attachNewNode(c_node)
        self.collider.show()
        # Setting a tag so it's easy to get back to the object when a collision occurs
        self.collider.setPythonTag('owner',self)

    def update(self, dt):
        i_am_speed = self.velocity.length()
        if i_am_speed > self.m_speed :
            self.velocity.normalize()
            self.velocity *= self.m_speed
            i_am_speed = self.m_speed
        if not self.walking :
            fric = FRICTION * dt
            if fric > i_am_speed:
                self.velocity.set(0,0,0)
            else : 
                fricVec = -self.velocity
                fricVec.normalize() 
                fricVec *= fric
                self.velocity += fricVec
        self.actor.setPos(self.actor.getPos() + self.velocity*dt)
            

    def updt_Health(self, delta):
        self.health = max(0, min(self.m_health, self.health+delta))

    def clean(self):
        if self.collider is not None and not self.collider.isEmpty():
            self.collider.clearPythonTag('owner')
            base.cTrav.removeCollider(self.collider)
            base.pusher.removeCollider(self.collider)
        if self.actor :
            self.actor.cleanup()
            self.actor.removeNode()
            self.actor = None
        self.collider = None

class Player(Entity):
    def __init__(self):
        Entity.__init__(self, Vec3(0,0,0),"Sample_model/p3d/models/act_p3d_chan",
                              {
                                  "idle" : "Sample_model/p3d/models/a_p3d_chan_idle",
                                  "walk" : "Sample_model/p3d/models/a_p3d_chan_run",
                              },
                            5,
                            10,
                            "player")
        self.actor.getChild(0).setH(180) #facing is the wrong way
        base.pusher.addCollider(self.collider, self.actor)
        base.cTrav.addCollider(self.collider, base.pusher)
        self.actor.loop("idle")

    def update(self, keys, camera, dt):
        Entity.update(self, dt)
        camera.setPos(camera.getPos() + self.velocity*dt)
        self.walking = False
        key_act = {
            "up": Vec3(0,self.acceleration*dt, 0),
            "down": Vec3(0, -self.acceleration*dt, 0),
            "left": Vec3(-self.acceleration*dt, 0, 0),
            "right": Vec3(self.acceleration*dt, 0, 0)
        }
        for k in key_act.keys():
            if keys[k]:
                self.walking = True
                self.velocity += key_act[k]
        if keys["shoot"]:
            print("Zap!")

        #Animation
        if self.walking:
            idleControl = self.actor.getAnimControl("idle")
            if idleControl.isPlaying():
                idleControl.stop()
            walkControl = self.actor.getAnimControl("walk")
            if not walkControl.isPlaying():
                self.actor.loop("walk")
        else:
            idleControl = self.actor.getAnimControl("idle")
            if not idleControl.isPlaying():
                self.actor.stop("walk")
                self.actor.loop("idle")

class Enemy(Entity):
    def __init__(self):
        Entity.__init__(self, Vec3(5,5,0),"Sample_model/SimpleEnemy/simpleEnemy",
                              {
                                  "spawn" : "Sample_model/SimpleEnemy/simpleEnemy-spawn",
                                  "stand" : "Sample_model/SimpleEnemy/simpleEnemy-stand",
                                  "walk" : "Sample_model/SimpleEnemy/simpleEnemy-walk",
                              },
                            4,
                            8,
                            "enemy")
        self.value = 1
        self.acceleration = 150.0
        base.pusher.addCollider(self.collider, self.actor)
        base.cTrav.addCollider(self.collider, base.pusher)
        self.actor.loop("stand")

    def update(self, player, dt):
        Entity.update(self, dt)
        self.act(player, dt)
        #Animation
        if self.walking:
            idleControl = self.actor.getAnimControl("idle")
            if idleControl.isPlaying():
                idleControl.stop()
            walkControl = self.actor.getAnimControl("walk")
            if not walkControl.isPlaying():
                self.actor.loop("walk")
        else:
            idleControl = self.actor.getAnimControl("idle")
            if not idleControl.isPlaying():
                self.actor.stop("walk")
                self.actor.loop("idle")
    
    def act(self, player, dt):
        pass