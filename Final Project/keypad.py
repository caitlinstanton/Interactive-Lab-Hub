from __future__ import print_function
import qwiic_i2c
import qwiic_button
import time
import sys
import random

def blink_buttons(idx,pattern,mapping):
  i = 0
  print(pattern)
  while i < idx:
    print("BLINKED: " +str(pattern[i]))
    button = pattern[i]
    mapping[button].LED_on(255)
    time.sleep(0.25)
    mapping[button].LED_off()
    time.sleep(0.25)
    i = i+1

def press_pattern(state,round,count,mapping,pattern,presses):

  # 0 -> START
  # 1 -> BLINK SUBSET
  # 2 -> WAIT FOR PRESS
  # 3 -> CHECK BUTTON
  # 4 -> DONE

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
        time.sleep(0.5)
    else:
      print("incorrect press")
      presses = []
      state = 1
  elif state == 4:
    print("DONE")
    
  return (state,round,count,presses)
  time.sleep(0.1)