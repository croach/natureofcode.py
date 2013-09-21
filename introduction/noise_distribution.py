from processing import *


size(300, 20)
xoff = 0.0
vals = [0] * width
norms = [0] * width


# def setup():
#     global vals, norms
#     size(300, 200)
#     vals = [0] * width
#     norms = [0] * width


def draw():
    global xoff, vals, norms
    background(100)
    index = int(noise(xoff)*width)
    vals[index] += 1
    xoff += 0.01
    stroke(255)
    normalization = False
    maxy = 0


    for x in range(len(vals)):
        line(x, height, x, height - norms[x])
        if vals[x] > height:
            normalization = True
        maxy = vals[x] if vals[x] > maxy else maxy

    # Normalize the data, if needed
    if normalization:
        norms = [(val_x/float(maxy)) * height for val_x in vals]
    else:
        norms = vals

run()
