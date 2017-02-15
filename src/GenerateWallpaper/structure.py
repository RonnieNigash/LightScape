from shape import Shape, Point
from math import pi, sin, cos
from random import random

class Structure:

    def __init__(self, wallpaper_size, num_shapes, size_shapes):
        self.wallpaper_size = wallpaper_size
        self.num_shapes = num_shapes
        self.size_shapes = size_shapes

        self.shapes = []

        self.points = {}

    def paint(self, fill_canvas):
        for shape in self.shapes:
            shape.paint(fill_canvas)

    def in_bounds(self, point):
        pos_x = point.coords[0]
        pos_y = point.coords[1]
        return (pos_x != 0 and pos_y != 0 and pos_x < self.wallpaper_size[0] and pos_y < self.wallpaper_size[1])

    def populate_colors(self, first_color, second_color):

        rotate = random() * 2 * pi

        number_of_shapes = len(self.shapes)

        change_green = ( second_color[0] - first_color[0] ) / number_of_shapes
        change_red = ( second_color[0] - first_color[0] ) / number_of_shapes
        change_blue = ( second_color[0] - first_color[0] ) / number_of_shapes

        curr_color = first_color

        for shape in self.shapes:
            curr_color_casted = (
                    int(curr_color[0]),
                    int(curr_color[1]),
                    int(curr_color[2])
                    )

            shape.color = curr_color_casted

            curr_color = (
                    curr_color[0] + change_green,
                    curr_color[1] + change_red,
                    curr_color[2] + change_blue
                    )

    def generate_struct(self):
        for x in range(0, self.num_shapes[0]):
            for y in range(0, self.num_shapes[1]):
                coordinates = [
                        ( (x) * self.size_shapes[0],    (y) * self.size_shapes[1]),
                        ( (x+1) * self.size_shapes[0],  (y) * self.size_shapes[1]),
                        ( (x+1) * self.size_shapes[0],  (y+1) * self.size_shapes[1]),
                        ( (x) * self.size_shapes[0],    (y+1) * self.size_shapes[1])
                ]

                new_points = []

                for coord in coordinates:
                    if coord in self.points:
                        new_points.append(self.points[coord])
                    else:
                        new_point = Point(coord)
                        self.points[coord] = new_point
                        new_points.append(new_point)

                self.shapes.append(Shape(new_points))
        
        for point in self.points.values():
            if self.in_bounds(point):
                point.evolve()
