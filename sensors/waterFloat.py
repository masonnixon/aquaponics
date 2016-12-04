#!/usr/bin/env python
#coding: utf8

import time
import RPi.GPIO as GPIO
#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.remove_event_detect(23)

#def printFunction(channel):
#  print('Water switch pressed!')
#  print('Note how the bouncetime affects the button press')
#  GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=300)

while True:
#  printFunction(0)
  #if(GPIO.input(23) ==1):
  #  print('Button 1 pressed')
  current_time = time.localtime()
  cur_time_str = time.strftime('%a, %d %b %Y %H:%M:%S', current_time)

  GPIO.wait_for_edge(23, GPIO.RISING)
  print(cur_time_str,'Water level is too low')
  GPIO.wait_for_edge(23, GPIO.FALLING)
  print(cur_time_str,'Water level is high enough')

GPIO.cleanup()
GPIO.remove_event_detect(23)
