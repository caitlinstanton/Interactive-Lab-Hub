import RPi.GPIO as GPIO
import time

def connect():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(26,GPIO.OUT)
  GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  green = False
  red = False
  yellow = False

  GPIO.output(26,GPIO.HIGH)
  while (not green) or (not red) or (not yellow):
    if GPIO.input(5):
      green = True
    elif not GPIO.input(5):
      green = False

    if GPIO.input(6):
      red = True
    elif not GPIO.input(6):
      red = False

    if GPIO.input(13):
      yellow = True
    elif not GPIO.input(13):
      yellow = False

  return True
  GPIO.cleanup()