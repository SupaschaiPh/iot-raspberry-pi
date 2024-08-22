from iot import read
import time
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()


con_status = mqttc.connect("broker.mqttdashboard.com", 1883)
print(con_status)
while True:
        mqttc.publish("supass/iot/chart",  (read.ReadChannel(0)/4095)*100)
        time.sleep(0.1)
