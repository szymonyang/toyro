import pytest
from toyro.constant import EAST, NORTH, LEFT, SOUTH, WEST
from toyro.exceptions import InvalidCoordException, NotPlacedException
from toyro.robot import Robot
from toyro.table import Table


class TestTable:

    def test_place(self, robot: Robot, table: Table):
        robot.place(0, 0, NORTH, table)
        assert robot.is_placed() == True

    def test_place_twice(self, robot: Robot, table: Table):
        robot.place(1, 1, NORTH, table)
        assert robot.is_placed() == True

        robot.place(2, 2, WEST, table)
        assert robot.is_placed() == True
        assert robot.report() == (2, 2, WEST)

    def test_move(self, robot: Robot, table: Table):
        robot.place(0, 0, NORTH, table)
        robot.move(table)
        assert robot.report() == (0, 1, NORTH)

    def test_left(self, robot: Robot, table: Table):
        robot.place(0, 0, NORTH, table)
        robot.rotate(LEFT)
        assert robot.report() == (0, 0, WEST)

    def test_move_right(self, robot: Robot, table: Table):
        robot.place(1, 2, EAST, table)
        robot.move(table)
        robot.move(table)
        robot.rotate(LEFT)
        robot.move(table)
        assert robot.report() == (3, 3, NORTH)

    def test_robot_fall(self, robot: Robot, table: Table):
        robot.place(0, 0, WEST, table)
        with pytest.raises(InvalidCoordException):
            robot.move(table)

    def test_place_fail(self, robot: Robot, table: Table):
        with pytest.raises(InvalidCoordException):
            robot.place(10, 10, SOUTH, table)

    def test_move_not_place(self, robot: Robot):
        with pytest.raises(NotPlacedException):
            robot.move()

    def test_report_not_place(self, robot: Robot):
        with pytest.raises(NotPlacedException):
            robot.report()

    def test_rotate_not_place(self, robot: Robot):
        with pytest.raises(NotPlacedException):
            robot.rotate()


@pytest.fixture(autouse=True)
def robot():
    return Robot()


@pytest.fixture(autouse=True)
def table():
    return Table(5, 5)
