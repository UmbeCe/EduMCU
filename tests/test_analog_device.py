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

from analog_device import AnalogDevice

adc = AnalogDevice("A0")

print(adc)

adc.write(0, 1234)

print(adc.read(0))

adc.write(0, -50)

print(adc.read(0))

adc.write(0, 5000)

print(adc.read(0))

adc.reset()

print(adc.read(0))