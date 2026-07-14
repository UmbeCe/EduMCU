"""
EduMCU Core

020 - pwm_out.py
"""

from peripheral import Peripheral
from pwm_device import PwmDevice


class PwmOut(Peripheral):
    """
    Simulated PWM output.
    """

    def __init__(self,
                 manager,
                 name):

        super().__init__(
            manager,
            PwmDevice(name)
        )

    # ---------------------------------------------------------

    def write(self, duty_cycle):
        """
        Set duty cycle (0.0 -> 1.0).
        """

        self.runtime.advance_us(
        self.runtime.simulation_config.pwm_write_us)

        self.hardware.write(
            self.address,
            duty_cycle
        )

    # ---------------------------------------------------------

    def read(self):

        return self.hardware.read(
            self.address
        )

    # ---------------------------------------------------------

    def enable(self):

        self.hardware.enable()

    # ---------------------------------------------------------

    def disable(self):

        self.hardware.disable()

    # ---------------------------------------------------------

    def frequency(self, hz):

        self.hardware.set_frequency(hz)

    # ---------------------------------------------------------

    def period_us(self, period_us):

        if period_us <= 0:

            raise ValueError("Period must be > 0")

        self.frequency(
            1_000_000.0 / period_us
        )

    # ---------------------------------------------------------

    def period_ms(self, period_ms):

        self.period_us(
            period_ms * 1000.0
        )

    # ---------------------------------------------------------

    def level(self):
        """
        Current logic level.
        """

        return self.hardware.level

    # ---------------------------------------------------------

    def update(self, runtime):
        """
        Update PWM output according to simulated time.
        """

        if not self.hardware.enabled:

            self.hardware.level = 0
            return

        frequency = self.hardware.get_frequency()

        if frequency <= 0:

            self.hardware.level = 0
            return

        period_us = 1_000_000.0 / frequency

        t = runtime.time_us % period_us

        high_time = self.hardware.duty_cycle * period_us

        self.hardware.level = 1 if t < high_time else 0

    # ---------------------------------------------------------

    def reset(self):

        self.hardware.reset()

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"PwmOut("
            f"{self.name}, "
            f"{self.hardware.get_frequency():.0f} Hz, "
            f"duty={self.read():.2f})"
        )