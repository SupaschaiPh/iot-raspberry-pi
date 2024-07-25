import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

R = 17
G = 27
B = 22

GPIO.setup(R,GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)

colors = [
    (True, False, False),
    (False, True, False),
    (False, False, True),
    (True, True, False),
    (True, False, True),
    (False, True, True),
    (True, True, True)
]


while True:
        for color in colors:
            GPIO.output(R, not color[0])
            GPIO.output(G, not color[1])
            GPIO.output(B, not color[2])
            time.sleep(1)
