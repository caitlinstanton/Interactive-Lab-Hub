from wires import *
import wires
#import simon
#import cardswipe

if __name__ == '__main__':
    try:
      wires = False
      while not wires:
        wires = connect()
    except (KeyboardInterrupt, SystemExit) as exErr:
        sys.exit(0)