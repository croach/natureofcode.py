from p5 import *

from walker import Walker

w = Walker()

def setup():
    size(800, 200)
    frameRate(30)

def draw():
    background(255);
    w.walk()
    w.display()

run()
