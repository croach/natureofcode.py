from p5 import *

def setup():
	size(640, 480)


def draw():
	if (mousePressed):
		fill(0)
	else:
		fill(255)
	ellipse(mouseX, mouseY, 80, 80)

run()