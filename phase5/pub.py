import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

mqttc = mqtt.Client()

GPIO.setmode(GPIO.BCM)
PIN_BUTTON = 21
GPIO.setup(PIN_BUTTON, GPIO.IN)

#def callback(): 
#      mqttc.publish("supass/iot/button",  GPIO.input(PIN_BUTTON))

#GPIO.add_event_detect(PIN_BUTTON,GPIO.BOTH,callback=callback)


con_status = mqttc.connect("broker.mqttdashboard.com", 1883)
print(con_status)
while True:
        mqttc.publish("supass/iot/button",  "ON"  if GPIO.input(PIN_BUTTON) == 1 else "OFF")
        time.sleep(0.1)
