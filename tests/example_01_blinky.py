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

# ---------------------------------------------------------

board = Board()

led = board.DigitalOut("LED1")

print("----------------------------------------")
print("EduMCU Example 01 - Blinky")
print("----------------------------------------")
print()

print("Starting simulation...\n")

# ---------------------------------------------------------


def toggle(self):
    """
    Toggle the output state.
    """

    self.write(not self.read())


for i in range(10):

    led.toggle()

    state = "ON " if led.read() else "OFF"

    print(
        f"Blink {i+1:2d} | "
        f"LED = {state} | "
        f"Cycles = {board.cycles:8d} | "
        f"Time = {board.time_us:10.3f} us"
    )

    #
    # Advance the simulation by 10 ms
    #
    board.run(480000)

print()
print("Simulation finished.")