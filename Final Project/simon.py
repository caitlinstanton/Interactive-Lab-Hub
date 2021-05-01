from __future__ import print_function
import qwiic_i2c
import qwiic_button
import time
import sys
import random

one = qwiic_button.QwiicButton('0x6f')
two = qwiic_button.QwiicButton('0x5f')
three = qwiic_button.QwiicButton('0x4f')
four = qwiic_button.QwiicButton('0x3f')
five = qwiic_button.QwiicButton('0x1f')
# six = qwiic_button.QwiicButton(i2c_addr)

mapping = {1:one, 2:two, 3:three, 4:four, 5:five}

for i in mapping:
  i2c_addr = mapping[i]
  name = str(i)
  button = qwiic_button.QwiicButton(i2c_addr)

pattern = []
for i in range(0,len(mapping)):
  n = random.randint(1,len(mapping))
  pattern.append(n)

print(pattern)

def turn_on():
  print(one)
  one.LED_on(255)

def blink_buttons(idx):
  i = 0
  while i <= idx:
    print(i)
    button = pattern[i]
    if button == 1:
      turn_on()
      # one.LED_on(255)
    else:
      print("oop")
    # print(mapping[button])
    # mapping[button].LED_on(255)
    # time.sleep(1)
    # tmp.LED_off()
    i = i+1

def run_example():

    if one.begin() == False:
        print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    print("\nButton's ready!")

    while 1:

        blink_buttons(4)
        
        time.sleep(0.02)    # Don't hammer too hard on the I2C bus

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 7")
        sys.exit(0)