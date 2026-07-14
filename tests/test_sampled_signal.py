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




from sampled_signal import SampledSignal

samples = [10, 20, 30, 40, 50]

signal = SampledSignal(
    samples,
    sample_rate=1_000_000
)


print(signal)

print()

print("=== Lecture à 1 MHz ===")

for t in range(7):

    print(
        f"{t} us -> {signal.sample(t)}"
    )

print()

print("Durée :", signal.duration_us, "us")

print("Nombre d'échantillons :", len(signal))



signal2 = SampledSignal(
    [100, 200, 300],
    sample_rate=500_000
)

for t in range(8):

    print(
        t,
        signal2.sample(t)
    )

signal3 = SampledSignal(
    [1, 2, 3],
    sample_rate=1_000_000,
    loop=True
)

for t in range(8):

    print(
        signal3.sample(t),
        end=" "
    )
