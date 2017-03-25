from random import choice

from p5 import *


class Walker(object):
    def __init__(self):
        self.location = PVector(width/2, height/2)
        self.noff = PVector(random(1000), random(1000))

    def walk(self):
        self.location.x = map(noise(self.noff.x), 0, 1, 0, width)
        self.location.y = map(noise(self.noff.y), 0, 1, 0, height)
        self.noff.add(0.01, 0.01, 0)

    def display(self):
        strokeWeight(2)
        fill(127)
        stroke(0)
        ellipse(self.location.x, self.location.y, 48, 48)

