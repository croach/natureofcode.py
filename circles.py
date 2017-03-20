from processing import *


def setup():
    size(600, 400)
    frameRate(1)
    background(200)

def draw():
    stroke(random(255))
    strokeWeight(random(10))
    fill(random(255))
    diam = random(100)
    x = random(width)
    y = random(height)
    ellipse(x, y, diam, diam)

run()
