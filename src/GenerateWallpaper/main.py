
#!/usr/local/bin/python3

from os import path
from PIL import Image, ImageDraw

resolution = [1680, 1050]

file_directory = path.realpath(__file__).rstrip("/main.py")

print(file_directory)

output_file = "background.png"

wallpaper = Image.new("RGB", resolution, 0)
fill_canvas = ImageDraw.Draw(wallpaper)

wallpaper.save(output_file) 
