
#!/usr/local/bin/python3

from os import path
from PIL import Image, ImageDraw
from math import ceil
import random

RESOLUTION = [1680, 1050]
SHAPE_SIZE = (120, 100)

def generate_GRB():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

def generate_structure(num_shapes_horizontal, num_shapes_vertical, SHAPE_SIZE, wallpaper_size):
    points = []
    for x in range(0, num_shapes_horizontal):
        for y in range(0, num_shapes_vertical):
            coordinates = [
                    ( (x) * SHAPE_SIZE[0],      (y) * SHAPE_SIZE[1]),
                    ( (x+1) * SHAPE_SIZE[0],    (y) * SHAPE_SIZE[1]),
                    ( (x) * SHAPE_SIZE[0],      (y+1) * SHAPE_SIZE[1]),
                    ( (x+1) * SHAPE_SIZE[0],    (y+1) * SHAPE_SIZE[1])
            ]
            points.append(coordinates)
    return points 

file_directory = path.realpath(__file__).rstrip("/main.py")

output_file = "background.png"

wallpaper = Image.new("RGB", RESOLUTION, 0)
fill_canvas = ImageDraw.Draw(wallpaper)


colors = []

for i in range(0, 2):
    colors.append(generate_GRB())

num_shapes_horizontal = ceil((RESOLUTION[0] / SHAPE_SIZE[0]))
num_shapes_vertical = ceil((RESOLUTION[1] / SHAPE_SIZE[1]))

structure_of_shapes = generate_structure(num_shapes_horizontal, num_shapes_vertical, SHAPE_SIZE, wallpaper.size)

print(structure_of_shapes)

wallpaper.save(output_file) 
