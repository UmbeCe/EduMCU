"""
EduMCU Core

007 - runtime.py
"""

from scheduler import Scheduler
from simulation_config import SimulationConfig


class Runtime:
    """
    Simulation runtime.

    Responsibilities
    ----------------
    - Execute the CPU
    - Advance the simulated time
    - Execute scheduled tasks
    - Update peripherals
    """

##    def __init__(self,
##                 cpu,
##                 manager,
##                 scheduler=None,
##                 quantum_us=10):
##
##        self.cpu = cpu
##        self.manager = manager
##
##        if scheduler is None:
##            scheduler = Scheduler()
##
##        self.scheduler = scheduler
##
##        self.quantum_us = quantum_us
##
##        self.quantum = max(
##            1,
##            int(
##                quantum_us
##                * self.cpu.clock.frequency
##                / 1_000_000
##            )
##        )

    def __init__(self,
                 cpu,
                 manager,
                 scheduler=None,
                 quantum_us=None,
                 simulation_config=None):

        self.cpu = cpu
        self.manager = manager

        # self.manager.runtime = self

        if scheduler is None:
            scheduler = Scheduler()

        self.scheduler = scheduler

        if simulation_config is None:
            self.simulation_config = SimulationConfig() # IL FAUT CREER L'OBJET AVANT DE LUI AFFECTER UN ATTRIBUT

        else:
            self.simulation_config = simulation_config


        if quantum_us is None:
            quantum_us = self.simulation_config.quantum_us

        else:
            quantum_us = quantum_us



        self.quantum_us = quantum_us # interval de simulation en temps

        self.quantum_cycles = max(
            1,
            int(
                quantum_us
                * cpu.clock.frequency
                / 1_000_000
            ) # interval de simulation en cylces
        )

    # ---------------------------------------------------------

    @property
    def time_us(self):

        return (
            self.cpu.cycles
            / self.cpu.clock.frequency
            * 1_000_000
        )


    @property
    def time_ms(self):

        return self.time_us / 1000


    @property
    def time_s(self):

        return self.time_us / 1_000_000



    # ---------------------------------------------------------

##    def step(self):
##        """
##        Execute one CPU step.
##        """
##
##        self.cpu.step()
##
##        self.scheduler.update(self.time_us)
##
##        for peripheral in self.manager:
##
##            if hasattr(peripheral, "update"):
##
##                peripheral.update(self)

##    def step(self):
##        """
##        Execute one simulation step (one quantum).
##        """
##
##        self.cpu.advance(self.quantum_cycles)
##
##        self.scheduler.update(self.time_us)
##
##        for peripheral in self.manager:
##
##            if hasattr(peripheral, "update"):
##
##                peripheral.update(self)

    def step(self):

        self.cpu.advance(self.quantum_cycles)

        self.scheduler.update(self.time_us)

        for peripheral in self.manager:

            if hasattr(peripheral, "update"):

                peripheral.update(self)

    # ---------------------------------------------------------

##    def run(self, cycles):
##        """
##        Execute several CPU cycles.
##        """
##
##        remaining = cycles
##
##        while remaining > 0:
##
##            block = min(
##                remaining,
##                self.quantum_cycles
##            )
##
##            #
##            # Advance CPU
##            #
##
##            self.cpu.advance(block)
##
##            #
##            # Update scheduler
##            #
##
##            self.scheduler.update(
##                self.time_us
##            )
##
##            #
##            # Update peripherals
##            #
##
##            for peripheral in self.manager:
##
##                if hasattr(peripheral, "update"):
##
##                    peripheral.update(self)
##
##            remaining -= block

    def run(self, steps):

        for _ in range(steps):

            self.step()

    # ---------------------------------------------------------

##    def run_us(self, us):
##
##        cycles = int(
##            us
##            * self.cpu.clock.frequency
##            / 1_000_000
##        )
##
##        self.run(cycles)

    def run_us(self, us):

        steps = max(
            1,
            int(us / self.quantum_us)
        )

        self.run(steps)

    # ---------------------------------------------------------

    def run_ms(self, ms):

        self.run_us(ms * 1000)


    # ---------------------------------------------------------

    def run_s(self, seconds):

        self.run_us(seconds * 1_000_000)


##    # ---------------------------------------------------------
##
##    def stop(self):
##
##        self.running = False

    # ---------------------------------------------------------

    def reset(self):

        self.cpu.reset()

        self.scheduler.reset()

        self.manager.reset()

    # ---------------------------------------------------------

    def advance_us(self, us):
        """
        Consume simulated execution time.
        """

        self.run_us(us)

    # ---------------------------------------------------------

##    def __repr__(self):
##
##        return (
##            f"Runtime("
##            f"time={self.time_us:.3f} us)"
##        )

    def __repr__(self):

        return (
            f"Runtime("
            f"time={self.time_us:.3f} us, "
            f"quantum={self.quantum_cycles} cycles "
            f"({self.quantum_us} us)"
            f")"
        )