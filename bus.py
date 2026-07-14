"""
EduMCU Core

004 - bus.py

Memory bus.

Responsibilities
----------------
- Attach memory-mapped devices.
- Detach devices.
- Find the device corresponding to an address.
- Route memory reads.
- Route memory writes.

The Bus knows nothing about the CPU,
the Scheduler or the peripherals.

EduMCU Core v1.0
"""

__version__ = "1.0"


class Bus:
    """
    Memory bus.
    """

    def __init__(self):

        self.devices = []

    # ---------------------------------------------------------

    def attach(self, device):
        """
        Attach a device to the memory bus.
        """

        # Vérifie qu'il n'y a pas de recouvrement mémoire
        for other in self.devices:

            overlap = (
                device.start <= other.end and
                device.end >= other.start
            )

            if overlap:

                raise ValueError(
                    f"Memory overlap between "
                    f"{device} and {other}"
                )

        self.devices.append(device)

    # ---------------------------------------------------------

    def detach(self, device):
        """
        Remove a device from the bus.
        """

        if device in self.devices:

            self.devices.remove(device)

    # ---------------------------------------------------------

    def find(self, address):
        """
        Return the device mapped at the given address.
        """

        for device in self.devices:

            if device.contains(address):

                return device

        raise ValueError(
            f"No device mapped at address 0x{address:04X}"
        )

    # ---------------------------------------------------------

    def read(self, address):
        """
        Read from the memory bus.
        """

        device = self.find(address)

        return device.read(address)

    # ---------------------------------------------------------

    def write(self, address, value):
        """
        Write to the memory bus.
        """

        device = self.find(address)

        device.write(address, value)

    # ---------------------------------------------------------

    def clear(self):
        """
        Remove all devices.
        """

        self.devices.clear()

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.devices)

    # ---------------------------------------------------------

    def __repr__(self):

        lines = ["Memory Bus"]

        for device in self.devices:

            lines.append(
                f"0x{device.start:04X} - "
                f"0x{device.end:04X} : "
                f"{device.__class__.__name__}"
            )

        return "\n".join(lines)