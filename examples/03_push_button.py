"""
EduMCU Examples

03_button_led.py

Description
-----------
Control a virtual LED with a virtual push button.
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

led = board.DigitalOut("LED1")

simulation_time = 6.0

print("----------------------------------------")
print("EduMCU Example 03 - Button controls LED")
print("----------------------------------------")

# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

while board.time_s < simulation_time:

    #
    # Simulate a button press between
    # 2 s and 4 s.
    #
    if 2.0 <= board.time_s < 4.0:

        button.simulate(True)

    else:

        button.simulate(False)

    #
    # Mirror button state to LED.
    #
    led.write(button.read())

    print(
        f"{board.time_s:6.3f} s | "
        f"BUTTON = {'ON ' if button.read() else 'OFF'} | "
        f"LED = {'ON' if led.read() else 'OFF'}"
    )

    board.delay_ms(250)

print()

print("----------------------------------------")
print("Simulation finished")
print("----------------------------------------")

print(f"Elapsed time : {board.time_s:.3f} s")
print(f"CPU cycles   : {board.cycles}")