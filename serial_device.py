"""
EduMCU Core

021 - serial_device.py
"""

from bus_device import BusDevice


class SerialDevice(BusDevice):
    """
    Simulated UART hardware.
    """

    def __init__(self, name):

        super().__init__(0, 1)

        self.name = name

        self.enabled = False

        self.baudrate = 115200

        self.tx_buffer = []

        self.rx_buffer = []

        self.tx_ready = True

        self.rx_ready = False

    # ---------------------------------------------------------

    def enable(self):

        self.enabled = True

    # ---------------------------------------------------------

    def disable(self):

        self.enabled = False

    # ---------------------------------------------------------

    def set_baudrate(self, baudrate):

        self.baudrate = int(baudrate)

    # ---------------------------------------------------------

    def get_baudrate(self):

        return self.baudrate

    # ---------------------------------------------------------

    def write(self, address, value):
        """
        Write one byte to the TX buffer.
        """

        value = int(value) & 0xFF

        self.tx_buffer.append(value)

        self.tx_ready = False

    # ---------------------------------------------------------

    def read(self, address):
        """
        Read one byte from the RX buffer.
        """

        if not self.rx_buffer:

            self.rx_ready = False

            return None

        value = self.rx_buffer.pop(0)

        self.rx_ready = len(self.rx_buffer) > 0

        return value

    # ---------------------------------------------------------

    def receive(self, value):
        """
        Simulate reception of one byte.
        """

        value = int(value) & 0xFF

        self.rx_buffer.append(value)

        self.rx_ready = True

    # ---------------------------------------------------------

    def transmit(self):
        """
        Simulate transmission of one byte.
        """

        if not self.tx_buffer:

            self.tx_ready = True

            return None

        value = self.tx_buffer.pop(0)

        self.tx_ready = len(self.tx_buffer) == 0

        return value

    # ---------------------------------------------------------

    def available(self):

        return len(self.rx_buffer)

    # ---------------------------------------------------------

    def reset(self):

        self.enabled = False

        self.baudrate = 115200

        self.tx_buffer.clear()

        self.rx_buffer.clear()

        self.tx_ready = True

        self.rx_ready = False

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"SerialDevice("
            f"{self.name}, "
            f"{self.baudrate} baud, "
            f"TX={len(self.tx_buffer)}, "
            f"RX={len(self.rx_buffer)}, "
            f"enabled={self.enabled})"
        )