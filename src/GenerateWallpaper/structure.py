from shape import Shape, Point

class Structure:

    def __init__(self, wallpaper_size, num_shapes, size_shapes):
        self.wallpaper_size = wallpaper_size
        self.num_shapes = num_shapes
        self.size_shapes = size_shapes

        self.shapes = []

        self.points = {}

    def generate_struct(self):
        for x in range(0, self.num_shapes[0]):
            for y in range(0, self.num_shapes[1]):
                coordinates = [
                        ( (x) * self.size_shapes[0],      (y) * self.size_shapes[1]),
                        ( (x+1) * self.size_shapes[0],    (y) * self.size_shapes[1]),
                        ( (x) * self.size_shapes[0],      (y+1) * self.size_shapes[1]),
                        ( (x+1) * self.size_shapes[0],    (y+1) * self.size_shapes[1])
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
