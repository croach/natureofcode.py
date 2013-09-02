from random import randint

from processing import *


def setup():
    global random_counts
    size(800, 200)
    random_counts = [0]*20

def draw():
    background(255)

    # Pick a number and increase its count
    index = randint(0, len(random_counts)-1)
    random_counts[index] += 1

    # Draw a rectangle to graph results
    stroke(0)
    strokeWeight(2)
    fill(127)

    w = width/len(random_counts)

    for x in range(len(random_counts)):
        rect(x*w, height - random_counts[x], w-1, random_counts[x])

run()
