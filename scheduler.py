"""
EduMCU Core

002 - scheduler.py
"""


class Task:

    def __init__(self,
                 period_us,
                 function):

        self.period_us = period_us

        self.function = function

        self.last_run = 0.0

        self.enabled = True

        self.running = False


class Scheduler:
    """
    Cooperative scheduler.
    """

    def __init__(self):

        self.tasks = []

        self.time_us = 0.0

    # ---------------------------------------------------------

    def every_us(self,
                 period_us,
                 function):

        self.tasks.append(

            Task(
                period_us,
                function
            )

        )

    # ---------------------------------------------------------

    def every_ms(self,
                 period_ms,
                 function):

        self.every_us(
            period_ms * 1000,
            function
        )

    # ---------------------------------------------------------

    def update(self,
               current_time_us):
        """
        Called by Runtime.
        """

        self.time_us = current_time_us

        for task in self.tasks:

            if not task.enabled:
                continue

            if task.running:
                continue

            if (
                self.time_us
                - task.last_run
                >= task.period_us
            ):

                task.running = True

                task.function()

                task.running = False

                task.last_run = self.time_us

    # ---------------------------------------------------------

    def millis(self):

        return self.time_us / 1000.0

    # ---------------------------------------------------------

    def micros(self):

        return self.time_us

    # ---------------------------------------------------------

    def reset(self):

        self.time_us = 0.0

        for task in self.tasks:

            task.last_run = 0.0

            task.running = False

    # ---------------------------------------------------------

    def clear(self):

        self.tasks.clear()

    # ---------------------------------------------------------

    def __len__(self):

        return len(self.tasks)