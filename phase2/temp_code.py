import time
import spidev
import math

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

#GPIO.cleanup() 

def ReadChannel(channel):
    r = spi.xfer2([4 | 2 | (channel >> 2), (channel & 3) << 6, 0])
    return ((r[1] & 15) << 8) + r[2]

def CalcTempMCPDegC(reading):
    voltage = reading * 3.3 / 4095
    return reading, voltage, 100 * (voltage - 1) + 50

def CalcTempThermisterDegC(reading):
    voltage = reading * 3.3 / 4095
    resistance = (voltage * 10000) / (3.3 - voltage)
    tempK = (298.15 * 4050) / (298.15 * math.log(resistance / 10000) + 4050)
    tempC = tempK - 273.15
    return reading, voltage, tempC

def temp():
    mcp_data = CalcTempMCPDegC(ReadChannel(1))
    therm_data = CalcTempThermisterDegC(ReadChannel(2))

    print(f"Temp Sensor ==\tReading: {mcp_data[0]}\tVoltage: {mcp_data[1]:.2f}V\tTemp: {mcp_data[2]:.2f} Celsius",end="")
    print(f"\t\tThermistor Sensor ==\tReading: {therm_data[0]}\tVoltage: {therm_data[1]:.2f}V\tTemp: {therm_data[2]:.2f} Celsius")
     
    time.sleep(0.5) 

if __name__ == "__main__":
    while True:
        temp()

