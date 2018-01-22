# Connect LED to GPIO22 (pin 15)
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, True)
time.sleep(3)
GPIO.cleanup()
