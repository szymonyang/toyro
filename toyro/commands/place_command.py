from toyro.commands.base_command import BaseCommand
from toyro.robot import Robot
from toyro.table import Table


class PlaceCommand(BaseCommand):
    def __init__(self, robot: Robot):
        super().__init__(robot)

    @BaseCommand.catch_operaltional_exception
    def execute(self, x, y, f, table: Table):
        self._robot.place(x, y, f, table)
