"""
EduMCU Core

006 - device_manager.py

Peripheral memory manager.

Responsibilities
----------------
- Allocate memory addresses.
- Register peripherals on the bus.
- Retrieve peripherals by name.
- Remove peripherals.

EduMCU Core v1.0
"""

__version__ = "1.0"

##
##class DeviceManager:
##    """
##    Peripheral manager.
##    """
##
##    def __init__(self, bus, start_address=0x5000):
##
##        self.bus = bus
##
##        self.start_address = start_address
##        self.next_address = start_address
##
##        #
##        # périphériques indexés par leur nom
##        #
##        self.devices = {}
##
##    # ---------------------------------------------------------
##
##    def allocate_address(self, size):
##        """
##        Allocate a memory area.
##
##        Parameters
##        ----------
##        size : int
##            Device size in bytes.
##        """
##
##        address = self.next_address
##
##        self.next_address += size
##
##        return address
##
##    # ---------------------------------------------------------
##
##    def add(self, device):
##        """
##        Register a peripheral.
##        """
##
##        #
##        # allocation mémoire
##        #
##        device.start = self.allocate_address(
##            device.size
##        )
##
##        #
##        # connexion au bus
##        #
##        self.bus.attach(device)
##
##        #
##        # enregistrement par nom
##        #
##        if hasattr(device, "name"):
##
##            self.devices[device.name] = device
##
##        return device
##
##    # ---------------------------------------------------------
##
##    def get(self, name):
##        """
##        Return a peripheral from its name.
##        """
##
##        return self.devices.get(name)
##
##    # ---------------------------------------------------------
##
##    def remove(self, name):
##        """
##        Remove a peripheral.
##        """
##
##        device = self.devices.pop(name)
##
##        self.bus.detach(device)
##
##    # ---------------------------------------------------------
##
##    def clear(self):
##        """
##        Remove every peripheral.
##        """
##
##        for device in list(self.devices.values()):
##
##            self.bus.detach(device)
##
##        self.devices.clear()
##
##        self.next_address = self.start_address
##
##    # ---------------------------------------------------------
##
##    def __len__(self):
##
##        return len(self.devices)
##
##    # ---------------------------------------------------------
##
##    def __repr__(self):
##
##        lines = ["Device Manager"]
##
##        for name, device in self.devices.items():
##
##            lines.append(
##                f"{name:10s}"
##                f" -> "
##                f"0x{device.start:04X}"
##            )
##
##        return "\n".join(lines)



"""
EduMCU Core

006 - device_manager.py
"""

class DeviceManager:

    def __init__(self, bus):

        self.bus = bus

        self.next_address = 0x5000

        #
        # Hardware connected to the bus
        #
        self.devices = []

        #
        # User peripherals
        #
        self.peripherals = []

    # ---------------------------------------------------------

    def allocate_address(self):

        address = self.next_address

        self.next_address += 0x10

        return address

    # ---------------------------------------------------------

    def add(self, device):

        address = self.allocate_address()

        device.address = address
        device.start = address

        self.bus.attach(device)

        self.devices.append(device)

        return device

    # ---------------------------------------------------------

    def register(self, peripheral):

        self.peripherals.append(peripheral)

    # ---------------------------------------------------------

    def __iter__(self):

        return iter(self.peripherals)

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.peripherals)

    # ---------------------------------------------------------

    def reset(self):

        for device in self.devices:

            if hasattr(device, "reset"):

                device.reset()

        for peripheral in self.peripherals:

            if hasattr(peripheral, "reset"):

                peripheral.reset()