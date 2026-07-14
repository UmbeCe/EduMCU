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

board = Board(48000000, 1000)

print(board.cpu.running)

led = board.DigitalOut("LED1")

print(board.time_s)

board.step()

print(board.time_s)

board.step()

print(board.time_s)




simulation_time = 10

while board.time_s < simulation_time:

    led.toggle()

    print(
        f"{board.time_s:6.3f} s"
    )

    board.run_ms(500)