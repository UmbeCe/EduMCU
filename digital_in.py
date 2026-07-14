"""
EduMCU Core

012 - digital_in.py

Digital input peripheral.

Responsibilities
----------------
- Read a digital input.
- Allow simulation of an external signal.

EduMCU Core v1.0
"""

__version__ = "1.0"

from peripheral import Peripheral
from digital_device import DigitalDevice


class DigitalIn(Peripheral):
    """
    Digital input peripheral.
    """

    def __init__(self, manager, name):

        super().__init__(
            manager,
            DigitalDevice(name)
        )

    # ---------------------------------------------------------

    def read(self):
        """
        Read the input level.
        """
        self.runtime.advance_us(
        self.runtime.simulation_config.gpio_read_us)

        return self.read_register()


    # ---------------------------------------------------------

    def simulate(self, value):
        """
        Simulate an external digital signal.
        """

        self.hardware.write(
            self.address,
            1 if value else 0
        )

    # ---------------------------------------------------------

    def is_high(self):
        """
        Return True if HIGH.
        """

        return self.read() == 1

    # ---------------------------------------------------------

    def is_low(self):
        """
        Return True if LOW.
        """

        return self.read() == 0

    # ---------------------------------------------------------

    def __bool__(self):

        return bool(self.read())

    # ---------------------------------------------------------

    def __repr__(self):

        state = "HIGH" if self.read() else "LOW"

        return (
            f"DigitalIn("
            f"{self.name}, "
            f"{state})"
        )