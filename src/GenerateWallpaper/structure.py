from shape import Shape, Point

class Structure:

    def __init__(self, wallpaper_size, num_shapes, size_shapes):
        self.wallpaper_size = wallpaper_size
        self.num_shapes = num_shapes
        self.size_shapes = size_shapes

        self.shapes = []

        self.points = {}

    def in_bounds(self, point):
        pos_x = point.coords[0]
        pos_y = point.coords[1]
        return (pos_x != 0 and pos_y != 0 and pos_x < self.wallpaper_size[0] and pos_y < self.wallpaper_size[1])

    def populate_colors(self, first_color, second_color):
        number_of_shapes = len(self.num_shapes)

        GRB_change = []

        for color in range(0, 3):
            GRB_change.append( (second_color[color] - first_color[color]) / number_of_shapes )

        GRB_save = first_color

        for shape in self.shapes:
            shape.color = (
                    int(GRB_save[0]) + int(GRB_change[0]),
                    int(GRB_save[1]) + int(GRB_change[1]),
                    int(GRB_save[2]) + int(GRB_change[2]),
                    )

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

        for point in self.points.values():
            if self.in_bounds(point):
                point.evolve()
