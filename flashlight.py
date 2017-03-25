from p5 import *


def setup():
    size(400, 400)
    noStroke()


def draw():
    background(230)
    step = 50
    for i in range(0, width + step, step):
        for j in range(0, height + step, step):
            diameter = dist(mouseX, mouseY, i, j)/3.3
            fill(0, diameter*4)
            ellipse(i, j, diameter, diameter)


run()
