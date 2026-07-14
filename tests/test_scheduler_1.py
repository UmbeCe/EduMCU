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


def hello(time):

    print(time)


scheduler.every_us(
    5,
    hello
)


for i in range(20):

    scheduler.step()