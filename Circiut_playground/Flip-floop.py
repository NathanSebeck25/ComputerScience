from adafruit_circuitplayground import cp

import time


while True:
   if cp.switch:
      for z in range(5,10):
         cp.pixels[z]= (0, 0, 0)
            
            
      for i in range(0,5):
            
            cp.pixels[i]= (47, 2, 79)
            #turns right side on left side off
   else:
      for y in range(0,5):
            
            cp.pixels[y]= (0, 0, 0)
            
      for b in range(5,10):
            
            cp.pixels[b]= (47, 2, 79)
            #turns right side off turns right side on 