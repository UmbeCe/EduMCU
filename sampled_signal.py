"""
EduMCU Core

015 - sampled_signal.py

Sampled analog signal.

A SampledSignal stores a sequence of ADC samples acquired at a fixed
sampling frequency.

The signal is deterministic:
the returned sample depends only on the simulation time.
"""

from signal_analog import Signal


class SampledSignal(Signal):

    def __init__(self,
                 samples,
                 sample_rate,
                 loop=False,
                 name="SampledSignal"):

        super().__init__(name)

        self.samples = list(samples)

        self.sample_rate = float(sample_rate)

        self.loop = loop

    # ---------------------------------------------------------

    @property
    def sample_period_us(self):
        """
        Sampling period in microseconds.
        """

        return 1_000_000.0 / self.sample_rate

    # ---------------------------------------------------------

    @property
    def duration_us(self):
        """
        Total signal duration.
        """

        return len(self.samples) * self.sample_period_us

    # ---------------------------------------------------------

    def sample(self, time_us):
        """
        Return the sample corresponding to simulation time.
        """

        if len(self.samples) == 0:
            return 0

        index = int(
            time_us / self.sample_period_us
        )

        if self.loop:
            index %= len(self.samples)

        if index < 0:
            index = 0

        if index >= len(self.samples):
            return self.samples[-1]

        return self.samples[index]

    # ---------------------------------------------------------

    def reset(self):
        """
        Stateless signal.
        """
        pass

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.samples)

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"SampledSignal("
            f"{len(self.samples)} samples, "
            f"{self.sample_rate:.0f} Hz)"
        )