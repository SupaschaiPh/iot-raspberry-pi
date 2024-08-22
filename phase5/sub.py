import paho.mqtt.client as mqtt
import pwm


MQTT_BROKER = 'mqtt-dashboard.com'  
MQTT_PORT = 1883  
MQTT_TOPIC = 'supass/iot/led'  

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic once connected
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")
    try :
        pwm.pi_pwm.ChangeDutyCycle(int(message.payload.decode()))
    except:
        pwm.pi_pwm.ChangeDutyCycle(100 if message.payload.decode().upper() == "ON" else 0)
 

# Create a new MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop to process network traffic and dispatch callbacks
client.loop_start()

try:
    # Keep the script running
    while True:
        pass
except KeyboardInterrupt:
    # Stop the loop and disconnect gracefully on keyboard interrupt
    client.loop_stop()
    client.disconnect()
