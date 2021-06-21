import ursina as ur
from ursina import duplicate
from ursina.texture_importer import load_texture


class Player(ur.Entity):
    def __init__(self):
        super().__init__(model="cube", scale=(1, 1, 0.9), texture="pink_shirt.png")
        self.leg = ur.Entity(model="sphere", scale=0.9, texture="wheel.png")
        self.arms = [
            ur.Entity(
                model="cube", scale=(0.2, 0.75, 0.2), rotation_z=15, texture="skin.png"
            ),
            ur.Entity(
                model="cube", scale=(0.2, 0.75, 0.2), rotation_z=-15, texture="skin.png"
            ),
        ]
        self.hands = [
            ur.Entity(model="sphere", scale=0.25, rotation_z=15, texture="skin.png"),
            ur.Entity(model="sphere", scale=0.25, rotation_z=-15, texture="skin.png"),
        ]
        h=  ur.Entity(model='cube', scale=(1,0.1,1), color=ur.color.black)
        self.hair = [
            h, duplicate(h, rotation_z=95), duplicate(h, rotation_z=-95), duplicate(h, rotation_x=90)
        ]
        print("-----------------------------",self.hair)
        self.head = ur.Entity(model="cube", texture=load_texture("face.png"))
        self.children.append(self.leg)
        self.children.extend(self.arms)
        self.children.extend(self.hands)
        self.collider = "cube"
        self.colliders = []
        self.collider.show()
        self.y += 3
        self.in_air = True
        self.base_jmp_force = 8
        self.jmp_force = self.base_jmp_force
        self.acc = 1 / 3

    def update(self):
        self.direction = ur.Vec3(
            self.forward * (ur.held_keys["z"] - ur.held_keys["s"])
            + self.right * (ur.held_keys["d"] - ur.held_keys["q"])
        ).normalized()
        self.jmp()

        # Here we gonna use raycast to manage collision
        origin = self.world_position + (0, 0.1, 0)
        hit_info = ur.boxcast(
            origin,
            self.direction,
            thickness=(1, 0.8),
            ignore=(self,),
            distance=0.5,
            debug=True,
        )
        if not hit_info.hit:
            self.position += self.direction * 5 * ur.time.dt
            if self.direction != ur.Vec3(0, 0, 0):
                self.leg.rotation += (
                    self.direction[2] * 160 * ur.time.dt,
                    0,
                    self.direction[0] * 160 * ur.time.dt,
                )
                #self.updt_limb_facing()
        self.updt_limb()

    def jmp(self):
        if self.in_air:
            self.y += self.jmp_force * ur.time.dt
            self.jmp_force -= self.acc
            if self.y <= +1:
                self.in_air = False
                self.y = +1
                self.jmp_force = self.base_jmp_force

    def updt_limb(self):
        self.leg.position = self.position + ur.Vec3(0, -0.5, 0)
        self.arms[0].position = self.position + ur.Vec3(-0.65, 0, 0)
        self.arms[1].position = self.position + ur.Vec3(+0.65, 0, 0)
        self.hands[0].position = self.position + ur.Vec3(-0.75, -0.4, 0)
        self.hands[1].position = self.position + ur.Vec3(+0.75, -0.4, 0)
        self.head.position = self.position + ur.Vec3(0, +1, 0)
        self.hair[0].position =self.position + ur.Vec3(0, +1.55, 0)
        self.hair[1].position = self.position + ur.Vec3(-0.60, +1.1, 0)
        self.hair[2].position = self.position + ur.Vec3(0.60, +1.1, 0)
        self.hair[3].position = self.position + ur.Vec3(0, +1.1, -0.5)

    def updt_limb_facing(self):
        """Use the self.direction to update the direction where limbs are facing"""
        print(self.direction)
        rotate = 0
        dir_x = self.direction[0]
        dir_z = self.direction[2]
        if dir_x>0 and dir_z>0:
            rotate = 45
        elif dir_x<0 and not dir_z<0:
            rotate = -45
        self.head.rotation_y = rotate
        for h in self.hair :
            h.rotation_y =rotate