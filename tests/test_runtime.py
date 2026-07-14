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
from runtime import Runtime
from device_manager import DeviceManager



clock = Clock()

bus = Bus()

manager = DeviceManager(bus)

cpu = CPU(clock, bus)

runtime = Runtime(
    cpu,
    manager
)

print(runtime)

cpu.start()

runtime.step()

print(cpu.cycles)

print(runtime.time_us)

runtime.run(100)

print(cpu.cycles)

runtime.reset()

print(cpu.cycles)

print(runtime.time_us)

runtime.step()