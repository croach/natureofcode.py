from p5 import *


class Walker(object):
    def __init__(self):
        self.x = width/2
        self.y = height/2

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

        self.x = constrain(self.x, 0, width-1)
        self.y = constrain(self.y, 0, height-1)

    def render(self):
        stroke(0);
        point(self.x, self.y)
