import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont, ImageColor
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565
from time import strftime, sleep
from itertools import zip_longest
import webcolors

import smbus, time
bus = smbus.SMBus(1)
addr = 0x20

global state
state = 0
# 0 is middle state
# 1 is left direction (for binary clock)
# 2 is right direction (for normal clock)

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
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

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
regSize = 30
regFont = ImageFont.truetype("baby blocks.ttf", regSize)
binarySize = 40
binaryFont = ImageFont.truetype("3Dventure.ttf", binarySize)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

try:
    bus_data = bus.read_i2c_block_data(addr, 0x03, 5)
    #X_MSB = bus.read_byte_data(addr, 0x03) # Reads MSB for horizontal joystick position
    #X_LSB = bus.read_byte_data(addr, 0x04) # Reads LSB for horizontal joystick position

    #Y_MSB = bus.read_byte_data(addr, 0x05) # Reads MSB for vertical joystick position
    #Y_LSB = bus.read_byte_data(addr, 0x06) # Reads LSB for vertical joystick position

    #Select_Button = bus.read_byte_data(addr, 0x07) # Reads button position
except Exception as e:
    print(e)

def bcd(digits):
    def bcdigit(d):
       return (bin(d)[2:].rjust(4,'0'))
    return ((bcdigit(int(d)) for d in digits))

def vertical_strings(strings):
    'Orient an iterable of strings vertically: one string per column.'
    iters = [iter(s) for s in strings]
    concat = ''.join
    return '\n'.join(map(concat,
                         zip_longest(*iters, fillvalue=' ')))

def qwiicjoystick(curr):
    try:
        bus_data = bus.read_i2c_block_data(addr, 0x03, 5)
        #X_MSB = bus.read_byte_data(addr, 0x03) # Reads MSB for horizontal joystick position
        #X_LSB = bus.read_byte_data(addr, 0x04) # Reads LSB for horizontal joystick position
    
        #Y_MSB = bus.read_byte_data(addr, 0x05) # Reads MSB for vertical joystick position
        #Y_LSB = bus.read_byte_data(addr, 0x06) # Reads LSB for vertical joystick position

        #Select_Button = bus.read_byte_data(addr, 0x07) # Reads button position
    except Exception as e:
        print(e)

    X = (bus_data[0]<<8 | bus_data[1])>>6
    Y = (bus_data[2]<<8 | bus_data[3])>>6
    
    #print(X, Y, " Button = ", bus_data[4])
    
    time.sleep(.05)
    
    if curr == 0: #middle
        if X < 450:
            state = 2 #RIGHT
        elif 575 < X:
            state = 1 #LEFT
        else:
            state = 0
    elif curr == 1: #left
        if X < 450:
            state = 0 #RIGHT
        elif 575 < X:
            state = 1 #LEFT
        else:
            state = 1
    elif curr == 2:
        if X < 450:
            state = 2 #RIGHT
        elif 575 < X:
            state = 0 #LEFT
        else:
            state = 2
    else:
        state = 0
    
    # if Y< 450:
    #     print("DOWN")
    #     #direction = DOWN
    # elif 575 < Y:
    #     print("UP")
    #     #direction = UP

    #if Select_Button == 1:
        #terminate()
    return state

# get a color from the user
screenColor = None
while not screenColor:
    try:
        # get a color from the user and convert it to RGB
        screenColor = ImageColor.getrgb(input('Type the name of a color and hit enter: '))
    except ValueError:
        # catch colors we don't recognize and go again
        print("whoops I don't know that one")
while True:
    state = qwiicjoystick(state)
    if not buttonA.value and not buttonB.value:
        backlight.value = False  # turn off backlight
    else:
        backlight.value = True
    if state == 0: 
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=screenColor)
        disp.image(image, rotation)
    if state == 1: 
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=screenColor)
        #convert to binary
        bcdval = vertical_strings(bcd(strftime('%H%M%S')))
        x = (width/2) - (binarySize * 1.8)
        y = top
        draw.text((x,y),bcdval,font=binaryFont,fill="#FFFFFF")
        disp.image(image, rotation)
    if state == 2: 
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=screenColor)
        x = 0
        y = (height/2)-(regSize/2)
        draw.text((x,y),strftime('%H:%M:%S'),font=regFont,fill="#FFFFFF")
        disp.image(image, rotation)
    # if buttonA.value and not buttonB.value:  # just button B pressed
    #     # Draw a black filled box to clear the image.
    #     draw.rectangle((0, 0, width, height), outline=0, fill=screenColor)
    #     x = 0
    #     y = (height/2)-(regSize/2)
    #     draw.text((x,y),strftime('%H:%M:%S'),font=regFont,fill="#FFFFFF")
    #     disp.image(image, rotation)