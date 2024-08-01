import time
import spidev
spi = spidev.SpiDev() # Open SPI bus
spi.open(0, 0)
def ReadChannel(channel): # read channel (0-7) from MCP3208
adc = spi.xfer2([4 + (channel >> 2), (channel & 3) << 6, 0])
#send the three bytes to the A/D in the format the A/D's datasheet explains
data = ((adc[1] & 15) << 8) + adc[2]
#use AND operation with the second byte to get the last 4 bits, and then make way
#for the third data byte with the "move 8 bits to left" << 8 operation
return data
