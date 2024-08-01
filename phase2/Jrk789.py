import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000 # Set SPI clock speed to 1MHz

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

def CalcTempDegC(reading):
    voltage = reading * 3.3 / 4095  # Corrected calculation: 4095 for 12-bit ADC
    return (reading, voltage,100*(voltage-1)+50)


while True:
    mcp = CalcTempDegC(ReadChannel(1))
    thermister = CalcTempDegC(ReadChannel(2))
    print("Reading = %d\tVoltage = %.2fV\tTemperature = %.2f degC || Reading = %d Voltage = %.2fV Temperature = %.2f degC" % (mcp[0], mcp[1], mcp[2], thermister[0], thermister[1], thermister[2]))
    time.sleep(0.1) 
