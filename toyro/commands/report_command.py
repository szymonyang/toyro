from toyro.commands.base_command import BaseCommand
from toyro.robot import Robot


class ReportCommand(BaseCommand):
    def __init__(self, robot: Robot):
        super().__init__(robot)

    @BaseCommand.catch_operaltional_exception
    def execute(self):
        x, y, f = self._robot.report()
        print(f"Output: {x},{y},{f}")
