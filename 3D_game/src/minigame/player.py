import ursina as ur

class Player(ur.Entity):
    def __init__(self):
        super().__init__(model='cube', texture='pink_shirt.png')
        self.leg = ur.Entity(model='sphere', color=ur.color.pink, texture='wheel.png')
        self.children.append(self.leg)
        self.collider = 'cube'
        self.colliders = []
        self.collider.show()
        self.y += 3
        self.in_air = True
        self.base_jmp_force = 8
        self.jmp_force = self.base_jmp_force
        self.acc = 1/3
    
    def update(self):
        self.direction = ur.Vec3(
            self.forward * (ur.held_keys['z'] - ur.held_keys['s'])
            + self.right * (ur.held_keys['d'] - ur.held_keys['q'])
            ).normalized()
        self.jmp()

        #Here we gonna use raycast to manage collision
        origin = self.world_position + (0,0.1,0)
        hit_info = ur.boxcast(origin , self.direction, thickness=(1,0.8), ignore=(self,), distance=.5, debug=True)
        if not hit_info.hit:
            self.position += self.direction * 5 * ur.time.dt
            self.leg.rotation_z += 60 *ur.time.dt
        self.updt_members()

    def jmp(self):
        if self.in_air :
            self.y += self.jmp_force * ur.time.dt
            self.jmp_force -= self.acc
            if self.y <= +1:
                self.in_air = False
                self.y = +1
                self.jmp_force = self.base_jmp_force
    
    def updt_members(self):
        self.leg.position = self.position + ur.Vec3(0,-.5,0)