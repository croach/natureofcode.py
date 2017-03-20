from processing import *

def setup():
    size(640, 360)

def draw():
    background(255)

    mouse = PVector(mouseX, mouseY)
    center = PVector(width/2, height/2)
    mouse -= center

    translate(width/2, height/2)
    line(0, 0, mouse.x, mouse.y)

run()