from processing import *


location = PVector(100, 100)
velocity = PVector(2.5, 5)

def setup():
    size(200, 200)
    background(255)

def draw():
    global location

    noStroke()
    fill(255, 10)
    rect(0, 0, width, height)

    # Add the current speed to the location
    location += velocity

    # Reverse the direction if we've hit a boundary
    velocity.x = -velocity.x if location.x > width or location.x < 0 else velocity.x
    velocity.y = -velocity.y if location.y > height or location.y < 0 else velocity.y

    # Display the circle at location x, y
    stroke(0)
    fill(175)
    ellipse(location.x, location.y, 16, 16)

run()
