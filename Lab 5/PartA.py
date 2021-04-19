import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789
import numpy as np
import imageio
import time

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Function to determine if an image would be "red"
def is_red(img):
    # Displaying image on screen
    if disp.rotation % 180 == 90:
        height = disp.width  # we swap height/width to rotate it to landscape!
        width = disp.height
    else:
        width = disp.width  # we swap height/width to rotate it to landscape!
        height = disp.height
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)

    image = Image.open(img)
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True

    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image and display
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))
    disp.image(image)

    # Data processing
    i = imageio.imread(img)
    red = i[:,:,0]
    min_red = np.amin(red, axis = 0)
    max_red = np.amax(np.amax(red), axis = 0)
    avg_red = np.average(np.average(red, axis = 0))
    if(np.amin(min_red) > 15):
        print("The ",img, "picture has a red tint.", end ='')
    else:
        print("The ",img, "picture does not have a red tint.", end ='')
    print("The average pixel value for red is ", int(avg_red),"and the highest value is ",max_red,".")

    # Pause
    time.sleep(.5)




# Sample images
is_red('red.jpg')
is_red('pink.jpg')
is_red('blue.jpg')
