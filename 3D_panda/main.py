import panda3d as pa
from direct.showbase.ShowBase import ShowBase

class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

app = Main()
app.run()