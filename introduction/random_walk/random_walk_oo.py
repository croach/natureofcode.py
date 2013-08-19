"""The Random Walker from The Nature of Code, Introduction (1.2)
"""
from processing.sketch import Sketch

from walker import Walker


class RandomWalkers(Sketch):
    width = 640
    height = 360

    def setup(self):
        self.walker = Walker(self.width, self.height)

    def draw(self):
        self.walker.step()
        self.fill(0)
        self.point(self.walker.x, self.walker.y)


if __name__ == '__main__':
    sketch = RandomWalkers()
    sketch.run(port=8888)
