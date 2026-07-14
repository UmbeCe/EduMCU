"""
EduMCU Examples

08_pwm.py

PWM output demonstration.
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

led = board.PwmOut("LED_PWM")

simulation_time = 5.0

print("----------------------------------------")
print("EduMCU Example 08 - PWM")
print("----------------------------------------")

duty = 0.0
step = 0.05

while board.time_s < simulation_time:

    led.write(duty)

    print(
        f"{board.time_s:5.2f} s | "
        f"Duty = {100*duty:5.1f} %"
    )

    duty += step

    if duty >= 1.0:
        duty = 0.0

    board.delay_ms(100) # necessay to increase the board.time_s !!! (or use board.step() is the board_time has to increase of a quantam_time = simulation_time)

print()

print("Simulation finished")