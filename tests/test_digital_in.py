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





from bus import Bus
from device_manager import DeviceManager
from digital_in import DigitalIn

bus = Bus()
manager = DeviceManager(bus)

button = DigitalIn(manager, "SW1")

print(button)

button.simulate(1)

print(button.read())

print(button.is_high())

print(button.is_low())

button.simulate(0)

print(button.read())

button.simulate(0)

print(button.read())

print(bool(button))

button.simulate(1)

print(bool(button))