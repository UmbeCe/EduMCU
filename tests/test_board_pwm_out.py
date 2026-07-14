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

pwm = board.PwmOut("PWM1")

pwm.enable()

pwm.frequency(1000)

pwm.write(0.25)

print(" Temps(us) | Cycles | Level ")

print("-----------------------------")

for _ in range(240):

    board.step()

    if board.cycles % 12 == 0:

        print(
            f"{board.time_us:9.3f} | "
            f"{board.cycles:6} | "
            f"{pwm.level()}"
        )