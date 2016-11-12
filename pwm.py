import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

p = GPIO.PWM(18	, 50) 
print("ini")
p.start(50)             # start the PWM on 50 percent duty cycle  
                        # duty cycle value can be 0.0 to 100.0%, floats are OK  
print("start")
p.ChangeDutyCycle(90)   # change the duty cycle to 90%  
print("cdc")
p.ChangeFrequency(100)  # change the frequency to 100 Hz (floats also work)  
                        # e.g. 100.5, 5.2  

p.start(0)
print("cfq")
p.stop()                # stop the PWM output  
print("stp")
GPIO.cleanup()          # when your program exits, tidy up after yourself  
print("cln")
#GPIO.output(18, GPIO.HIGH)
