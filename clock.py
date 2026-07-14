"""
EduMCU Core

001 - clock.py

Virtual CPU clock.

Responsibilities
----------------
- Store CPU frequency.
- Convert cycles to time.
- Convert time to cycles.

The Clock does not advance time.
Time progression is handled by the Scheduler.

EduMCU Core v1.0
"""

__version__ = "1.0"


class Clock:
    """
    Virtual CPU clock.

    Parameters
    ----------
    frequency : int
        CPU frequency in Hertz.
    """

    def __init__(self, frequency=48_000_000):

        if frequency <= 0:
            raise ValueError("Clock frequency must be positive.")

        self._frequency = int(frequency)

    # -------------------------------------------------
    # Properties
    # -------------------------------------------------

    @property
    def frequency(self):
        """CPU frequency in Hz."""
        return self._frequency

    @property
    def period(self):
        """
        Duration of one CPU cycle in seconds.
        """
        return 1.0 / self._frequency

    # -------------------------------------------------
    # Conversions
    # -------------------------------------------------

    def cycles_to_seconds(self, cycles):
        """
        Convert CPU cycles to seconds.
        """
        return cycles / self._frequency

    def cycles_to_microseconds(self, cycles):
        """
        Convert CPU cycles to microseconds.
        """
        return self.cycles_to_seconds(cycles) * 1_000_000

    def seconds_to_cycles(self, seconds):
        """
        Convert seconds to CPU cycles.
        """
        return round(seconds * self._frequency)

    def microseconds_to_cycles(self, microseconds):
        """
        Convert microseconds to CPU cycles.
        """
        return self.seconds_to_cycles(
            microseconds / 1_000_000
        )

    # -------------------------------------------------

    def __str__(self):

        return f"Clock({self.frequency} Hz)"

    def __repr__(self):

        return str(self)