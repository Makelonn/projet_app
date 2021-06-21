from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import WindowProperties

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        properties = WindowProperties()
        properties.setTitle('Wow, a game !')
        properties.setSize(1024,576)
        self.win.requestProperties(properties)
        # Camera not controlled by the mouse
        self.disable_mouse()
        # .egg is human readable format -> converted to .bam by panda3d
        self.environment = loader.loadModel("Sample_model/Env/environment")
        self.environment.reparentTo(render)


app = Game()
app.run()