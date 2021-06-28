from direct.actor.Actor import Actor
from random import getrandbits
from math import copysign
from panda3d.core import Vec3, Vec2, CollisionNode, CollisionSphere
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
        self.velocity = Vec3(0, 0, 0)
        self.acceleration = 150.0
        self.walking = False
        # Collider
        c_node = CollisionNode(colliderName)
        c_node.addSolid(CollisionSphere(0, 0, 0, 0.3))
        self.collider = self.actor.attachNewNode(c_node)
        base.pusher.addCollider(self.collider, self.actor)
        base.cTrav.addCollider(self.collider, base.pusher)
        self.collider.show()
        # Setting a tag so it's easy to get back to the object when a collision occurs
        self.collider.setPythonTag('owner', self)

    def update(self, dt):
        i_am_speed = self.velocity.length()
        if i_am_speed > self.m_speed:
            self.velocity.normalize()
            self.velocity *= self.m_speed
            i_am_speed = self.m_speed
        if not self.walking:
            fric = FRICTION * dt
            if fric > i_am_speed:
                self.velocity.set(0, 0, 0)
            else:
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
        if self.actor:
            self.actor.cleanup()
            self.actor.removeNode()
            self.actor = None
        self.collider = None


class Player(Entity):
    def __init__(self):
        Entity.__init__(self, Vec3(0, 0, 0), "Sample_model/p3d/models/act_p3d_chan",
                        {
            "idle": "Sample_model/p3d/models/a_p3d_chan_idle",
            "walk": "Sample_model/p3d/models/a_p3d_chan_run",
        },
            5,
            10,
            "player")
        self.actor.loop("idle")

    def update(self, keys, camera, dt):
        Entity.update(self, dt)
        self.walking = False
        key_act = {
            "up": Vec3(0, self.acceleration*dt, 0),
            "down": Vec3(0, -self.acceleration*dt, 0),
            "left": Vec3(-self.acceleration*dt, 0, 0),
            "right": Vec3(self.acceleration*dt, 0, 0)
        }
        key_facing = {
            "up": 180, "down": 0, "left": 270, "right": 90
        }
        for k in key_act.keys():
            if keys[k]:
                self.walking = True
                self.velocity += key_act[k]
                self.actor.getChild(0).setH(key_facing[k])
        if keys["shoot"]:
            print("Zap!")
        camera.setX(self.actor.getX())
        camera.setY(self.actor.getY()-8)
        # Animation
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
        Entity.__init__(self, Vec3(5, 5, 0), "Sample_model/SimpleEnemy/simpleEnemy",
                        {
            "spawn": "Sample_model/SimpleEnemy/simpleEnemy-spawn",
            "stand": "Sample_model/SimpleEnemy/simpleEnemy-stand",
            "walk": "Sample_model/SimpleEnemy/simpleEnemy-walk",
        },
            4,
            8,
            "enemy")
        self.value = 1
        self.acceleration = 75.0
        self.attack_distance = 1
        self.detect_distance = 3
        self.actor.loop("stand")

    def update(self, p_actor, dt):
        Entity.update(self, dt)
        self.act(p_actor, dt)
        # Animation
        if self.walking:
            walkControl = self.actor.getAnimControl("walk")
            if not walkControl.isPlaying():
                self.actor.loop("walk")
        else:
            spawnControl = self.actor.getAnimControl("spawn")

            if spawnControl is None or not spawnControl.isPlaying():
                standControl = self.actor.getAnimControl("stand")
                if not standControl.isPlaying():
                    self.actor.stop("walk")
                    self.actor.loop("stand")

    def act(self, p_actor, dt):
        v_toPlayer3 = p_actor.getPos()-self.actor.getPos()
        v_toPlayer2 = v_toPlayer3.getXy()
        distancePlayer = v_toPlayer2.length()
        if not distancePlayer > self.detect_distance:
            self.actor.setH(Vec2(0, 1).signedAngleDeg(v_toPlayer2))
            if distancePlayer > self.attack_distance:
                self.walking = True
                v_toPlayer3.setZ(0)
                v_toPlayer3.normalize()
                self.velocity += v_toPlayer3*self.acceleration*dt
            else:
                # Attacking ?
                self.walking = False
                self.velocity.set(0, 0, 0)
        else:
            self.walking = False
            self.velocity.set(0, 0, 0)


class Trap(Entity):
    def __init__(self):
        Entity.__init__(self, Vec3(-2, 7, 0),
                        "Sample_model/SlidingTrap/trap",
                        {
            "walk": "Sample_model/SlidingTrap/trap-walk",
            "stand": "Sample_model/SlidingTrap/trap-stand"
        },
            100.0,
            10.0,
            "trap"
        )
        self.value = 1
        self.acceleration = 100.0
        self.detect_distance = 0.5
        self.walking = False
        self.ignorePlayer = False
        self.movement = 0
        self.movingAlongX = bool(getrandbits(1))

    def update(self, p_actor, dt):
        Entity.update(self, dt)
        self.act(p_actor, dt)
        if self.walking:
            walkingControl = self.actor.getAnimControl("walk")
            if not walkingControl.isPlaying():
                self.actor.loop("walk")
        else:
            spawnControl = self.actor.getAnimControl("spawn")
            if spawnControl is None or not spawnControl.isPlaying():
                attackControl = self.actor.getAnimControl("attack")
                if attackControl is None or not attackControl.isPlaying():
                    standControl = self.actor.getAnimControl("stand")
                    if not standControl.isPlaying():
                        self.actor.loop("stand")

    def act(self, p_actor, dt):
        if self.movement != 0:
            self.walking = True
            if self.movingAlongX:
                self.velocity.addX(self.movement*self.acceleration*dt)
            else:
                self.velocity.addY(self.movement*self.acceleration*dt)
        else:
            self.walking = False
            v_toPlayer = (p_actor.getPos() - self.actor.getPos()).getXy()
            if self.movingAlongX:
                detect = v_toPlayer.y
                move = v_toPlayer.x
            else:
                detect = v_toPlayer.x
                move = v_toPlayer.y
            if abs(detect) < 0.5:
                self.movement = copysign(1, move)
