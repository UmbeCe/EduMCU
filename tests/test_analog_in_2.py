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


clock = Clock(48_000_000)

bus = Bus()

manager = DeviceManager(bus)

cpu = CPU(clock, bus)

scheduler = Scheduler()

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
    [100, 200, 300, 400, 500],
    sample_rate=1_000_000
)

adc.load_signal(signal)

cpu.start()

cpu_period_ns = 1e9 / clock.frequency

print()

print(" Temps(us) | Cycles CPU | ADC ")

print("-------------------------------")

previous_cycles = cpu.cycles

for i in range(8):

    runtime.step()

    delta_cycles = cpu.cycles - previous_cycles

    previous_cycles = cpu.cycles

    print(
        f"{runtime.time_us:9} | "
        f"{cpu.cycles:10} | "
        f"{adc.read():4} "
        f"(+{delta_cycles} cycles)"
    )

    print(f"Période CPU : {cpu_period_ns:.2f} ns")