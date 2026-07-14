"""
EduMCU Examples

06_analog_input.py

Description
-----------
Read a virtual analog input.
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


# ---------------------------------------------------------
# Create the virtual board
# ---------------------------------------------------------

board = Board()

adc = board.AnalogIn("ADC1")

simulation_time = 5.0

print("----------------------------------------")
print("EduMCU Example 06 - Analog Input")
print("----------------------------------------")


# ---------------------------------------------------------
# Main loop
# ---------------------------------------------------------

while board.time_s < simulation_time:

    #
    # Simulate an analog voltage.
    #
    voltage = board.time_s / simulation_time

    # NUMERICAL VALUE FOR THE ADC BETWEEN 0 and 2^120 - 1 = 4095
    # adc.simulate(4095)
    # value = adc.read()

    adc.simulate_voltage(voltage)
    value = adc.read_voltage()

    print(
        f"{board.time_s:6.3f} s | "
        f"Voltage = {voltage:4.2f} V | "
        f"ADC = {value:4f} | "
        f"{board.time_s:6.3f} s | "
        f"Analog = {adc.read():.3f}"

    )


    board.delay_ms(250)


print()

print("----------------------------------------")
print("Simulation finished")
print("----------------------------------------")

print(f"Elapsed time : {board.time_s:.3f} s")
print(f"CPU cycles   : {board.cycles}")