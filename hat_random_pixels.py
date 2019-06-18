#!usr/bin/env python 
from sense_hat import SenseHat
import time 
import random 

sense = SenseHat()

r = random.randint(0, 225)
o = random.randint(0, 225) 
d = random.randint(0, 225)
R = random.randint(0, 7)
O = random.randint(0, 7)
sense.set_pixel(R, O, (r, o, d))

time.sleep(1)
sense.clear()
