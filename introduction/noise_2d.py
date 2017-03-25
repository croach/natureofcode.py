# from p5 import *


# increment = 0.02

# def setup():
#     size(800,200)
#     # noLoop()

# def draw():
#     background(0)

#     # Optional: adjust noise detail here
#     # noiseDetail(8,0.65f)

#     # loadPixels()

#     xoff = 0.0 # Start xoff at 0

#     # For every x,y coordinate in a 2D space, calculate a noise value and produce a brightness value
#     for x in range(width):
#         xoff += increment
#         yoff = 0.0
#         for y in range(height):
#             yoff += increment

#             # Calculate noise and scale by 255
#             bright = noise(xoff, yoff) * 255

#             # Try using this line instead
#             #bright = random(0,2 55)

#             # # Set each pixel onscreen to a grayscale value
#             # pixels[x+y*width] = color(bright)
#             fill(bright)
#             rect(x, y, 1, 1)

#     # updatePixels()

# run()


from p5 import *

increment = 0.02
xoff = 0.0
granularity = 10

def setup():
    size(800,200)
    # noLoop()


def draw():

    background(0)

    # Optional: adjust noise detail here
    # noiseDetail(8,0.65f)

    # loadPixels()

    # xoff = 0.0 # Start xoff at 0

    global xoff
    noStroke()

    # For every x,y coordinate in a 2D space, calculate a noise value and produce a brightness value
    for x in range(0, width, granularity):
        xoff += increment
        yoff = 0.0
        for y in range(0, height, granularity):
            yoff += increment

            # Calculate noise and scale by 255
            bright = noise(xoff, yoff) * 255

            # Try using this line instead
            #bright = random(0,2 55)

            # # Set each pixel onscreen to a grayscale value
            # pixels[x+y*width] = color(bright)
            fill(int(round(bright)))
            rect(x, y, granularity, granularity)

    # updatePixels()

run()
