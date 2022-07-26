from toyro.commands import BaseCommand
from toyro.table import Table


class RobotMotor:

    def execute_command(self, command: BaseCommand, *args):
        command.execute(*args)
