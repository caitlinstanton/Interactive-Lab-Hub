import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
  GPIO.output(26,GPIO.HIGH)
  if GPIO.input(5):
    print("green connected!")
  if GPIO.input(6):
    print("red connected!")
  if GPIO.input(13):
    print("yellow connected!")
    exit()
GPIO.cleanup()