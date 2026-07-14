"""
EduMCU Core

003 - bus_device.py

Base class for all memory-mapped peripherals.

Responsibilities
----------------
- Store the peripheral memory range.
- Answer memory reads.
- Answer memory writes.

EduMCU Core v1.0
"""

__version__ = "1.0"


class BusDevice:
    """
    Base class for every memory-mapped peripheral.
    """

    def __init__(self, start=0, size=1):

        if size <= 0:
            raise ValueError("Device size must be greater than zero.")

        self.start = int(start)
        self.size = int(size)

    # ---------------------------------------------------------

    @property
    def end(self):
        """
        Last address occupied by the device.
        """
        return self.start + self.size - 1

    # ---------------------------------------------------------

    def contains(self, address):
        """
        Returns True if the address belongs to this device.
        """
        return self.start <= address <= self.end

    # ---------------------------------------------------------

    def read(self, address):
        """
        Read a value from the device.

        Must be overridden by subclasses.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__}.read() not implemented."
        )

    # ---------------------------------------------------------

    def write(self, address, value):
        """
        Write a value to the device.

        Must be overridden by subclasses.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__}.write() not implemented."
        )

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"(0x{self.start:04X}-0x{self.end:04X})"
        )