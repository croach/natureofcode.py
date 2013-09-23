from processing.sketch import Sketch
from processing.server import SketchApplication

from walker import Walker


class RandomWalker(Sketch):
    width = 800
    height = 200

    def setup(self):
        self.walker = Walker(self)
        self.background(255)

    def draw(self):
        self.walker.step()
        self.walker.render()


if __name__ == '__main__':
    SketchApplication(RandomWalker, port=8888).run()
