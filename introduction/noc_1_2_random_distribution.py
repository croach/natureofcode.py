from random import randint

from processing import *


random_counts = [0]*20

def setup():
    global random_counts
    size(640, 240)

def draw():
    background(255)
    
    idx = randint(0, len(random_counts)-1)
    random_counts[idx] += 1
    
    stroke(0)
    fill(175)
    w = width/len(random_counts)
    for i in range(len(random_counts)):
        rect(i * w, height - random_counts[i], w - 1, random_counts[i])

run()
