import time
import board
import busio
import adafruit_mpr121

def swiped(mpr121,start_time,end_time,swipe_time_sec):
  if (not(swipe_time_sec>1 and swipe_time_sec<3)):
    start_time = time.perf_counter()
    while (mpr121[0].value):
        print("still touching")
    end_time = time.perf_counter()
    swipe_time_sec = end_time - start_time
    return (False,start_time,end_time,swipe_time_sec)
  else:
    return (True,start_time,end_time,swipe_time_sec)