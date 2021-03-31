from __future__ import print_function
import qwiic_i2c
import qwiic_button
import time
import sys
import time
import board
import busio
import adafruit_mpr121

my_button1 = qwiic_button.QwiicButton()
my_button2 = qwiic_button.QwiicButton(0x4F)

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

def play():

    print("\nLet's play Mancala!")

    if my_button1.begin() == False:
        print("\nThe Qwiic Button 1 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    if my_button2.begin() == False:
        print("\nThe Qwiic Button 2 isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    print("\nButton's ready!")

    my_button1.LED_on(255)

    while 1:

        # Check if button 1 is pressed
        if my_button1.is_button_pressed() == True:
            my_button1.LED_off()
            my_button2.LED_on(255)
            print("\nPlayer 2's turn!")
        
        # Check if button2 is pressed
        if my_button2.is_button_pressed() == True:
            my_button1.LED_on(255)
            my_button2.LED_off()
            print("\nPlayer 1's turn")

        for i in range(12):
            if mpr121[i].value:
                print(f"Banana {i} touched!")
        time.sleep(0.25)  # Small delay to keep from spamming output messages.

if __name__ == '__main__':
    try:
        play()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nThanks for playing!")
        my_button2.LED_off()
        my_button1.LED_off()
        sys.exit(0)