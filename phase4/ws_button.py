import RPi.GPIO as GPIO
import asyncio
import websockets , json
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

GPIO.setmode(GPIO.BCM)
PINXX = 21
GPIO.setup(PINXX,GPIO.IN)

def ReadChannel(channel):
    """Reads data from the specified channel of the MCP3208 ADC.

    Args:
        channel: The ADC channel to read from (0-7).

    Returns:
        The raw ADC reading as an integer (0-4095).
    """

    r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])
    data = ((r[1]&15) << 8) + r[2]
    return data

async def readTempToServer(websocket):
        while True:
                LED_MODE = 1
                await websocket.send(json.dumps({"LED_STATE":[not not GPIO.input(PINXX),ReadChannel(3)][LED_MODE], "LED_MODE": LED_MODE }))
                #print([not not GPIO.input(PINXX),ReadChannel(3)][LED_MODE])
                await asyncio.sleep(0.25)
async def recieve_message(websocket):
        while True:
                try:
                    message = await websocket.recv()
                    print(f"Recieve : {message}")
                except websockets.exceptions.ConnectionClosed:
                    print("Conection Closed")
                    break
async def communicate():
        uri = "ws://192.168.103.32:8765"
        async with websockets.connect(uri) as websocket:
               while True:
                    await asyncio.gather(readTempToServer(websocket))
                    await asyncio.sleep(0.5)


if __name__== "__main__":
        asyncio.run(communicate())
