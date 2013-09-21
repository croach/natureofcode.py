from processing import *


x = 100
y = 100
xspeed = 2.5
yspeed = 2


def setup():
    size(800, 200)


def draw():
    global x, y, xspeed, yspeed

    background(255)

    # Add the current speed to the location
    x += xspeed
    y += yspeed

    # Reverse the direction if we've reached a boundary
    xspeed = -xspeed if x > width or x < 0 else xspeed
    yspeed = -yspeed if y > height or y < 0 else yspeed

    # Display the circle at x,y location
    stroke(0)
    strokeWeight(2)
    fill(127)
    ellipse(x, y, 48, 48)

run()
