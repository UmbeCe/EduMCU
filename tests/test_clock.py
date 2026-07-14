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

clock = Clock(48_000_000)

print(clock)

print(clock.frequency)

print(clock.period)

print(clock.microseconds_to_cycles(1))

print(clock.cycles_to_microseconds(48))

print(clock.seconds_to_cycles(1))

print(clock.cycles_to_seconds(96))