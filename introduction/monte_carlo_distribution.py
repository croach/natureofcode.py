from p5 import *


size(200, 200)
vals = [0] * width    # Array to count how often a random number is picked
norms = [0] * width   # Normalized version of above


def draw():
    background(100)

    # Pick a random number between 0 and 1 based on custom probability function
    n = montecarlo()

    # What spot in the array did we pick
    index = int(n*width)
    vals[index] += 1
    stroke(255)

    normalization = False
    maxy = 0

    # Draw graph based on values in norms array
    # If a value is greater than the height, set normalization to true
    for x in xrange(len(vals)):
        line(x, height, x, height-norms[x])
        if vals[x] > height: normalization = True
        if vals[x] > maxy: maxy = vals[x]

    # If normalization is true then normalize to height
    # Otherwise, just copy the info
    for x in xrange(len(vals)):
        if normalization:
            norms[x] = (vals[x] / float(maxy)) * height
        else:
            norms[x] = vals[x]


# An algorithm for picking a random number based on monte carlo method
# Here probability is determined by formula y = x
def montecarlo():
    # Limit the number of iterations to make sure we don't get stuck in an infinite loop
    for i in xrange(10000):
        # Pick two random numbers
        r1 = random(1)
        r2 = random(1)
        y = r1*r1  # y = x*x (change for different results)

        # If r2 is valid, we'll use this one
        if r2 < y:
            return r1

    # Hack in case we run into a problem (need to improve this)
    return 0

run()
