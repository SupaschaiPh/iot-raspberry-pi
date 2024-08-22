import spidev
import time

# SPI configuration (adjust as needed)
spi_bus = 0
spi_device = 0
spi_speed = 1000000  # Hz

# Create an SPI object and open the connection
spi = spidev.SpiDev()
spi.open(spi_bus, spi_device)
spi.max_speed_hz = spi_speed


def ReadChannel( channel):
  """Reads a value from the specified SPI channel.

  Args:
    spi: An open spidev object.
    channel: The channel to read from (0-7).

  Returns:
    The read value as an integer (0-1023), or None on error.
  """

  if channel < 0 or channel > 7:
    print("Invalid channel selection.")
    return None

  # Construct the SPI message
  #  First byte: Start bit (1) + Single-ended mode (1) + Channel selection (3 bits) 
  #  Second and third bytes: Don't care for reading
  msg = [(0b10000000 | (channel << 4)), 0x00, 0x00]
  
  try:
    # Send the message and receive the response
    response = spi.xfer2(msg)

    # Extract the data bits from the response
    # Discard first byte, combine next two bytes for 10-bit resolution
    adc_value = ((response[1] & 0x0F) << 8) | response[2]
    return adc_value

  except Exception as e:
    print("Error reading SPI:", e)
    return None



