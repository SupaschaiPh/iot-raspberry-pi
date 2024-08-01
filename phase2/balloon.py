import time
import spidev
import RPi.GPIO as GPIO
import math
from numpy import log as ln
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 100000

# Function to read SPI data from MCP3208 chip
def ReadChannel(channel):
    #adc = spi.xfer2([4 + (channel >> 2), (channel & 3) << 6, 0])
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])
    data = ((adc[1] & 15) << 8) + adc[2]
    #adc = spi.xfer2([1, (8 + channel) << 4, 0])
    #data = ((adc[1] & 3) << 8) + adc[2]
    return data

def convert_to_temperature(adc_value):
    # MCP9700 has a 10mV/  C scale factor with a 500mV offset for 0  C
    voltage = (adc_value * 3.3) / 4096
    temperature = 100*(voltage-1)+50
    #temperature = (voltage-0.5)*100
    return temperature

def read_temp_from_thermistor(channel, r1, vin=3.3):
    volts = (channel*3.3)/4096
    # Convert voltage level to resistance
   # r_thermistor = (volts * r1) / (vin - volts)
    # Simple linear approximation of temperature (Celsius)
    r = (volts*r1)/(vin-volts)
    temperature = (298.15*4050)/(298.15*ln(r/r1)+4050)
    temperature = temperature-273.15
    return temperature

def convert_volts(data):
    volts = (data * 3.3) / float(4096)
    return volts

r1 = 10000
try:
    while True:
        adc_value = ReadChannel(0)  # Read from channel 0
        val = ReadChannel(1)
        val2 = ReadChannel(2)
        temper = read_temp_from_thermistor(val, r1)
        temperature = convert_to_temperature(adc_value)
        vol1 = convert_volts(adc_value)
        vol2 = convert_volts(val)
        vol3 = convert_volts(val2)
        print(f"Temperature: {temperature:.2f} C")
        print(f"Temperature2: {temper:.2f} C")
        print(f"vol temp: {vol1} C")
        print(f"vol temp2: {vol2} C")
        print(f"vol: {vol3} C")
        time.sleep(1)
except KeyboardInterrupt:
    spi.close()
    GPIO.cleanup()
