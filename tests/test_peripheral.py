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
from bus_device import BusDevice
from device_manager import DeviceManager
from peripheral import Peripheral


class DummyDevice(BusDevice):
    """
    Simple hardware used only for testing Peripheral.
    """

    def __init__(self):

        super().__init__(0, 1)

        self.name = "Dummy"

        self.value = 0

    def read(self, address):

        return self.value

    def write(self, address, value):

        self.value = value

    def reset(self):

        self.value = 0


# -----------------------------------------------------------------

bus = Bus()

manager = DeviceManager(bus)

hardware = DummyDevice()

peripheral = Peripheral(manager, hardware)

# -----------------------------------------------------------------

print("Nom :", peripheral.name)

print("Adresse :", hex(peripheral.address))

print("Nombre de périphériques :", len(manager))

print(peripheral)