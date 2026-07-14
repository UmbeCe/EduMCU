"""
EduMCU Core

011 - digital_out.py

Digital output peripheral.

Responsibilities
----------------
- Provide a simple API for a digital output.

EduMCU Core v1.0
"""

__version__ = "1.0"

from peripheral import Peripheral
from digital_device import DigitalDevice


class DigitalOut(Peripheral):
    """
    Digital output peripheral.
    """

    def __init__(self, manager, name):

        super().__init__(
            manager,
            DigitalDevice(name)
        )

    # ---------------------------------------------------------

    def write(self, value):
        """
        Write a digital value.
        """
        self.runtime.advance_us(
        self.runtime.simulation_config.gpio_write_us)

        self.write_register(
            1 if value else 0
        )

    # ---------------------------------------------------------

    def read(self):
        """
        Read the current output state.
        """
        self.runtime.advance_us(
        self.runtime.simulation_config.gpio_read_us)

        return self.read_register()

    # ---------------------------------------------------------

    def on(self):
        """
        Set output HIGH.
        """

        self.write(1)

    # ---------------------------------------------------------

    def off(self):
        """
        Set output LOW.
        """

        self.write(0)

    # ---------------------------------------------------------

    def toggle(self):
        """
        Toggle the output state.
        """

        self.write(
            not self.read()
        )

    # ---------------------------------------------------------

    def __bool__(self):

        return bool(self.read())

    # ---------------------------------------------------------

    def __repr__(self):

        state = "HIGH" if self.read() else "LOW"

        return (
            f"DigitalOut("
            f"{self.name}, "
            f"{state})"
        )