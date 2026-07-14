"""
EduMCU Core

009 - peripheral.py

Base class for all user peripherals.

Responsibilities
----------------
- Own the hardware device.
- Register it into the DeviceManager.
- Expose common properties.

EduMCU Core v1.0
"""

__version__ = "1.0"


##class Peripheral:
##    """
##    Base class for all peripherals.
##    """
##
##    def __init__(self, manager, hardware):
##
##        self.manager = manager
##
##        self.bus = manager.bus
##
##        self.hardware = hardware
##
##        #
##        # Register the hardware
##        #
##        manager.add(hardware)
##
##        manager.register(self)
##
##        #
##        # Useful shortcuts
##        #
##        self.name = hardware.name
##
##        self.address = hardware.start


class Peripheral:

    def __init__(self, manager, hardware):

        self.manager = manager

        self.bus = manager.bus

        self.hardware = hardware

        manager.add(hardware)

        manager.register(self)

        self.name = hardware.name

        self.address = hardware.start

    # ---------------------------------------------------------

    @property
    def size(self):

        return self.hardware.size

    @property # TOUS LES PERIPHERIQUES ONT ACCES A LA RUNTIME
    def runtime(self):

        return self.manager.runtime

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset the peripheral.
        """

        if hasattr(self.hardware, "reset"):

            self.hardware.reset()

    # ---------------------------------------------------------

    def read_register(self, offset=0):
        """
        Read one hardware register.
        """

        return self.bus.read(
            self.address + offset
        )

    # ---------------------------------------------------------

    def write_register(self, value, offset=0):
        """
        Write one hardware register.
        """

        self.bus.write(
            self.address + offset,
            value
        )

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"{self.__class__.__name__}"
            f"("
            f"{self.name}, "
            f"0x{self.address:04X}"
            f")"
        )