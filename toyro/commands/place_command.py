from toyro.commands.base_command import BaseCommand
from toyro.robot import Robot
from toyro.table import Table


class PlaceCommand(BaseCommand):
    def __init__(self,  robot: Robot, table: Table):
        super().__init__(robot)
        self._table = table

    @BaseCommand.catch_operaltional_exception
    def execute(self, x: str, y: str, f: str,):
        super().execute()
        self._robot.place(x, y, f, self._table)
