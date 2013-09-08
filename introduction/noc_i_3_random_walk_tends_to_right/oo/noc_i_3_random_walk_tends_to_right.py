from processing.sketch import Sketch

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
    sketch = RandomWalker()
    sketch.run(port=8888)
