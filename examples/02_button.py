"""
EduMCU Examples

02_button.py

Description
-----------
Read a virtual push button.
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


# ---------------------------------------------------------
# Create the virtual board
# ---------------------------------------------------------

board = Board()

button = board.DigitalIn("BUTTON1")

simulation_time = 5.0

print("----------------------------------------")
print("EduMCU Example 02 - Button")
print("----------------------------------------")

#
# For this example, simulate a button press.
#
button.simulate(False)

# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

while board.time_s < simulation_time:

    #
    # Simulate the user pressing the button
    #
    if board.time_s >= 2.0:
        button.simulate(True)

    print(
        f"{board.time_s:6.3f} s | "
        f"BUTTON = {'PRESSED' if button.read() else 'RELEASED'}"
    )

    board.delay_ms(500)

print()

print("----------------------------------------")
print("Simulation finished")
print("----------------------------------------")

print(f"Elapsed time : {board.time_s:.3f} s")
print(f"CPU cycles   : {board.cycles}")
