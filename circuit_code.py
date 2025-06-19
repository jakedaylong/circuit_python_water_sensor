''' SPDX-FileCopyrightText: 2018 Tony DiCola for Adafruit Industries
 SPDX-License-Identifier: MIT
 Simple example to send a message and then wait indefinitely for messages
 to be received.  This uses the default RadioHead compatible GFSK_Rb250_Fd250
 modulation and packet format for the radio.'''

import time
import board
import busio
import digitalio
import adafruit_rfm69

# Define radio parameters.
RADIO_FREQ_MHZ = 915  # Frequency of the radio in Mhz. Must match your

# module! Can be a value like 915.0, 433.0, etc.
# Define pins connected to the chip, use these if wiring up the breakout according to the guide:

# Or uncomment and instead use these if using a Feather M0 RFM69 board
# and the appropriate CircuitPython build:
# CS = digitalio.DigitalInOut(board.RFM69_CS)
# RESET = digitalio.DigitalInOut(board.RFM69_RST)
# Define the onboard LED

CS = digitalio.DigitalInOut(board.GP17)
RESET = digitalio.DigitalInOut(board.GP21)
LED = digitalio.DigitalInOut(board.LED)
LED.direction = digitalio.Direction.OUTPUT

# Initialize SPI bus.
spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)

# Initialze RFM radio
rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, RADIO_FREQ_MHZ)

# Optionally set an encryption key (16 byte AES key). MUST match both
# on the transmitter and receiver (or be set to None to disable/the default).
#rfm69.encryption_key = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
uart = busio.UART(tx=board.GP0, rx=board.GP1)

# Print out some chip state:
print(f"Temperature: {rfm69.temperature}C")
print(f"Frequency: {rfm69.frequency_mhz}mhz")
print(f"Bit rate: {rfm69.bitrate / 1000}kbit/s")
print(f"Frequency deviation: {rfm69.frequency_deviation}hz")

# Send a packet.  Note you can only send a packet up to 60 bytes in length.
# This is a limitation of the radio packet size, so if you need to send larger
# amounts of data you will need to break it into smaller send calls.  Each send
# call will wait for the previous one to finish before continuing.
rfm69.send(bytes("Hello world!\r\n", "utf-8"))
print("Sent hello world message!")

# Wait to receive packets.  Note that this library can't receive data at a fast
# rate, in fact it can only receive and process one 60 byte packet at a time.
# This means you should only use this for low bandwidth scenarios, like sending
# and receiving a single message at a time.
print("Sending packets...")

while True:
    # write command character via uart to sensor module for data.
    uart.write('j')

    # read sensor data from uart
    data = uart.read()
    print(str(data))

    # send recevied data from uart sensor over rfm69 radio
    rfm69.send(bytes(str(data), "utf-8"))

    #sleep radio and code for 2 seconds
    rfm69.sleep()
    time.sleep(2)
