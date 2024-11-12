
from adafruit_circuitplayground import cp

import time
#Create a program that turns pixels 0-9 on for 100ms
# then off for 100ms in number order when button A is pressed.
#It should appear as a single light is traveling through the circle of pixels on your board.
while True:
   if cp.button_a:
      for space in range(0,10):
          cp.pixels[space]= (47, 2, 79)
          time.sleep(.1)
          cp.pixels[space]= (0, 0, 0)