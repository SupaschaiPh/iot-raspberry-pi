import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

#GPIO.cleanup() 

def ReadChannel(channel):
    r = spi.xfer2([4 | 2 | (channel >> 2), (channel & 3) << 6, 0])
    return ((r[1] & 15) << 8) + r[2]


if __name__ == "__main__":
    while True:
        print(ReadChannel(0))

