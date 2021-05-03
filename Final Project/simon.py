from __future__ import print_function
import qwiic_i2c
import qwiic_button
import time
import sys
import random

mapping = {1:0x6f, 2:0x5f, 3:0x4f, 4:0x3f, 5:0x2f, 6:0x1f}

for i in mapping:
  button = qwiic_button.QwiicButton(mapping[i])
  button.set_debounce_time(500)
  button.LED_off()
  mapping[i] = button

pattern = []
for i in range(0,len(mapping)):
  n = random.randint(1,len(mapping))
  pattern.append(n)

print(pattern)

def blink_buttons(idx):
  i = 0
  while i < idx:
    print("BLINKED: " +str(pattern[i]))
    button = pattern[i]
    mapping[button].LED_on(255)
    time.sleep(1)
    mapping[button].LED_off()
    time.sleep(1)
    i = i+1

def round():

  state = 0
  # 0 -> START
  # 1 -> BLINK SUBSET
  # 2 -> WAIT FOR PRESS
  # 3 -> CHECK BUTTON
  # 4 -> DONE

  while True:
    if state == 0:
      print("START")
      round = 1 # variable to keep track of one past the last button it's expecting
      presses = []
      state = 1
    elif state == 1:
      print("BLINK")
      if round == len(pattern):
        state = 4
      else:
        blink_buttons(round)
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
      break

if __name__ == '__main__':
    try:
      round()
    except (KeyboardInterrupt, SystemExit) as exErr:
        sys.exit(0)