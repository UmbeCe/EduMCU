"""
EduMCU Examples

09_serial.py

UART demonstration.
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

board = Board()

uart = board.Serial("USART1")

simulation_time = 3.0

counter = 0

print("----------------------------------------")
print("EduMCU Example 09 - Serial")
print("----------------------------------------")

while board.time_s < simulation_time:

    message = f"Message {counter}"

    uart.write(message)

    print(
        f"{board.time_s:5.2f} s | "
        f"TX : {message}"
    )

    counter += 1

    board.delay_ms(500) # necessay to increase the board.time_s !!! (or use board.step() is the board_time has to increase of a quantam_time = simulation_time)

print()

print("Simulation finished")