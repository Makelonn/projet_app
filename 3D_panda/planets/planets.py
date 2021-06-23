from direct.directbase import DirectStart
from panda3d.ode import OdeWorld, OdeBody, OdeMass
from panda3d.core import Quat

# Load the cube where the ball will fall from
# cube = loader.loadModel("box.egg")
# cube.reparentTo(render)
# # cube.setColor(0.2, 0, 0.7)
# cube.setScale(20)

# Load the smiley model which will act as our iron ball
sphere = loader.loadModel("jack.egg")
sphere.reparentTo(render)
sphere.setPos(10, 1, 21)
sphere.setScale(5)
# sphere.setColor(0.7, 0.4, 0.4)

# Setup our physics world and the body
world = OdeWorld()
world.setGravity(0, 0, -9.81)
body = OdeBody(world)
M = OdeMass()
# M.setSphere(7874, 1.0)
# body.setMass(M)
# body.setPosition(sphere.getPos(render))
# body.setQuaternion(sphere.getQuat(render))

# Set the camera position
base.disableMouse()
base.camera.setPos(80, -20, 40)
base.camera.lookAt(0, 0, 10)

base.run()
