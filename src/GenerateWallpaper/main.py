
#!/usr/local/bin/python3

from os import path
from PIL import Image, ImageDraw, ImageFilter
#from PyAgg import Draw, Brush, Pen # <- PyAgg library not supported in Python3
from math import ceil
import subprocess, sys
import random
from structure import Structure

RESOLUTION = [1680, 1050]
#SHAPE_SIZE = (60, 40)

def generate_GRB():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

def sum_of_min_max(r, g , b):
    if b < g: g, b = b, g
    if g < r: r, g = g, r
    if b < g: g, b = b, g
    return r + b

def complement(r, g, b):
    k = sum_of_min_max(r, g, b)
    return tuple(k - u for u in (r, g, b))

file_directory = path.realpath(__file__).rstrip("/main.py")

for run in range(0, 5):

    SHAPE_SIZE = (random.randint(15,100), random.randint(15,100))
    output_file = "background" + str(run) + ".png"

    wallpaper = Image.new("RGB", RESOLUTION, 0)
#    fill_canvas = Draw(wallpaper) # <- PyAgg library not supported in Python3
    fill_canvas = ImageDraw.Draw(wallpaper)

    colors = []

    colors.append(generate_GRB())

    num_shapes_horizontal = ceil((RESOLUTION[0] / SHAPE_SIZE[0]))
    num_shapes_vertical = ceil((RESOLUTION[1] / SHAPE_SIZE[1]))

    structure_of_shapes = Structure(
            wallpaper.size,
            (num_shapes_horizontal, num_shapes_vertical),
            SHAPE_SIZE
            )
    structure_of_shapes.generate_struct()

#    structure_of_shapes.populate_colors(colors[0], colors[1])
    structure_of_shapes.populate_colors(colors[0], complement(colors[0][0], colors[0][1], colors[0][2]))

    structure_of_shapes.paint(fill_canvas)

    contour = wallpaper.filter(ImageFilter.CONTOUR)
    contour_emboss = contour.filter(ImageFilter.EMBOSS)
    wallpaper = Image.blend(wallpaper, contour_emboss, 0.5)


    wallpaper.save(output_file) 
