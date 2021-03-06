"""The Random Walker from The Nature of Code, Introduction
"""

from random import choice

from processing.mathfuncs import constrain


class Walker(object):
    def __init__(self, sketch):
        self.sketch = sketch
        self.x = self.sketch.width/2
        self.y = self.sketch.height/2

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
