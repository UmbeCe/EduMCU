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


print("----------------------------------------")
print("EduMCU - Board ADC Test")
print("----------------------------------------")

board = Board()

adc = board.AnalogIn("A0")

#
# Signal de test
#

signal = SampledSignal(
    samples=[
        100,
        300,
        500,
        700,
        900,
        700,
        500,
        300
    ],
    sample_rate=1000
)

adc.load_signal(signal)

print(board)
print()

print("Reading ADC")
print("-----------")

print(f"{'Step':>4} {'Cycles':>8} {'Time(us)':>10} {'ADC':>6}")

for step in range(20):

    value = adc.read()

    print(
        f"{step:4d} "
        f"{board.cycles:8d} "
        f"{board.time_us:10.3f} "
        f"{value:6}"
    )

    #
    # 100 µs simulées
    #
    board.run(4800)

print()

print("Reset")

board.reset()

print(board)

print()

print("ADC integration test PASSED")