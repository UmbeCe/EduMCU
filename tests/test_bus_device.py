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




from bus_device import BusDevice

device = BusDevice(start=0x4000, size=16)

print(device)
print(device.start)
print(device.end)
print(device.size)

print(device.contains(0x4000))
print(device.contains(0x4005))
print(device.contains(0x400F))
print(device.contains(0x4010))