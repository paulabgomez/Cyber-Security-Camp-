#!usr/bin/env python
from sense_hat import SenseHat
import time 
import random 
sense = SenseHat()

r = random.randint(0, 225)

sense.show_letter('H', (r, 0, r))
time.sleep(1)
sense.show_letter('i', (0, r, 0))
time.sleep(1)
sense.show_letter('!', (0, r, r))
time.sleep(1)

sense.clear()
