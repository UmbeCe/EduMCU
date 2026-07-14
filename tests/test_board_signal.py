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




from board import Board
from sampled_signal import SampledSignal

board = Board()

adc = board.AnalogIn("A0")

signal = SampledSignal(
    [100, 200, 300, 400],
    sample_rate=1_000_000
)

adc.load_signal(signal)

print("Temps(us)   Cycles   ADC")

for _ in range(250):

    board.step()

    if board.cycles % 48 == 0:

        print(
            f"{board.time_us:8.3f}   "
            f"{board.cycles:6}   "
            f"{adc.read()}"
        )