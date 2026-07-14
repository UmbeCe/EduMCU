"""
EduMCU Core

simulation_config.py
"""


class SimulationConfig:
    """
    Global simulation parameters.
    """


    def __init__(self):

        # Duration of one simulation quantum.
        self.quantum_us = 10.0

        # Enable debug information
        self.debug = False

        # Maximum number of scheduler callbacks
        # executed during one update.

        #
        # Peripheral timings
        #

        self.gpio_read_us = 0.05
        self.gpio_write_us = 0.05

        self.adc_read_us = 3.0

        self.pwm_write_us = 0.2

        self.serial_write_us = 0.2