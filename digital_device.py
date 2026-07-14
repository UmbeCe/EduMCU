"""
EduMCU Core

010 - digital_device.py

Memory-mapped digital I/O device.

Responsibilities
----------------
- Store one digital value.
- Respond to bus read/write operations.

EduMCU Core v1.0
"""

__version__ = "1.0"

from bus_device import BusDevice


class DigitalDevice(BusDevice):
    """
    Digital hardware device.
    """

    def __init__(self, name):

        # 1 registre mémoire
        super().__init__(0, 1)

        self.name = name

        self.value = 0

    # ---------------------------------------------------------

    def read(self, address):

        return self.value

    # ---------------------------------------------------------

    def write(self, address, value):

        self.value = 1 if value else 0

    # ---------------------------------------------------------

    def reset(self):

        self.value = 0

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"DigitalDevice("
            f"{self.name}, "
            f"value={self.value})"
        )