import random
import RPi.GPIO as GPIO
from wires import *
import wires
#import keypad
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

      order = [1,2,3]
      print(order)
      wires = False
      keypad = False
      cardswipe = False

      while True:
        current = time.perf_counter()
        print(current)
        if state == 0:
          start = time.perf_counter()
          end = start + 10
          print("start: " + str(start))
          print("end: " + str(end))
          random.shuffle(order)
          print(order)
          state = order[0]
          order.remove(state)

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
          state = 4
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