"""
EduMCU Core

014 - signal.py

Base class for all signal generators.
"""

__version__ = "1.0"


class Signal:
    """
    Base class for all analog signal sources.
    """

    def __init__(self, name="Signal"):

        self.name = name

    # ---------------------------------------------------------

    def sample(self, time_us):
        """
        Return the signal value at the given simulation time.

        Must be implemented by subclasses.
        """
        raise NotImplementedError(
            "sample(time_us) must be implemented."
        )

    # ---------------------------------------------------------

    def reset(self):
        """
        Reset the signal state.

        Stateless signals do nothing.
        """
        pass

    # ---------------------------------------------------------

    def __repr__(self):

        return f"{self.__class__.__name__}({self.name})"