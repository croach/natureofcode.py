"""The Random Walker from The Nature of Code, Introduction
"""

from processing import constrain

from random import choice, randint


class Walker(object):
    def __init__(self, sketch):
        self.sketch = sketch
        self.x = self.sketch.width/2
        self.y = self.sketch.height/2
        self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]

    @property
    def position(self):
        return {'x': self.x, 'y': self.y}

    def step(self):
        direction = choice(['left', 'right', 'forward', 'backward'])
        if direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'forward':
            self.y += 1
        elif direction == 'backward':
            self.y -= 1

        self.x = constrain(self.x, 0, self.sketch.width-1)
        self.y = constrain(self.y, 0, self.sketch.height-1)

    def render(self):
        self.sketch.stroke(0);
        self.sketch.point(self.x, self.y)
