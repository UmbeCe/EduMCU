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

print("Press Ctrl+C to stop.")

try:

    while True:

        led.toggle()

        print(
            f"LED={'ON' if led.read() else 'OFF'} "
            f"Time={board.time_us:.3f} us"
        )

        board.run(480000)

except KeyboardInterrupt:

    print("\nSimulation stopped by user.")