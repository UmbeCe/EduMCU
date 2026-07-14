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

clock = Clock(48_000_000)
bus = Bus()

cpu = CPU(clock, bus)

print(cpu)

cpu.start()

print(cpu.running)

cpu.step()

print(cpu.cycles)

for _ in range(10):
    cpu.step()

print(cpu.cycles)

cpu.stop()

cpu.step()

print(cpu.cycles)

cpu.reset()

print(cpu.cycles)

cpu.start()

for _ in range(48):
    cpu.step()

print(cpu.time_us)

