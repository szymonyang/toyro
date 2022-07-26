
import logging
from typing import List

from pyparsing import line
from toyro.commands import LeftCommand, RightCommand, MoveCommand, ReportCommand, PlaceCommand
from toyro.constant import LEFT, MOVE, PLACE, REPORT, RIGHT
from toyro.robot import Robot
from toyro.utils.parse import parse
from toyro.table import Table
from toyro.robot_motor import RobotMotor


class RobotMotherBoard:
    def __init__(self, robot: Robot, table: Table, motor: RobotMotor):
        self. _robot = robot
        self._table = table
        self._motor = motor

    def start(self, files: List, dir: str):
        for filename in files:
            with open(dir + filename, "r") as f:
                for line in f:
                    commands = parse(line)

                    if not len(commands):
                        logging.warning(f"Invalid command '{line.strip()}'")
                        continue
                    self.run(commands)

    def run(self, commands: List):
        cmd = commands[0]
        if cmd == PLACE:
            direction = commands[1:]
            p = PlaceCommand(self._robot, self._table)
            self._motor.execute_command(p, *direction)
            return

        if cmd == MOVE:
            m = MoveCommand(self._robot, self._table)
            self._motor.execute_command(m)
            return

        if cmd == LEFT:
            l = LeftCommand(self._robot)
            self._motor.execute_command(l)
            return

        if cmd == RIGHT:
            r = RightCommand(self._robot)
            self._motor.execute_command(r)
            return

        if cmd == REPORT:
            r = ReportCommand(self._robot)
            self._motor.execute_command(r)
            return

        logging.warning(f"Invalid command '{line}'")

    @property
    def robot(self):
        return self._robot
