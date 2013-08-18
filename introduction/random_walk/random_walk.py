from processing import Sketch

from walker import Walker


NUMBER_OF_WALKERS = 10000


class RandomWalkers(Sketch):
    width = 1250
    height = 650
    frame_rate = 30

    def setup(self):
        self.walkers = [Walker(self.width, self.height) for i in range(NUMBER_OF_WALKERS)]

    def draw(self):
        for w in self.walkers:
            w.step()
            self.fill(w.color)
            self.point(w.x, w.y)


if __name__ == '__main__':
    sketch = RandomWalkers()
    sketch.run(port=8888)
