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
from bus_device import BusDevice
from digital_out import DigitalOut

class DummyDevice(BusDevice):

    def __init__(self,name):

        super().__init__(0,16)

        self.name=name

    def read(self,address):

        return 0

    def write(self,address,value):

        pass





bus = Bus()

manager = DeviceManager(bus)

print(manager)

led = DigitalOut(manager, "LED1")

print(len(manager))

adc = DummyDevice("ADC")

manager.add(adc)

print(adc.start)

adc = DummyDevice("ADC")

manager.add(adc)

print(adc.start)

# print(manager.get("ADC"))

# print(len(manager))

# manager.remove("ADC")

# print(len(manager))

# manager.clear()

# print(len(manager))

print(manager.next_address)

for p in manager:
    print(p)