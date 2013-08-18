"""The Walker class from The Nature of Code, Introduction (1.2)

TO DO's:

- The HEIGHT and WIDTH variables should be made global somehow. Maybe
  look into how Flask handles context locals, i.e., global variables
  that are essentially proxies to the same object in the current
  active context.

- The display method is missing because functions such as stroke and
  point are not globaly available.

"""

from random import choice, randint

# TODO: add to the processing library
def constrain(amt, low, high):
    """Constrains a value to not exceed a maximum and minimum value.
    """
    if amt < low:
        return low
    elif amt > high:
        return high
    else:
        return amt

class Walker(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = self.width/2
        self.y = self.height/2
        self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]

    @property
    def position(self):
        return {'x': self.x, 'y': self.y}

    def step(self):
        direction = choice(['left', 'right', 'forward', 'backward'])
        if direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1
        elif direction == 'forward':
            self.y += 1
        elif direction == 'backward':
            self.y -= 1

        self.x = constrain(self.x, 0, self.width-1)
        self.y = constrain(self.y, 0, self.height-1)
