"""
Test EduMCU Core function

"""

# To import the EduMCU Core from root file
import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


from clock import Clock
from bus import Bus
from cpu import CPU
from scheduler import Scheduler
from runtime import Runtime
from device_manager import DeviceManager

from analog_in import AnalogIn
from sampled_signal import SampledSignal
# from simulation_config import SimulationConfig


clock = Clock()

bus = Bus()

manager = DeviceManager(bus)

cpu = CPU(clock, bus)

scheduler = Scheduler()

# simulation_config = SimulationConfig()

runtime = Runtime(
    cpu,
    manager,
    scheduler
)

adc = AnalogIn(
    manager,
    "A0"
)

signal = SampledSignal(
    [100, 200, 300, 400],
    sample_rate=1_000_000
)



adc.load_signal(signal)

cpu.start()

for i in range(6):

    runtime.step()

    print(
        runtime.time_us,
        adc.read()
    )


adc.simulate(1234)

print(adc.read())

adc.unload_signal()

runtime.step()

print(adc.read())