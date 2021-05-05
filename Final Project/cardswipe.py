import time
import board
import busio
import adafruit_mpr121
# import datetime
# from datetime import timedelta
# from datetime import time

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

start_time = 0
end_time = 0
swipe_time_sec = 0
while(not(swipe_time_sec>1 and swipe_time_sec<3)):
    if mpr121[0].value:
        start_time = time.perf_counter()
    while (mpr121[0].value):
        print("still touching")
    if not (mpr121[0].value):
        end_time = time.perf_counter()
    swipe_time_sec = end_time - start_time
    print(swipe_time_sec)
print("done")
time.sleep(0.25)  # Small delay to keep from spamming output messages.