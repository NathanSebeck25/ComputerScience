
from adafruit_circuitplayground import cp

import time
#Create a program that flashes all lights GREEN then off in 367ms intervals.
while True:
    
        cp.pixels.fill((0,0,0))
        time.sleep(.367)
        cp.pixels.fill((0,1,0))
        time.sleep(.367)