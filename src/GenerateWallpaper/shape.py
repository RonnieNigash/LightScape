from random import uniform, randint 
#from PyAgg import Draw, Brush, Pen # <- PyAgg library not supported in Python

class Shape:

    def __init__(self, points, color=(0,0,0)):
        self.points = points
        self.color = color

    def paint(self, fill_canvas):
#        fill_canvas.polygon([shape.coords for shape in self.points], self.color, outline="black")
        fill_canvas.polygon([shape.coords for shape in self.points], self.color)
#        fill_canvas.polygon([shape.coords for shape in self.points], Brush(self.color), Pen('black')) # <- PyAgg library not supported in Python

class Point:

    def __init__(self, coords):
        self.coords = coords

    def evolve(self):
        x_delta = uniform(-1,1) * randint(1, 40)
        y_delta = uniform(-1,1) * randint(1, 40)

        self.coords = (self.coords[0] + x_delta, self.coords[1] + y_delta)
