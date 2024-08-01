import spidev
import time

# Create an SPI object
spi = spidev.SpiDev()

# Open SPI bus 0, device (CS) 0
spi.open(0, 0)

# Set SPI speed (in Hz)
spi.max_speed_hz = 50000

# Set SPI mode (0, 1, 2, or 3)
spi.mode = 0

# Function to read data from a specific channel
def read_channel(channel):
    # Ensure channel is between 0 and 7
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")

    # MCP3008 specific command to read data
    # Start bit, single-ended bit, and 3 bits of channel number
    start_bit = 0x01
    single_ended = 0x08
    channel_command = start_bit | (single_ended | (channel >> 2))

    # Create command bytes
    command = [channel_command, (channel & 0x03) << 6, 0x00]

    # Send command and receive response
    response = spi.xfer2(command)

    # Combine response bytes
    adc_out = ((response[1] & 0x03) << 8) | response[2]
    return adc_out

try:
    while True:
        # Read from channel 0
        channel_0_value = read_channel(0)
        print(f"Channel 0 value: {channel_0_value}")

        # Read from channel 1
        channel_1_value = read_channel(1)
        print(f"Channel 1 value: {channel_1_value}")

        # Sleep for a bit
        time.sleep(1)

except KeyboardInterrupt:
    # Close SPI connection on interrupt
    spi.close()
