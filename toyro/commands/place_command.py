from toyro.commands.base_command import BaseCommand
from toyro.robot import Robot
from toyro.table import Table


class PlaceCommand(BaseCommand):
    def __init__(self, x: str, y: str, f: str, robot: Robot, table: Table):
        super().__init__(robot)
        self._x = x
        self._y = y
        self._f = f
        self._table = table

    @BaseCommand.catch_operaltional_exception
    def execute(self):
        self._robot.place(self._x, self._y, self._f, self._table)
