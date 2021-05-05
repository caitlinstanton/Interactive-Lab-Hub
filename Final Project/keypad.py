from __future__ import print_function
import qwiic_i2c
import qwiic_button
import time
import sys
import random
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

def blink_buttons(idx,pattern,mapping):
  i = 0
  print(pattern)
  while i < idx:
    print("BLINKED: " +str(pattern[i]))
    button = pattern[i]
    mapping[button].LED_on(255)
    time.sleep(1)
    mapping[button].LED_off()
    time.sleep(1)
    i = i+1

def press_pattern(state,round,count,mapping,pattern,presses):

  # 0 -> START
  # 1 -> BLINK SUBSET
  # 2 -> WAIT FOR PRESS
  # 3 -> CHECK BUTTON
  # 4 -> DONE

  # Draw a black filled box to clear the image.
  draw.rectangle((0, 0, width, height), outline=0, fill=0)

  if state == 0:
    print("START")
    round = 1 # variable to keep track of one past the last button it's expecting
    presses = []
    state = 1

  elif state == 1:
    print("BLINK")
    print(round)
    if round == len(pattern):
      state = 4
    else:
      
      blink_buttons(round,pattern,mapping)
      count = 0 # variable to keep track of the current press to check for
      presses = []
      state = 2
  elif state == 2:
    for i in mapping:
      if mapping[i].is_button_pressed():
        print("PRESSED " + str(i))
        print("count: " + str(count))
        presses.append(i)
        state = 3
        break
      else:
        state = 2
  elif state == 3:
    print("CHECK")
    print(presses)
    if presses[count] == pattern[count]:
      print("correct press")
      if count < (round - 1):
        print("continue round")
        state = 2
        count += 1 
        time.sleep(0.5)      
      else:
        print("next round\n")
        round += 1
        state = 1
    else:
      print("incorrect press")
      presses = []
      state = 1
  elif state == 4:
    print("DONE")
    
  return (state,round,count,presses)

  # Write four lines of text
  IP = "Round: " + str(round)
  y = top
  draw.text((x, y), IP, font=font, fill="#FFFFFF")

  # Display image.
  disp.image(image, rotation)
  time.sleep(0.1)