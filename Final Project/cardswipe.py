import time
import board
import busio
import adafruit_mpr121

# Initialize connections
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# Initialize variables
start_time = 0
end_time = 0
swipe_time_sec = 0

while(not(swipe_time_sec>1 and swipe_time_sec<3)):
    start_time = time.perf_counter()
    while (mpr121[0].value):
        print("still touching")
    end_time = time.perf_counter()
    swipe_time_sec = end_time - start_time
    print(swipe_time_sec)
print("done")