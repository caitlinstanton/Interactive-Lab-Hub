import random
import RPi.GPIO as GPIO
from wires import *
import wires
from keypad import *
import keypad
#import cardswipe

if __name__ == '__main__':
    try:

      state = 0
      # 0 -> START
      # 1 -> WIRES
      # 2 -> KEYPAD
      # 3 -> CARDSWIPE
      # 4 -> WIN
      # 5 -> LOSE

      order = [1,2]
      print(order)

      wires = False

      keypad = False
      pattern_state = 0
      pattern_round = 1
      pattern_count = 0
      presses = []
      mapping = {}
      pattern = []

      cardswipe = False

      while True:
        current = time.perf_counter()
        print(current)
        if state == 0:
          start = time.perf_counter()
          end = start + 90
          print("start: " + str(start))
          print("end: " + str(end))
          random.shuffle(order)
          print(order)
          state = order[0]
          order.remove(state)

          mapping = {1:0x6f, 2:0x5f, 3:0x4f, 4:0x3f, 5:0x2f, 6:0x1f}

          for i in mapping:
            button = qwiic_button.QwiicButton(mapping[i])
            button.set_debounce_time(500)
            button.LED_off()
            mapping[i] = button

          for i in range(0,len(mapping)):
            n = random.randint(1,len(mapping))
            pattern.append(n)

          print(pattern)
        elif state == 1:
          
          while not wires:
            wires = connect()
            if current > end:
              print("RAN OUT OF TIME, UNCONNECTED")
              state = 5
              break

          if wires:
            if current > end:
              print("RAN OUT OF TIME, CONNECTED")
              state = 5
            elif not order and current <= end:
              print("WOW")
              state = 4
            elif order:
              print("NEXT STATE")
              state = order[0]
              order.remove(state)

        elif state == 2:
          
          if not keypad:
            (tmp_state,tmp_round,tmp_count,tmp_presses) = press_pattern(pattern_state,pattern_round,pattern_count,mapping,pattern,presses)
            keypad = (tmp_state == 4)
            pattern_state = tmp_state
            pattern_round = tmp_round
            pattern_count = tmp_count
            presses = tmp_presses
            if current > end:
              print("RAN OUT OF TIME, DIDN'T FINISH")
              state = 5
              break

          if keypad:
            if current > end:
              print("RAN OUT OF TIME, FINISHED")
              state = 5
            elif not order and current <= end:
              print("WOW")
              state = 4
            elif order:
              print("NEXT STATE")
              state = order[0]
              order.remove(state)

        elif state == 3:
          state = 4
        elif state == 4:
          print("WON")
          break
        elif state == 5:
          print("LOST")
          break

    except (KeyboardInterrupt, SystemExit) as exErr:
        sys.exit(0)