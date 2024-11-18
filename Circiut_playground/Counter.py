from adafruit_circuitplayground import cp

import time

import random
count = 0
while True:
    if cp.button_a:
        count+=1
        while cp.button_a:
            pass
        cp.pixels[-1+count] = (47, 2, 79)
    if cp.button_b:
        count-=1
        while cp.button_b:
            pass
        cp.pixels[0+count] = (0,0,0)

    if count >9:
        count = 9

    if count <0:
        count = 0