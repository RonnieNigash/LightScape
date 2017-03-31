from PIL import ImageGrab

NUM_LEDS = 120
NUM_X_LEDS = (0.6)*NUM_LEDS
NUM_Y_LEDS = (0.4)*NUM_LEDS

img = ImageGrab.grab().convert('RGB')
px = img.load()

width = img.size[0]
height = img.size[1]

width_per_LED = (int) (2 * (width / NUM_X_LEDS))
height_per_LED = (int) (2 * (height / NUM_Y_LEDS))

samples = []

for x_top in range(0, width, width_per_LED):
    samples.append(px[x_top,0])

for x_bot in range(0, width, width_per_LED):
    samples.append(px[x_top,height-1])

for y_left in range(0, height, height_per_LED):
    samples.append(px[0,y_left])

for y_right in range(0, height, height_per_LED):
    samples.append(px[width-1,y_right])

print(samples)
