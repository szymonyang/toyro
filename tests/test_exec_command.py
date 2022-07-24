import pytest
from toyro.constant import EAST, SOUTH
from toyro.robot import Robot
from toyro.table import Table
from toyro.commands import PlaceCommand, LeftCommand, RightCommand, MoveCommand


class TestExecCommand:

    def test_exec_command(self, robot: Robot, table_4x4: Table):
        pass

    def test_catch_invalid_coord_exception(self, robot: Robot, table_4x4: Table):
        """
        should not throw any exception
        """
        p = PlaceCommand(robot)
        p.execute(0, 0, EAST, table_4x4)
        p.execute(10, 0, EAST, table_4x4)

    def test_catch_not_placed_exception(self, robot: Robot, table_4x4: Table):
        l = LeftCommand(robot)
        l.execute()

        r = RightCommand(robot)
        r.execute()

        m = MoveCommand(robot)
        m.execute(table_4x4)

    def test_catch_robot_falling(self, robot: Robot, table_4x4: Table):
        p = PlaceCommand(robot)
        p.execute(1, 0, SOUTH, table_4x4)

        m = MoveCommand(robot)
        m.execute(table_4x4)

    def test_should_throw_other_exception(self, robot: Robot,  table_4x4: Table):
        with pytest.raises(Exception):
            robot.place(0, 0, "INVALID DIRECTION", table_4x4)


@pytest.fixture(autouse=True)
def robot():
    return Robot()


@pytest.fixture(autouse=True)
def table_4x4():
    return Table(5, 5)
