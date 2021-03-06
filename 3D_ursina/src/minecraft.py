'''
Disclaimer: This solution is not scalable for creating a big world.
Creating a game like Minecraft requires specialized knowledge and is not as easy
to make as it looks.
You'll have to do some sort of chunking of the world and generate a combined mesh
instead of separate blocks if you want it to run fast. You can use the Mesh class for this.
You can then use blocks with colliders like in this example in a small area
around the player so you can interact with the world.
'''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position +
                              mouse.normal)
                # voxel.collider = MeshCollider(
                #     voxel, mesh=voxel.model, center=Vec3(self.position + mouse.normal))

            if key == 'right mouse down':
                destroy(self)


for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x, 0, z))
        voxel = Voxel(position=(-x, 0, z))
        voxel = Voxel(position=(x, 0, -z))
        voxel = Voxel(position=(-x, 0, -z))

root_folder = Path(__file__).parent.parent
asset_folder = root_folder / 'asset/'
texture_folder = asset_folder / 'texture/'

my_texture = load_texture("Chair.png", path=texture_folder)
chair_model = load_model('Office_Chair.blend', path=asset_folder)

chair = Entity(model=chair_model, texture=my_texture,
               collider='box', position=Vec3(1, 1, 1), scale=1)

player = FirstPersonController(speed=10)

app.run()
