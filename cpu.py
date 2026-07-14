"""
EduMCU Core

005 - cpu.py

Virtual CPU.

Responsibilities
----------------
- Own the CPU clock.
- Own the memory bus.
- Count executed CPU cycles.

The CPU does NOT emulate an ARM Cortex.
It is only responsible for advancing the
simulation one CPU cycle at a time.

EduMCU Core v1.0
"""

__version__ = "1.0"


class CPU:
    """
    Virtual CPU.
    """

    def __init__(self, clock, bus):

        self.clock = clock
        self.bus = bus

        self.running = False
        self.cycles = 0

    # ---------------------------------------------------------

    @property
    def frequency(self):
        """
        CPU frequency in Hz.
        """
        return self.clock.frequency

    # ---------------------------------------------------------

    @property
    def time_us(self):
        """
        Elapsed simulated CPU time.
        """
        return self.clock.cycles_to_microseconds(
            self.cycles
        )

    # ---------------------------------------------------------

    def start(self):
        """
        Start the CPU.
        """
        self.running = True

    # ---------------------------------------------------------

    def stop(self):
        """
        Stop the CPU.
        """
        self.running = False

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset the CPU.
        """
        self.cycles = 0

    # ---------------------------------------------------------

    def step(self):
        """
        Execute one CPU cycle.
        """

        if not self.running:
            return

        self.cycles += 1

    # ---------------------------------------------------------

    def advance(self, cycles):
        """
        Advance the CPU by several cycles.
        """

        if not self.running:
            return

        self.cycles += cycles

    # ---------------------------------------------------------

    def read(self, address):
        """
        Read a value through the memory bus.
        """
        return self.bus.read(address)

    # ---------------------------------------------------------

    def write(self, address, value):
        """
        Write a value through the memory bus.
        """
        self.bus.write(address, value)

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"CPU("
            f"{self.frequency/1e6:.1f} MHz, "
            f"cycles={self.cycles})"
        )