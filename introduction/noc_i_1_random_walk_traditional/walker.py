from random import choice, randint

from processing import *


class Walker(object):
    def __init__(self, width, height):
        # self.width = width
        # self.height = height
        self.x = width/2
        self.y = height/2
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

        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)

    def render(self):
        stroke(0);
        point(self.x, self.y)
