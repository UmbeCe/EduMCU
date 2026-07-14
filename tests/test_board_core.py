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

print(board)

board.step()

print(board)

board.run(100)

print(board)

print("Cycles :", board.cycles)

print("Temps :", board.time_us)
