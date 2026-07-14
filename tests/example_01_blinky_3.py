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

board = Board()

led = board.DigitalOut("LED1")

def forever(self, callback):
    """
    Execute a callback forever.
    Stop cleanly with Ctrl+C.
    """
    try:
        while True:
            callback()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

def loop():

    led.toggle()

    board.run(480000) # Simulaire à un wait

board.forever(loop)