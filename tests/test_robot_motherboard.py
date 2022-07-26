import re
import pytest
from toyro.constant import NORTH, SOUTH, WEST
from toyro.robot import Robot
from toyro.table import Table
from toyro.robot_motherboard import RobotMotherBoard
from toyro.robot_motor import RobotMotor

DIR_TEST = "tests/fixtures/"


def test_robusticity(motherboard: RobotMotherBoard):
    '''
    the app should be robust and able to handle incorrect input
    '''
    motherboard.start(["input_invalid.txt"], DIR_TEST)


@pytest.fixture()
def robot():
    return Robot()


@pytest.fixture()
def table_5x5():
    return Table(5, 5)


@pytest.fixture()
def motor():
    return RobotMotor()


@pytest.fixture(autouse=True)
def motherboard(robot, table_5x5, motor):
    return RobotMotherBoard(robot, table_5x5, motor)
