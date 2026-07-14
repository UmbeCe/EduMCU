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




from pwm_device import PwmDevice

print("=== Création ===")

pwm = PwmDevice("PWM1")

print(pwm)

print()

print("=== Activation ===")

pwm.enable()

print(pwm)

print()

print("=== Duty Cycle ===")

pwm.write(0, 0.25)

print("Duty =", pwm.read(0))

print(pwm)

print()

print("=== Changement de fréquence ===")

pwm.set_frequency(500)

print("Frequency =", pwm.get_frequency())

print(pwm)

print()

print("=== Saturation ===")

pwm.write(0, 2.0)

print("Duty =", pwm.read(0))

pwm.write(0, -1.0)

print("Duty =", pwm.read(0))

print()

print("=== Désactivation ===")

pwm.disable()

print(pwm)

print()

print("=== Reset ===")

pwm.reset()

print(pwm)