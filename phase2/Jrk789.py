```py
import time
import spidev
import math

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m' 

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

def print_color_graph(temp, label):
    temp_scaled = int(temp * 2)
    if temp < 10:
        color = colors.BLUE
    elif temp < 20:
        color = colors.GREEN
    elif temp < 30:
        color = colors.YELLOW
    else:
        color = colors.RED
    bar = color + "*" * temp_scaled + colors.ENDC
    print(f"{label}: |{bar: <50}| {temp:.2f}°C", end='\r')

while True:
    mcp_data = CalcTempMCPDegC(ReadChannel(1))
    therm_data = CalcTempThermisterDegC(ReadChannel(2))

    print("-" * 40)
    print("MCP3208 Sensor:")
    print(f"  - Reading: {mcp_data[0]}")
    print(f"  - Voltage: {mcp_data[1]:.2f}V")
    print_color_graph(mcp_data[2], "  - Temperature") 

    print("\nThermistor Sensor:")
    print(f"  - Reading: {therm_data[0]}")
    print(f"  - Voltage: {therm_data[1]:.2f}V")
    print_color_graph(therm_data[2], "  - Temperature") 
    
    time.sleep(0.5) 
```
