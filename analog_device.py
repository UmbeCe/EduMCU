"""
EduMCU Core

013 - analog_device.py

Memory-mapped analog input device.

Responsibilities
----------------
- Store one ADC value.
- Respond to bus read/write operations.

EduMCU Core v1.0
"""

__version__ = "1.0"

from bus_device import BusDevice


class AnalogDevice(BusDevice):
    """
    Analog hardware device.
    """

##    def __init__(self,
##                 name,
##                 resolution=12):
##
##        super().__init__(0, 2)
##
##        self.name = name
##
##        self.resolution = resolution
##
##        self.maximum = (1 << resolution) - 1
##
##        self.value = 0


    def __init__(self,
                 name,
                 resolution=12,
                 vref=3.3):

        super().__init__(0, 2)

        self.name = name

        self.resolution = resolution

        self.max_value = (1 << resolution) - 1

        self.vref = vref

        self.value = 0

    # ---------------------------------------------------------

    def read(self, address):

        return self.value

    # ---------------------------------------------------------

    def write(self, address, value):

        if value < 0:
            value = 0

        if value > self.max_value:
            value = self.max_value

        self.value = int(value)

    # ---------------------------------------------------------

    def reset(self):

        self.value = 0

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"AnalogDevice("
            f"{self.name}, "
            f"{self.value}/{self.max_value})"
        )