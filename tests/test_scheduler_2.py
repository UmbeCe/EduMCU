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

scheduler = Scheduler(
    time_step_us=0.5
)


def task(time):

    print(time)


scheduler.every_us(
    2,
    task
)

for i in range(20):

    scheduler.step()