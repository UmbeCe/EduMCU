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



from signal_analog import Signal


print("=== Test 1 ===")

sig = Signal("Test")

print(sig)

print()

print("=== Test 2 ===")

sig.reset()

print("Reset OK")

print()

print("=== Test 3 ===")

try:

    sig.sample(1000)

except NotImplementedError as e:

    print("Exception capturée :")

    print(e)