#!usr/bin/env python 
from sense_hat import SenseHat
sense = SenseHat()

yellow = (0, 255, 255)
cyan = (150, 225, 0) 

speed = 0.2 

message = 'hello world!!!!!!!!!!!!'

sense.show_message(message, speed, text_colour=yellow, back_colour=cyan)

sense.clear()

