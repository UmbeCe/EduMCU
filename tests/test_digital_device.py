"""
Test EduMCU Core function

"""

# To import the EduMCU Core from root file
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(__file__)
    )
)





from digital_device import DigitalDevice

gpio = DigitalDevice("LED1")

print(gpio)

print(gpio.read(0))

gpio.write(0, 1)

print(gpio.read(0))

gpio.write(0, 0)

print(gpio.read(0))

gpio.write(0, 42)

print(gpio.read(0))

gpio.reset()

print(gpio.read(0))