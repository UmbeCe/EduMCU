"""
EduMCU Core

Integration test
Board + GPIO
"""

from board import Board


print("----------------------------------------")
print("EduMCU - Board GPIO Test")
print("----------------------------------------")

board = Board()

print(board)
print()

#
# Create GPIOs
#

led = board.DigitalOut("LED1")

button = board.DigitalIn("BUTTON1")

print("Peripherals created")
print("-------------------")

print(led)
print(button)
print()

#
# Write LED
#

print("Digital Output")
print("--------------")

led.write(1)

print("LED =", led.read())

led.write(0)

print("LED =", led.read())

print()

#
# Read Button
#

print("Digital Input")
print("-------------")

print("BUTTON =", button.read())

print()

#
# Execute simulation
#

print("Simulation")
print("----------")

for i in range(10):

    board.step()

    print(
        f"Step {i+1:2d} : "
        f"cycles={board.cycles:4d} "
        f"time={board.time_us:8.3f} us"
    )

print()

#
# Reset
#

print("Reset")
print("-----")

board.reset()

print(board)

print()

print("GPIO test finished successfully.")