"""
EduMCU

Integration test

Runtime + SampledSignal
"""

from clock import Clock
from bus import Bus
from cpu import CPU
from scheduler import Scheduler
from runtime import Runtime
from device_manager import DeviceManager

from sampled_signal import SampledSignal


# ---------------------------------------------------------
# Hardware
# ---------------------------------------------------------

clock = Clock()

bus = Bus()

manager = DeviceManager(bus)

cpu = CPU(clock, bus)

scheduler = Scheduler()

runtime = Runtime(
    cpu,
    manager,
    scheduler
)

# ---------------------------------------------------------
# Signal
# ---------------------------------------------------------

signal = SampledSignal(
    # samples=[100, 200, 300, 400, 500],
    # sample_rate=1_000_000
    # sample_rate=500000
    samples=[0, 1000, 2000, 3000],
    sample_rate=250000
)

print(signal)

print()

print("Temps(us)   Valeur")

print("------------------")

# ---------------------------------------------------------
# Simulation
# ---------------------------------------------------------

cpu.start()

for i in range(8):

    print(
        f"{runtime.time_us:8}   {signal.sample(runtime.time_us)}"
    )

    runtime.step()