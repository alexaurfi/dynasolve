import pyglet
import dyna.world as wd

class DynaScene:
    def __init__(self, world : wd.World):
        self.size = (200,200)
        self.center = (self.size[0]/2, self.size[1]/2)
        self.scale  =  (10.0,10.0)
        self.window = pyglet.window.Window(self.size[0],self.size[1], "animation")
        self.batch = pyglet.graphics.Batch()
        self.world = world

        @self.window.event
        def on_draw():
            self.batch.draw()
        
    def run(self):
        pyglet.app.run()