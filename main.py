
from toyro.robot_motherboard import RobotMotherBoard
from toyro.table import Table
from toyro.robot_motor import RobotMotor
from toyro.robot import Robot
from toyro.utils.method import get_files

TABLE_WIDTH = 5
TABLE_LENGTH = 5
DIR = "input/"

if __name__ == "__main__":
    robot = Robot()
    table = Table(TABLE_WIDTH, TABLE_LENGTH)
    motor = RobotMotor()

    motherboard = RobotMotherBoard(robot, table, motor)
    files = get_files(DIR)
    motherboard.start(files, DIR)
