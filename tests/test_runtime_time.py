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

print("----------------------------------------")
print("EduMCU - Runtime Time API Test")
print("----------------------------------------")

print("Initial state")
print(f"Cycles : {board.cycles}")
print(f"Time   : {board.time_us:.3f} us")
print()

board.run_us(100)

print("After run_us(100)")
print(f"Cycles : {board.cycles}")
print(f"Time   : {board.time_us:.3f} us")
print()

board.run_ms(1)

print("After run_ms(1)")
print(f"Cycles : {board.cycles}")
print(f"Time   : {board.time_ms:.3f} ms")
print()

board.run_s(1)
# board.run_ms(100)

print("After run_s(1)")
print(f"Cycles : {board.cycles}")
print(f"Time   : {board.time_s:.3f} s")
print()

print("Runtime Time API PASSED")