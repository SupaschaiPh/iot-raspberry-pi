import time
import spidev

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device (CS) 0
spi.max_speed_hz = 1350000  # MCP3208 can work up to 1.35 MHz
spi.mode = 0b01  # MCP3208 uses SPI mode 1

def read_channel(channel):
    """
    Read the specified channel from MCP3208 (0-7).

    :param channel: Channel number (0-7)
    :return: ADC value (0-4095)
    """
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")

    # Construct the request bytes
    request = [1, (8 + channel) << 4, 0]
    response = spi.xfer2(request)

    # Combine the result bytes
    data = ((response[1] & 3) << 8) + response[2]

    return data

# Example usage
if __name__ == "__main__":
    try:
        while True:
            for i in range(8):
                value = read_channel(i)
                print(f"Channel {i}: {value}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        spi.close()
