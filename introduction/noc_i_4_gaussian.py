from p5 import *


def setup():
    size(640, 360)
    background(255)

def draw():
    # Get a gaussian number w/ mean of 0 and standard deviation of 1.0
    xloc = randomGaussian()

    sd = 60
    mean = width/2
    xloc = (xloc * sd) + mean

    noStroke()
    fill(0, 10)
    ellipse(xloc, height/2, 16, 16)

run()
