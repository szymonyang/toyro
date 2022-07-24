from toyro.commands.base_command import BaseCommand
from toyro.robot import Robot
from toyro.constant import LEFT


class LeftCommand(BaseCommand):
    def __init__(self, robot: Robot):
        super().__init__(robot)

    @BaseCommand.catch_operaltional_exception
    def execute(self):
        self._robot.rotate(LEFT)
