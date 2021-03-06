from random import choice

from p5 import *


class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2

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
