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

uart = board.Serial("UART0")

print("=== Création ===")

print(uart)

print()

print("=== Activation ===")

uart.enable()

uart.baudrate(9600)

print(uart)

print()

print("=== Émission ===")

uart.write("Hello")

print("TX Buffer :", uart.hardware.tx_buffer)

print()

print("=== Réception simulée ===")

uart.receive("World")

print("Disponible :", uart.available())

print("Lecture :", uart.read())

print("Disponible :", uart.available())

print()

print("=== println ===")

uart.println("EduMCU")

print("TX Buffer :", uart.hardware.tx_buffer)

print()

print("=== Reset ===")

uart.reset()

print(uart)