"""
EduMCU Core

019 - pwm_device.py
"""

from bus_device import BusDevice


class PwmDevice(BusDevice):
    """
    Simulated PWM hardware.

    Stores the configuration and current output level.
    """

    def __init__(self, name):

        super().__init__(0, 1)

        self.name = name

        self.enabled = False

        self.frequency = 1000.0      # Hz

        self.duty_cycle = 0.0        # 0.0 → 1.0

        self.level = 0               # current output level (0/1)

    # ---------------------------------------------------------

    def enable(self):

        self.enabled = True

    # ---------------------------------------------------------

    def disable(self):

        self.enabled = False

        self.level = 0

    # ---------------------------------------------------------

    def write(self, address, value):
        """
        Set duty cycle.

        Value is clamped between 0 and 1.
        """

        value = float(value)

        if value < 0.0:
            value = 0.0

        elif value > 1.0:
            value = 1.0

        self.duty_cycle = value

    # ---------------------------------------------------------

    def read(self, address):

        return self.duty_cycle

    # ---------------------------------------------------------

    def set_frequency(self, frequency):

        self.frequency = float(frequency)

    # ---------------------------------------------------------

    def get_frequency(self):

        return self.frequency

    # ---------------------------------------------------------

    def reset(self):

        self.enabled = False

        self.frequency = 1000.0

        self.duty_cycle = 0.0

        self.level = 0

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"PwmDevice("
            f"{self.name}, "
            f"{self.frequency:.0f} Hz, "
            f"duty={self.duty_cycle:.2f}, "
            f"level={self.level}, "
            f"enabled={self.enabled})"
        )