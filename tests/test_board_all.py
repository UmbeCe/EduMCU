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



"""
EduMCU Core

Integration Test
Board + All peripherals
"""

from board import Board
from sampled_signal import SampledSignal


print("=" * 50)
print("EduMCU - Full Integration Test")
print("=" * 50)

board = Board()

#
# Peripherals
#

led = board.DigitalOut("LED1")
button = board.DigitalIn("BUTTON1")
adc = board.AnalogIn("A0")
pwm = board.PwmOut("PWM1")
uart = board.Serial("UART0")
timer = board.Timer("Main")

#
# ADC signal
#

signal = SampledSignal(
    samples=[100, 250, 500, 750, 1000, 750, 500, 250],
    sample_rate=1000
)

adc.load_signal(signal)

#
# UART
#

uart.enable()
uart.baudrate(115200)

#
# PWM
#

pwm.enable()
pwm.period_ms(20)
pwm.write(0.50)

#
# Timer
#

# timer.start()
timer.start_s(100)

print("\nSimulation\n")

print(f"{'Step':>4} {'Time(us)':>10} {'ADC':>6} {'LED':>4}")

for step in range(20):

    #
    # Blink LED
    #

    led.write(step % 2)

    #
    # Read ADC
    #

    value = adc.read()

    #
    # Send to UART
    #

    uart.println(f"ADC={value}")

    #
    # Display state
    #

    print(
        f"{step:4d} "
        f"{board.time_us:10.3f} "
        f"{value:6d} "
        f"{led.read():4d}"
    )

    #
    # Advance simulation by 1 ms
    #

    board.run(48000)

print()

print("Timer elapsed : %.3f ms" % timer.elapsed_ms())

print("CPU cycles    :", board.cycles)

print("Simulation    : %.3f us" % board.time_us)

print()

print("UART transmitted bytes :", len(uart.hardware.tx_buffer))

print()

print("Resetting board...")

board.reset()

print(board)

print()

print("FULL INTEGRATION TEST PASSED")