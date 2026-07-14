"""
EduMCU Core

018 - timer.py
"""

class Timer:
    """
    Simulation timer based on Runtime.time_us.
    """

    def __init__(self, runtime, name="Timer"):

        self.runtime = runtime

        self.name = name

        self.running = False

        self.start_time = 0.0

    # ---------------------------------------------------------

##    def start(self):
##        """
##        Start the timer.
##        """
##
##        if not self.running:
##
##            self.start_time = self.runtime.time_us
##
##            self.running = True

    def start(self, duration_us = 100000000):

        self.start_us(duration_us)

        if duration_us is not None:

            self.duration = duration_us

            self.start_time = self.runtime.time_us

            self.running = True

    # ---------------------------------------------------------

    def start_us(self, duration_us):

        self.duration = duration_us

        self.start_time = self.runtime.time_us

        self.running = True

    # ---------------------------------------------------------

    def start_ms(self, duration_ms):
        self.start_us(duration_ms * 1000)

    # ---------------------------------------------------------

    def start_s(self, duration_s):
        self.start_us(duration_s * 1_000_000)

    # ---------------------------------------------------------

    def stop(self):
        """
        Stop the timer.
        """

        self.running = False

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset the timer.
        """

        self.start_time = self.runtime.time_us

    # ---------------------------------------------------------

    def restart(self):
        """
        Restart the timer.
        """

        self.start_time = self.runtime.time_us

        self.running = True

    # ---------------------------------------------------------

    def elapsed_us(self):
        """
        Elapsed time in microseconds.
        """

        if not self.running:

            return 0.0

        return self.runtime.time_us - self.start_time

    # ---------------------------------------------------------

    def elapsed_ms(self):
        """
        Elapsed time in milliseconds.
        """

        return self.elapsed_us() / 1000.0

    # ---------------------------------------------------------

    def elapsed_s(self):
        """
        Elapsed time in seconds.
        """

        return self.elapsed_us() / 1_000_000.0

    # ---------------------------------------------------------

    def expired(self):
        """
        Return True if the timer has expired.
        """

        if not self.running:
            return False

        return (
            self.runtime.time_us - self.start_time
            >= self.duration
        )

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"Timer("
            f"{self.name}, "
            f"{self.elapsed_us():.3f} us)"
        )
