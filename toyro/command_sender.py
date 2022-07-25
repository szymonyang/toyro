from toyro.table import Table
from toyro.robot import Robot
from toyro.constant import NORTH, SOUTH, WEST, EAST, MOVE, LEFT, RIGHT
from toyro.commands import BaseCommand, LeftCommand, RightCommand, MoveCommand, ReportCommand, PlaceCommand
from toyro.table import Table


class CommandSender:

    def send(self, command: BaseCommand):
        command.execute()
