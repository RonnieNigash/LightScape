
#!/usr/local/bin/python3

from os import path
from PIL import Image, ImageDraw
from math import ceil
import random

def generate_GRB():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

def generate_structure(num_shapes_horizontal, num_shapes_vertical, shape_size, wallpaper_size):
    points = []
    for x in range(0, num_shapes_horizontal):
        for y in range(0, num_shapes_vertical):
            coordinates = [
                    ( (x) * shape_size[0],      (y) * shape_size[1]),
                    ( (x+1) * shape_size[0],    (y) * shape_size[1]),
                    ( (x) * shape_size[0],      (y+1) * shape_size[1]),
                    ( (x+1) * shape_size[0],    (y+1) * shape_size[1])
            ]
            points.append(coordinates)
    return points 

resolution = [1680, 1050]
shape_size = (120, 100)

file_directory = path.realpath(__file__).rstrip("/main.py")

output_file = "background.png"

wallpaper = Image.new("RGB", resolution, 0)
fill_canvas = ImageDraw.Draw(wallpaper)

wallpaper.save(output_file) 

colors = []

for i in range(0, 2):
    colors.append(generate_GRB())

num_shapes_horizontal = ceil((resolution[0] / shape_size[0]))
num_shapes_vertical = ceil((resolution[1] / shape_size[1]))

structure_of_shapes = generate_structure(num_shapes_horizontal, num_shapes_vertical, shape_size, wallpaper.size)
