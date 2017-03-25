from p5 import *

from walker import Walker


def setup():
    global walker
    size(800, 200)
    background(255)
    walker = Walker()

def draw():
    walker.step()
    walker.render()

run()
