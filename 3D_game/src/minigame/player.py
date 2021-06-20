import ursina as ur

class Player(ur.Entity):
    def __init__(self):
        super().__init__(model='cube', color=ur.color.pink, on_click=self.mouse_clicked())
        self.collider = 'cube'
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

    def mouse_clicked(self):
        print("Oh u clicked on me !")

    def jmp(self):
        if self.in_air :
            self.y += self.jmp_force * ur.time.dt 
            self.jmp_force -= self.acc
            if self.y <= +.5:
                self.in_air = False
                self.y = +.5
                self.jmp_force = self.base_jmp_force