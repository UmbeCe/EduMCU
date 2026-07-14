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


def task(time):

    print("tick", time)


t = scheduler.every_us(
    3,
    task
)

for i in range(20):

    if i == 10:

        scheduler.cancel(t)

    scheduler.step()