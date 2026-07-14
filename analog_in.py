"""
EduMCU Core

016 - analog_in.py

Analog input peripheral.
"""

from peripheral import Peripheral
from analog_device import AnalogDevice


class AnalogIn(Peripheral):
    """
    Simulated Analog Input.

    The peripheral reads its value from a Signal object.
    """

    def __init__(self,
                 manager,
                 name):

        super().__init__(
            manager,
            AnalogDevice(name)
        )

        self.signal = None

    # ---------------------------------------------------------

    def load_signal(self, signal):
        """
        Attach a signal source.
        """

        self.signal = signal

    # ---------------------------------------------------------

    def unload_signal(self):
        """
        Remove the current signal.
        """

        self.signal = None

    # ---------------------------------------------------------

    def read(self):
        """
        Read ADC register.
        """

        self.runtime.advance_us(
        self.runtime.simulation_config.adc_read_us)


        return self.read_register()

    # ---------------------------------------------------------

    def read_voltage(self):
        """
        Read the input voltage.
        """

        self.runtime.advance_us(
        self.runtime.simulation_config.adc_read_us)


        return (
            self.read()
            / self.hardware.max_value
            * self.hardware.vref
        )

    # ---------------------------------------------------------

##    def simulate(self, value):
##        """
##        Directly force the ADC value.
##        Useful for simple tests.
##        """
##
##        self.hardware.write(
##            self.address,
##            value
##        )


##    def simulate(self, value):
##
##        self.write_register(value)

## N'UTILISE QUE DES VALEURS ENTRE 0 ET 4095 CE QUI N'EST PAS INSTINCYIF POUR L'UTILISATEUR

    def simulate(self, value):

        self.write_register(value)


    # ---------------------------------------------------------

    def simulate_voltage(self, voltage):
        """
        Simulate an input voltage.
        """

        voltage = max(
            0.0,
            min(voltage, self.hardware.vref)
        )

        adc = int(
            voltage
            / self.hardware.vref
            * self.hardware.max_value
        )

        self.write_register(adc)

    # ---------------------------------------------------------

    def update(self, runtime):
        """
        Update ADC according to simulation time.
        """

        if self.signal is None:
            return

        value = self.signal.sample(
            runtime.time_us
        )

        self.hardware.write(
            self.address,
            value
        )

    # ---------------------------------------------------------

    def reset(self):

        self.hardware.reset()

        if self.signal is not None:

            self.signal.reset()

    # ---------------------------------------------------------

    def __repr__(self):

        if self.signal is None:

            source = "None"

        else:

            source = self.signal.name

        return (
            f"AnalogIn("
            f"{self.name}, "
            f"signal={source})"
        )