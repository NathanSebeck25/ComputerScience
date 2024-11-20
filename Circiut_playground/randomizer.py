from adafruit_circuitplayground import cp

import time

import random

while True:
    x,y,z = cp.acceleration

    if abs(x)> 20 or abs(y) >20 or abs(z) >20:#defines the movement of the borad
        for i in range(0,10):
            cp.pixels[i] = (random.randint(0,150),random.randint(0,150),random.randint(0,150))
            # runs the randomizer of the pixels