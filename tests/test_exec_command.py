import pytest
from toyro.constant import EAST, NORTH, SOUTH
from toyro.robot import Robot
from toyro.table import Table
from toyro.commands import PlaceCommand, LeftCommand, RightCommand, MoveCommand, ReportCommand


class TestExecCommand:

    def test_exec_command(self, robot: Robot, table_4x4: Table):
        p = PlaceCommand(robot, table_4x4)
        p.execute(0, 0, EAST)

        l = LeftCommand(robot)
        l.execute()

        m = MoveCommand(robot, table_4x4)
        m.execute()

        assert robot.report() == (0, 1, NORTH)

    def test_catch_invalid_coord_exception(self, robot: Robot, table_4x4: Table):
        """
        should not throw any exception
        """
        p = PlaceCommand(robot, table_4x4)
        p.execute(10, 0, EAST)

    def test_catch_not_placed_exception(self, robot: Robot, table_4x4: Table):
        l = LeftCommand(robot)
        l.execute()

        r = RightCommand(robot)
        r.execute()

        m = MoveCommand(robot, table_4x4)
        m.execute()

        r = ReportCommand(robot)
        r.execute()

    def test_catch_robot_falling(self, robot: Robot, table_4x4: Table):
        p = PlaceCommand(robot, table_4x4)
        p.execute(1, 0, SOUTH)

        m = MoveCommand(robot, table_4x4)
        m.execute()

    def test_should_throw_other_exception(self, robot: Robot,  table_4x4: Table):
        with pytest.raises(Exception):
            robot.place(0, 0, "INVALID DIRECTION", table_4x4)


@pytest.fixture(autouse=True)
def robot():
    return Robot()


@pytest.fixture(autouse=True)
def table_4x4():
    return Table(4, 4)
