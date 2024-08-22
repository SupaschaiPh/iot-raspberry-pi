import RPi.GPIO as GPIO
import pwm
from time import sleep
GPIO.setwarnings(False) #disable warnings
GPIO.setmode(GPIO.BCM) #set pin numbering
ledpin = 4 #PWM pin connected to LED
#system
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000) #create PWM instance with frequency 1000
pi_pwm.start(0) #start PWM of 0% Duty Cycle
