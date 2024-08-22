import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()
con_status = mqttc.connect("broker.mqttdashboard.com", 1883)
print(con_status)
while True:
        mqttc.publish("supass/iot", "Hello")
        time.sleep(2)
