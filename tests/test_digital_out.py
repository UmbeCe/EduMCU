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
from digital_out import DigitalOut

bus = Bus()
manager = DeviceManager(bus)

led = DigitalOut(manager, "LED1")

print(led)

led.write(1)

print(led.read())

led.off()

print(led.read())

led.on()

print(led.read())

led.toggle()

print(led.read())

led.toggle()

print(led.read())

print(bool(led))

led.off()

print(bool(led))