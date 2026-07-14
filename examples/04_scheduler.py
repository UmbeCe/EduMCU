"""
EduMCU Examples

04_scheduler.py

Description
-----------
Blink a virtual LED using the Scheduler.
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

simulation_time = 5.0

print("----------------------------------------")
print("EduMCU Example 04 - Scheduler")
print("----------------------------------------")


# ---------------------------------------------------------
# Scheduled task
# ---------------------------------------------------------

def blink():

    led.toggle()

    print(
        f"{board.time_s:6.3f} s | "
        f"LED = {'ON' if led.read() else 'OFF'}"
    )


#
# Execute blink() every 500 ms.
#
board.every_ms(500, blink)


# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

while board.time_s < simulation_time:

    #
    # Nothing to do.
    # The Scheduler executes blink().
    #
    board.delay_ms(10)


print()

print("----------------------------------------")
print("Simulation finished")
print("----------------------------------------")

print(f"Elapsed time : {board.time_s:.3f} s")
print(f"CPU cycles   : {board.cycles}")