"""
EduMCU Examples

01_blinky.py

Description
-----------
Blink a virtual LED every 500 ms.
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

led = board.DigitalOut("LED1")

simulation_time = 10.0

print("----------------------------------------")
print("EduMCU Example 01 - Blinky")
print("----------------------------------------")

# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

while board.time_s < simulation_time:

    led.toggle()

    print(
        f"{board.time_s:6.3f} s | "
        f"LED = {'ON' if led.read() else 'OFF'}"
    )

    board.delay_ms(500)

print()

print("Simulation finished.")
print(
    f"Elapsed time : {board.time_s:.3f} s"
)
print(
    f"CPU cycles   : {board.cycles}"
)