from adafruit_circuitplayground import cp

import time

import random

def dice_roll(): 
    roll = random.randint(0,10)
    if cp.button_a:
                for i in range(roll):
                        cp.pixels[i] = (0,0,25)
                while cp.button_a:
                        pass
                #rooling of the dice
    if cp.button_b:
                for ia in range(0,10):
                        cp.pixels[ia] = (0,0,0)
                while cp.button_b:
                        pass
                #clears all the light's
while True:
    dice_roll()