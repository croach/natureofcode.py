"""The Random Walker from The Nature of Code, Introduction
"""

from processing.utils import constrain, random


class Walker(object):
    def __init__(self, sketch):
        self.sketch = sketch
        self.x = self.sketch.width/2
        self.y = self.sketch.height/2

    def step(self):
        r = random(1)
        if r < 0.4:
            self.x += 1
        elif r < 0.6:
            self.x -= 1
        elif r < 0.8:
            self.y += 1
        else:
            self.y -= 1

        self.x = constrain(self.x, 0, self.sketch.width-1)
        self.y = constrain(self.y, 0, self.sketch.height-1)


    def render(self):
        self.sketch.stroke(0);
        self.sketch.point(self.x, self.y)
