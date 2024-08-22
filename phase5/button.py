import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PINXX = 21
GPIO.setup(PINXX, GPIO.IN)
