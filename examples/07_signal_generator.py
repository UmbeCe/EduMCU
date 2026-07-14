"""
EduMCU Examples

07_signal_generator.py

Description
-----------
Sample a virtual sine wave.
"""

import os
import sys

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from board import Board
from sampled_signal import SampledSignal
import numpy as np

# ---------------------------------------------------------
# Create the virtual board
# ---------------------------------------------------------

# board = Board(48000000, 480000)
board = Board()
board.quantum_us = 1000 # pas de simulation

adc = board.AnalogIn("ADC1")


samples = [
    0,
    1024,
    2048,
    3072,
    4095,
    3072,
    2048,
    1024
]

signal = SampledSignal(
    samples=samples,
    sample_rate=800,
    loop=True
)


##signal = SampledSignal(
##    name="Sine",
##    amplitude=1.65,
##    offset=1.65,
##    frequency=1.0
##)

adc.load_signal(signal)

simulation_time = 0.5

print("----------------------------------------")
print("EduMCU Example 07 - Signal Generator")
print("----------------------------------------")

# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

while board.time_s < simulation_time:

    print(
        f"{board.time_s:6.3f} s | "
        f"{adc.read_voltage():5.2f} V | "
        f"ADC = {adc.read():4d}"
    )


    # board.delay_us(np.floor(10000000/signal.sample_rate))
    board.step() # avance en fonction du pas de simulation appellé quantum_us


print()

print("----------------------------------------")
print("Simulation finished")
print("----------------------------------------")

print(f"Elapsed time : {board.time_s:.3f} s")
print(f"CPU cycles   : {board.cycles}")