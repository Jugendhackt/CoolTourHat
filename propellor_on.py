import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)



print "LED on,LED an"
GPIO.output(21,GPIO.LOW)


