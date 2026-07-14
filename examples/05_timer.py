"""
EduMCU Examples

05_timer.py

Description
-----------
Use a Timer to blink a virtual LED.
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

timer = board.Timer("TIMER1")

simulation_time = 5.0

print("----------------------------------------")
print("EduMCU Example 05 - Timer")
print("----------------------------------------")


#
# Start a periodic timer.
#
timer.start_ms(500)


# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

while board.time_s < simulation_time:

    #
    # Has the timer expired?
    #
    if timer.expired():

        led.toggle()

        print(
            f"{board.time_s:6.3f} s | "
            f"LED = {'ON' if led.read() else 'OFF'}"
        )

        #
        # Restart the timer.
        #
        timer.start_ms(500)

    board.delay_ms(10)


print()

print("----------------------------------------")
print("Simulation finished")
print("----------------------------------------")

print(f"Elapsed time : {board.time_s:.3f} s")
print(f"CPU cycles   : {board.cycles}")