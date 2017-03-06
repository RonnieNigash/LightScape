from PIL import ImageGrab

SCREEN_RESOLUTION = [1680, 1050]
NUM_X_LEDS = 2
NUM_Y_LEDS = 2

width = SCREEN_RESOLUTION[0]
height = SCREEN_RESOLUTION[1]

num_x_steps = (int) (width / NUM_X_LEDS)
num_y_steps = (int) (height / NUM_Y_LEDS)

screen_grab = []

for x in range(0, width, num_x_steps):
    for y in range(0, height, num_y_steps):
        screen_grab.append(ImageGrab.grab( bbox = (x, y, x+1, y+1) ))

print ( screen_grab[0].getpixel( (0,0) ))
print ( screen_grab[1].getpixel( (0,0) ))
