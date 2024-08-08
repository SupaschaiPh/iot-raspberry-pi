import time
from LCD import LCD

# Initialize the LCD with specific parameters: Raspberry Pi revision, I2C address, and backlight status
lcd = LCD(2, 0x27, True)  # Using Raspberry Pi revision 2, I2C address 0x27, backlight enabled

def display(line1,line2):
    # Display messages on the LCD
    lcd.message(f"{line1}", 1)        # Display 'Hello World!' on line 1
    lcd.message(f"{line2}", 2)    # Display '    - Sunfounder' on line 2


# Keep the messages displayed for 5 seconds


# Clear the LCD display

def display_clear():
    lcd.clear()


if __name__ == "__main__":
    display_clear()
