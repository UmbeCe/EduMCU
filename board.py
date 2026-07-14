"""
EduMCU Core

023 - board.py
"""

from clock import Clock
from bus import Bus
from cpu import CPU

from scheduler import Scheduler
from runtime import Runtime
from simulation_config import SimulationConfig

from device_manager import DeviceManager

from digital_out import DigitalOut
from digital_in import DigitalIn

from analog_in import AnalogIn

from pwm_out import PwmOut

from serial import Serial

from timer import Timer


class Board:
    """
    Main EduMCU board.
    """

    # ---------------------------------------------------------

    def __init__(self,
                 frequency=48_000_000,
                 quantum_us=None
                 ):

        #
        # Core
        #

        self.clock = Clock(frequency)

        self.bus = Bus()

        self.cpu = CPU(
            self.clock,
            self.bus
        )

        self.manager = DeviceManager(
            self.bus
        )

        self.scheduler = Scheduler()

        self.simulation_config = SimulationConfig()

        if quantum_us is None:

            quantum_us = self.simulation_config.quantum_us

        else:

            quantum_us = quantum_us




##        self.runtime = Runtime(
##            self.cpu,
##            self.manager,
##            self.scheduler
##        )



        self.runtime = Runtime(
            self.cpu,
            self.manager,
            self.scheduler,
            quantum_us=quantum_us,
            simulation_config=self.simulation_config
        )

        #
        # Maintenant le runtime existe
        #
        self.manager.runtime = self.runtime


        #
        # User timers
        #

        self.timers = []

        #
        # Start CPU
        #

        self.cpu.start()

    # ---------------------------------------------------------
    # Execution
    # ---------------------------------------------------------

    def step(self):

        self.runtime.step()

    # ---------------------------------------------------------

    def tick(self):

        self.runtime.tick()

    # ---------------------------------------------------------

    def run(self, steps):

        self.runtime.run(steps)

    # ---------------------------------------------------------

    def run_us(self, us):

        self.runtime.run_us(us)

    # ---------------------------------------------------------

    def run_ms(self, ms):

        self.runtime.run_ms(ms)

    # ---------------------------------------------------------

    def delay_ms(self, ms):

        """
        Alias de la fonction run_ms()
        """
        self.runtime.run_ms(ms)


    # ---------------------------------------------------------

    def delay_us(self, us):

        """
        Alias de la fonction run_us()
        """
        self.runtime.run_us(us)


    # ---------------------------------------------------------

    def run_s(self, seconds):

        self.runtime.run_s(seconds)

    # ---------------------------------------------------------

    def reset(self):

        self.runtime.reset()

    # ---------------------------------------------------------

    def wait_ms(self, ms):
        """
        Advance the simulation by a given duration.
        """
        self.run_ms(ms)





    # ---------------------------------------------------------
    # Scheduler helpers
    # ---------------------------------------------------------

    def every_us(self,
                 period,
                 callback):

        self.scheduler.every_us(
            period,
            callback
        )

    # ---------------------------------------------------------

    def every_ms(self,
                 period,
                 callback):

        self.scheduler.every_ms(
            period,
            callback
        )


    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def cycles(self):

        return self.cpu.cycles

    # ---------------------------------------------------------
    @property
    def time_ms(self):

        return self.runtime.time_ms

    # ---------------------------------------------------------

    @property
    def time_s(self):

        return self.runtime.time_s


    # ---------------------------------------------------------

    @property
    def time_us(self):

        return self.runtime.time_us


    # ---------------------------------------------------------

    @property
    def quantum_us(self):
        return self.runtime.quantum_us


    # ---------------------------------------------------------

    @quantum_us.setter
    def quantum_us(self, value):
        self.runtime.quantum_us = value


    # ---------------------------------------------------------
    # Peripherals
    # ---------------------------------------------------------

    def DigitalOut(self, name):

        return DigitalOut(
            self.manager,
            name
        )

    # ---------------------------------------------------------

    def DigitalIn(self, name):

        return DigitalIn(
            self.manager,
            name
        )

    # ---------------------------------------------------------

    def AnalogIn(self, name):

        return AnalogIn(
            self.manager,
            name
        )

    # ---------------------------------------------------------

    def PwmOut(self, name):

        return PwmOut(
            self.manager,
            name
        )

    # ---------------------------------------------------------

    def Serial(self, name):

        return Serial(
            self.manager,
            name
        )

    # ---------------------------------------------------------

    def Timer(self,
              name="Timer"):

        timer = Timer(
            self.runtime,
            name
        )

        self.timers.append(timer)

        return timer

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"Board("
            f"{self.clock.frequency/1e6:.0f} MHz, "
            f"{self.cycles} cycles, "
            f"{self.time_us:.3f} us)"
        )

    # ---------------------------------------------------------

    def peripherals(self):

        return list(self.manager)