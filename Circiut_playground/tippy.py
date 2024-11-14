from adafruit_circuitplayground import cp

import time

while True:

    x,y,z =cp.acceleration
    if x>1:
            cp.pixels[1] = (0, 25, 0)
            cp.pixels[2] = (0, 25, 0)
            cp.pixels[3] = (0, 25, 0)
            cp.pixels[6] = (0, 0, 0)
            cp.pixels[7] = (0, 0, 0)
            cp.pixels[8] = (0, 0, 0)

    elif x < -1:
            cp.pixels[1] = (0, 0, 0)
            cp.pixels[2] = (0, 0, 0)
            cp.pixels[3] = (0, 0, 0)
            cp.pixels[6] =( 0, 25, 0)
            cp.pixels[7] = (0, 25, 0)
            cp.pixels[8] = (0, 25, 0)