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



from scheduler import Scheduler

scheduler = Scheduler()


def once(time):

    print("Une seule fois :", time)


scheduler.after_us(
    12,
    once
)

for i in range(30):

    scheduler.step()