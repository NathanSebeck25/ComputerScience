from adafruit_circuitplayground import cp

import time



while True:
    for i in range (0,10):
        cp.pixels.fill(1,0,0)
        cp.play_tone(500,.5)
        time.sleep(.5)
        cp.pixels.fill(0,0,1)
        cp.play_tone(900,.5)
        time.sleep(.5)
        