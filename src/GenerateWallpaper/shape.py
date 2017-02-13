from random import uniform

class Shape:

    def __init__(self, points, color=(0,0,0)):
        self.points = points
        self.color = color

class Point:

    def __init__(self, coords):
        self.coords = coords

    def evolve(self):
        x_delta = uniform(-1,1)
        y_delta = uniform(-1,1)

        self.coords = (self.coords[0] + x_delta, self.coords[1] + y_delta)


