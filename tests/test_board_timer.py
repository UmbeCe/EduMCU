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
from timer import Timer

board = Board()

timer = Timer(board.runtime, "T0")

print("=== Création ===")

print(timer)

print()

print("=== Démarrage ===")

timer.start_s(100) # equivalent to timer.start() because by defalut duration_us is set to 100_000_000


for _ in range(96):

    board.step()

print("Temps écoulé (µs) :", timer.elapsed_us())

print("Temps écoulé (ms) :", timer.elapsed_ms())

print()

print("=== Restart ===")

timer.restart()

for _ in range(48):

    board.step()

print("Temps écoulé (µs) :", timer.elapsed_us())

print()

print("=== Stop ===")

timer.stop()

for _ in range(48):

    board.step()

print("Temps écoulé (µs) :", timer.elapsed_us())

print()

print("=== Reset ===")

timer.reset()

print(timer)
