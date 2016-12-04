#!/usr/bin/env python
#coding: utf8

import time
import RPi.GPIO as GPIO

#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.remove_event_detect(23)

#global currentState
#currentState = 1

def printFunction(channel):
 # global currentState
#  current_time = time.localtime()
#  cur_time_str = time.strftime('%a, %d %b %Y %H:%M:%S', current_time)

  if(GPIO.input(channel)==0):# & currentState == 1):
    print "Water level is too low"
    #currentState = 0
  elif(GPIO.input(channel)==1):# & currentState == 1):
    print "Water level is high enough"
    #currentState = 1
#  elif(GPIO.input(channel)==0 & currentState == 0):
#    print cur_time_str, "00 Water level is too low"
#    currentState = 0
#  elif(GPIO.input(channel)==1 & currentState == 0):
#    print cur_time_str, "Water level is high enough"
#    currentState = 1
#  else:
#    currentState = 1
#  print('Water switch pressed!')
#  print('Note how the bouncetime affects the button press')

#def printFallFunction(channel):
#  print "Water level is too low"

current_time = time.localtime()
cur_time_str = time.strftime('%a, %d %b %Y %H:%M:%S', current_time)

print "Water level probe started at ", cur_time_str
print "When the water level drops to the bottom of the sensor, "
print "'Water level is too low' will be displayed."
print "Once the level is back to above the sensor 'Water level"
print "is high enough' will be displayed.\n"

#GPIO.add_event_detect(23, GPIO.BOTH, callback=printFunction, bouncetime=600)

try:
  while True:
     time.sleep(0.01)
#    time.sleep(5)
#    current_time = time.localtime()
#    cur_time_str = time.strftime('%a, %d %b %Y %H:%M:%S', current_time)
#    print cur_time_str
#  printFunction(0)
  #if(GPIO.input(23) ==1):
  #  print('Button 1 pressed')
  current_time = time.localtime()
  cur_time_str = time.strftime('%a, %d %b %Y %H:%M:%S', current_time)
#
  GPIO.wait_for_edge(23, GPIO.RISING)
  print cur_time_str, "Water level is too low"
  GPIO.wait_for_edge(23, GPIO.FALLING)
  print cur_time_str, "Water level is high enough"

finally:
  #GPIO.cleanup()
  GPIO.remove_event_detect(23)
  GPIO.cleanup()
