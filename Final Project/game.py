import random
import RPi.GPIO as GPIO
import board
import busio
import adafruit_mpr121
import time
from time import strftime, sleep
import subprocess
import digitalio
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import

from wires import *
import wires
from keypad import *
import keypad
from cardswipe import *
import cardswipe

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
disp.image(image,rotation)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
y = top

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)

# setup backlight and buttons
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

if __name__ == '__main__':
    try:
      
      state = -1
      # 0 -> START
      # 1 -> WIRES
      # 2 -> KEYPAD
      # 3 -> CARDSWIPE
      # 4 -> WIN
      # 5 -> LOSE

      wires = False

      keypad = False
      pattern_state = 0
      pattern_round = 1
      pattern_count = 0
      presses = []
      pattern = []
      first_task = ""
      second_task = ""
      third_task = ""
      
      mapping = {1:0x6f, 2:0x5f, 3:0x4f, 4:0x3f, 5:0x2f, 6:0x1f}

      for i in mapping:
        button = qwiic_button.QwiicButton(mapping[i])
        button.set_debounce_time(500)
        button.LED_off()
        mapping[i] = button

      ready = False
      while not ready:
        for i in mapping:
          button = mapping[i]
          ready = button.begin()

      cardswipe = False
      start_time = 0
      end_time = 0
      swipe_time_sec = 0
      i2c = busio.I2C(board.SCL, board.SDA)
      mpr121 = adafruit_mpr121.MPR121(i2c)

      end = 0
      current = 0
      time_left = 0
      start = False
      win = False

      while True:

        draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
        print(state)
        if state == -1:

          wires = False

          keypad = False
          pattern_state = 0
          pattern_round = 1
          pattern_count = 0
          presses = []
          pattern = []
          first_task = ""
          second_task = ""
          third_task = ""
          
          mapping = {1:0x6f, 2:0x5f, 3:0x4f, 4:0x3f, 5:0x2f, 6:0x1f}

          for i in mapping:
            button = qwiic_button.QwiicButton(mapping[i])
            button.set_debounce_time(500)
            button.LED_off()
            mapping[i] = button

          ready = False
          while not ready:
            for i in mapping:
              button = mapping[i]
              ready = button.begin()

          cardswipe = False
          start_time = 0
          end_time = 0
          swipe_time_sec = 0
          i2c = busio.I2C(board.SCL, board.SDA)
          mpr121 = adafruit_mpr121.MPR121(i2c)

          end = 0
          current = 0
          time_left = 0
          start = False
          win = False

          start = False
          win = False
          draw.text((x, y+95), "<-- Press button to start", font=font, fill=(255,255,255))
          disp.image(image,rotation)

          while buttonB.value:
            print(time.time()," waiting to start game")

          # Start button pressed
          start = True
          state = 0
          current = time.perf_counter()
          end = current + 60
          time_left = end - current

          order = [1,2,3]
          print(order)

        elif state == 0:
          random.shuffle(order)
          state = order[0]

          first = order[0]
          second = order[1]
          third = order[2]

          if first == 1:
            first_task = "1. wires"
          elif first == 2:
            first_task = "1. keypad"
          elif first == 3:
            first_task = "1. cardswipe"

          if second == 1:
            second_task = "2. wires"
          elif second == 2:
            second_task = "2. keypad"
          elif second == 3:
            second_task = "2. cardswipe"

          if third == 1:
            third_task = "3. wires"
          elif third == 2:
            third_task = "3. keypad"
          elif third == 3:
            third_task = "3. cardswipe"
            
          order.remove(state)
          print(state)
          for i in range(0,len(mapping)):
            n = random.randint(1,len(mapping))
            pattern.append(n)

        elif state == 1:

          draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
          if time_left > 0:
            # print(time_left)
            text_color = (255,255,255)

            # Flash yellow for last 15 seconds
            if time_left < 10 and int(time.time())%2 == 0:
                draw.rectangle((0, 0, width, height), outline=0, fill= (255,256,0))
                draw.text((x, y+110), "The imposter is coming!", font=font, fill=(0,0,0))
                text_color = (0,0,0)

            # Always display time left
            draw.text((x+70, y), "seconds left: ", font=font_big, fill=text_color)
            current = time.perf_counter()
            time_left = end - current
            draw.text((x+30, y), str(int(time_left)), font=font_big, fill=text_color)
            
            # Display text
            draw.text((x, y+45), "TASKS:", font=font, fill=text_color)
            if first_task == "1. wires":
              if wires:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            elif first_task == "2. keypad":
              if keypad:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            elif first_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            
            if second_task == "1. wires":
              if wires:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
            elif second_task == "2. keypad":
              if keypad:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
            elif second_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))

            if third_task == "1. wires":
              if wires:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
            elif third_task == "2. keypad":
              if keypad:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
            elif third_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
            

            disp.image(image,rotation)
          
          while not wires:
            wires = connect()
            if time_left <= 0:
              print("RAN OUT OF TIME, UNCONNECTED")
              wires = True
              state = 5

            draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
            if time_left > 0:
              print(time_left)
              text_color = (255,255,255)

              # Flash yellow for last 15 seconds
              if time_left < 10 and int(time.time())%2 == 0:
                  draw.rectangle((0, 0, width, height), outline=0, fill= (255,256,0))
                  draw.text((x, y+110), "The imposter is coming!", font=font, fill=(0,0,0))
                  text_color = (0,0,0)

              # Always display time left
              draw.text((x+70, y), "seconds left: ", font=font_big, fill=text_color)
              current = time.perf_counter()
              time_left = end - current
              draw.text((x+30, y), str(int(time_left)), font=font_big, fill=text_color)
              
              # Display text
              draw.text((x, y+45), "TASKS:", font=font, fill=text_color)
              if first_task == "1. wires":
                if wires:
                  draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
              elif first_task == "2. keypad":
                if keypad:
                  draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
              elif first_task == "3. cardswipe":
                if cardswipe:
                  draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
              
              if second_task == "1. wires":
                if wires:
                  draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
              elif second_task == "2. keypad":
                if keypad:
                  draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
              elif second_task == "3. cardswipe":
                if cardswipe:
                  draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+75), second_task, font=font, fill=(255,0,0))

              if third_task == "1. wires":
                if wires:
                  draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
              elif third_task == "2. keypad":
                if keypad:
                  draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
              elif third_task == "3. cardswipe":
                if cardswipe:
                  draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+90), third_task, font=font, fill=(255,0,0))

              disp.image(image,rotation)

          if wires:
            if time_left <= 0:
              print("RAN OUT OF TIME, CONNECTED")
              state = 5
            elif not order and time_left > 0:
              print("WOW")
              state = 4
            elif order:
              print("NEXT STATE")
              state = order[0]
              order.remove(state)

        elif state == 2:
          
          draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
          if time_left > 0:
            print(time_left)
            text_color = (255,255,255)

            # Flash yellow for last 15 seconds
            if time_left < 10 and int(time.time())%2 == 0:
                draw.rectangle((0, 0, width, height), outline=0, fill= (255,256,0))
                draw.text((x, y+110), "The imposter is coming!", font=font, fill=(0,0,0))
                text_color = (0,0,0)

            # Always display time left
            draw.text((x+70, y), "seconds left: ", font=font_big, fill=text_color)
            current = time.perf_counter()
            time_left = end - current
            draw.text((x+30, y), str(int(time_left)), font=font_big, fill=text_color)
            
            # Display text
            # Display text
            draw.text((x, y+45), "TASKS:", font=font, fill=text_color)
            if first_task == "1. wires":
              if wires:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            elif first_task == "2. keypad":
              if keypad:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            elif first_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            
            if second_task == "1. wires":
              if wires:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
            elif second_task == "2. keypad":
              if keypad:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
            elif second_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))

            if third_task == "1. wires":
              if wires:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
            elif third_task == "2. keypad":
              if keypad:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
            elif third_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0)) 

            disp.image(image,rotation)

          if not keypad:
            (tmp_state,tmp_round,tmp_count,tmp_presses) = press_pattern(pattern_state,pattern_round,pattern_count,mapping,pattern,presses)
            keypad = (tmp_state == 4)
            pattern_state = tmp_state
            pattern_round = tmp_round
            pattern_count = tmp_count
            presses = tmp_presses
            if time_left <= 0:
              print("RAN OUT OF TIME, DIDN'T FINISH")
              state = 5

          if keypad:
            if time_left <= 0:
              print("RAN OUT OF TIME, FINISHED")
              state = 5
            elif not order and time_left > 0:
              print("WOW")
              state = 4
            elif order:
              print("NEXT STATE")
              state = order[0]
              order.remove(state)

        elif state == 3:
          
          draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
          if time_left > 0:
            print(time_left)
            text_color = (255,255,255)

            # Flash yellow for last 15 seconds
            if time_left < 10 and int(time.time())%2 == 0:
                draw.rectangle((0, 0, width, height), outline=0, fill= (255,256,0))
                draw.text((x, y+110), "The imposter is coming!", font=font, fill=(0,0,0))
                text_color = (0,0,0)

            # Always display time left
            draw.text((x+70, y), "seconds left: ", font=font_big, fill=text_color)
            current = time.perf_counter()
            time_left = end - current
            draw.text((x+30, y), str(int(time_left)), font=font_big, fill=text_color)
            
            # Display text
            # Display text
            draw.text((x, y+45), "TASKS:", font=font, fill=text_color)
            if first_task == "1. wires":
              if wires:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            elif first_task == "2. keypad":
              if keypad:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            elif first_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
            
            if second_task == "1. wires":
              if wires:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
            elif second_task == "2. keypad":
              if keypad:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
            elif second_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+75), second_task, font=font, fill=(255,0,0))

            if third_task == "1. wires":
              if wires:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
            elif third_task == "2. keypad":
              if keypad:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
            elif third_task == "3. cardswipe":
              if cardswipe:
                draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
              else:
                draw.text((x, y+90), third_task, font=font, fill=(255,0,0))

            disp.image(image,rotation)

          while not cardswipe:
            (cardswipe,tmp_start_time,tmp_end_time,tmp_swiped_time_sec) = swiped(mpr121,start_time,end_time,swipe_time_sec)
            start_time = tmp_start_time
            end_time = tmp_end_time
            swipe_time_sec = tmp_swiped_time_sec
            if time_left <= 0:
              print("RAN OUT OF TIME, NOT SWIPED")
              cardswipe = True
              state = 5

            draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))
            if time_left > 0:
              print(time_left)
              text_color = (255,255,255)

              # Flash yellow for last 15 seconds
              if time_left < 10 and int(time.time())%2 == 0:
                  draw.rectangle((0, 0, width, height), outline=0, fill= (255,256,0))
                  draw.text((x, y+110), "The imposter is coming!", font=font, fill=(0,0,0))
                  text_color = (0,0,0)

              # Always display time left
              draw.text((x+70, y), "seconds left: ", font=font_big, fill=text_color)
              current = time.perf_counter()
              time_left = end - current
              draw.text((x+30, y), str(int(time_left)), font=font_big, fill=text_color)
              
              # Display text
              draw.text((x, y+45), "TASKS:", font=font, fill=text_color)
              if first_task == "1. wires":
                if wires:
                  draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
              elif first_task == "2. keypad":
                if keypad:
                  draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
              elif first_task == "3. cardswipe":
                if cardswipe:
                  draw.text((x, y+60), first_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+60), first_task, font=font, fill=(255,0,0))
              
              if second_task == "1. wires":
                if wires:
                  draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
              elif second_task == "2. keypad":
                if keypad:
                  draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+75), second_task, font=font, fill=(255,0,0))
              elif second_task == "3. cardswipe":
                if cardswipe:
                  draw.text((x, y+75), second_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+75), second_task, font=font, fill=(255,0,0))

              if third_task == "1. wires":
                if wires:
                  draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
              elif third_task == "2. keypad":
                if keypad:
                  draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
              elif third_task == "3. cardswipe":
                if cardswipe:
                  draw.text((x, y+90), third_task, font=font, fill=(0,255,0))
                else:
                  draw.text((x, y+90), third_task, font=font, fill=(255,0,0))
              

              disp.image(image,rotation)

          if cardswipe:
            if time_left <= 0:
              print("RAN OUT OF TIME, SWIPED")
              state = 5
            elif not order and time_left > 0:
              print("WOW")
              state = 4
            elif order:
              print("NEXT STATE")
              state = order[0]
              order.remove(state)

        elif state == 4:
          print("WON")
          status = "YOU WON!!!"
          draw.text((x, y+25), "GAME OVER", font=font, fill=(255,255,255))
          draw.text((x, y+40), status, font=font_big, fill=(255,255,255))
          draw.text((x, y+95), "<-- Press button to restart", font=font, fill=(255,255,255))
          disp.image(image,rotation)

          while buttonB.value:
              print(time.time()," waiting to restart ")

          state = -1
          sleep(0.5)
          
        elif state == 5:
          print("LOST")
          status = "YOU LOST :("
          draw.text((x, y+25), "GAME OVER", font=font, fill=(255,255,255))
          draw.text((x, y+40), status, font=font_big, fill=(255,255,255))
          draw.text((x, y+95), "<-- Press button to restart", font=font, fill=(255,255,255))
          disp.image(image,rotation)

          while buttonB.value:
              print(time.time()," waiting to restart ")

          state = -1
          sleep(0.5)

    except (KeyboardInterrupt, SystemExit) as exErr:
        sys.exit(0)