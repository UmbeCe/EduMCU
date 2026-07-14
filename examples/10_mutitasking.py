"""
EduMCU Examples

10_multitasking.py

Multiple peripherals running simultaneously.
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

led = board.DigitalOut("LED1")
adc = board.AnalogIn("ADC1")
uart = board.Serial("USART1")

timer = board.Timer("Blink")

timer.start_ms(500)

simulation_time = 5.0

print("----------------------------------------")
print("EduMCU Example 10 - Multitasking")
print("----------------------------------------")

while board.time_s < simulation_time:

    #
    # Virtual analog input
    #
    adc.simulate_voltage(board.time_s / simulation_time)

    #
    # Blink every 500 ms
    #
    if timer.expired():

        led.toggle()

        uart.write(
            f"ADC = {adc.read_voltage()}"
        )

        print(
            f"{board.time_s:5.2f} s | "
            f"LED={led.read()} | "
            f"ADC={adc.read_voltage():4f}"
        )

        timer.start_ms(500)

    board.step()

print()

print("----------------------------------------")
print("Simulation finished")
print("----------------------------------------")

print(f"Simulation time : {board.time_s:.2f} s")
print(f"CPU cycles      : {board.cycles}")