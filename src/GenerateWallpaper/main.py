
#!/usr/local/bin/python3

from os import path
from PIL import Image, ImageDraw
import random

def generate_GRB():
    return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

resolution = [1680, 1050]
size_shapes = (120, 100)

file_directory = path.realpath(__file__).rstrip("/main.py")

output_file = "background.png"

wallpaper = Image.new("RGB", resolution, 0)
fill_canvas = ImageDraw.Draw(wallpaper)

wallpaper.save(output_file) 

colors = []

for i in range(0, 2):
    colors.append(generate_GRB())

number_shapes = (resolution[0] / size_shapes[0])
number_shapes = (resolution[1] / size_shapes[1])



