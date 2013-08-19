from processing import *

from walker import Walker

def setup():
    global walker
    size(640, 360)
    background(255)
    fill(0)
    walker = Walker(width, height)

def draw():
    walker.step()
    point(walker.x, walker.y)

run()
