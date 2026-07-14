"""
EduMCU Core

022 - serial.py
"""

from peripheral import Peripheral
from serial_device import SerialDevice


class Serial(Peripheral):
    """
    Simulated UART peripheral.
    """

    def __init__(self,
                 manager,
                 name):

        super().__init__(
            manager,
            SerialDevice(name)
        )

    # ---------------------------------------------------------

    def enable(self):

        self.hardware.enable()

    # ---------------------------------------------------------

    def disable(self):

        self.hardware.disable()

    # ---------------------------------------------------------

    def baudrate(self, baud):

        self.hardware.set_baudrate(baud)

    # ---------------------------------------------------------

    def write(self, text):
        """
        Send a string.
        """
        self.runtime.advance_us(
        self.runtime.simulation_config.serial_write_us)
        for c in str(text):

            self.hardware.write(
                self.address,
                ord(c)
            )

    # ---------------------------------------------------------

    def println(self, text):

        self.write(str(text) + "\n")

    # ---------------------------------------------------------

    def read(self):
        """
        Read all available characters.
        """

        chars = []

        while self.available():

            value = self.hardware.read(
                self.address
            )

            if value is not None:

                chars.append(chr(value))

        return "".join(chars)

    # ---------------------------------------------------------

    def available(self):

        return self.hardware.available()

    # ---------------------------------------------------------

    def receive(self, text):
        """
        Inject received characters (simulation helper).
        """

        for c in str(text):

            self.hardware.receive(ord(c))

    # ---------------------------------------------------------

    def reset(self):

        self.hardware.reset()

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"Serial("
            f"{self.name}, "
            f"{self.hardware.get_baudrate()} baud)"
        )