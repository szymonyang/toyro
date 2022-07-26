from toyro.utils.parse import parse
from toyro.constant import EAST


def test_place():
    line = "PLACE 1,2,EAST\n"
    assert parse(line) == ["PLACE", 1, 2, EAST]


def test_left():
    line = "LEFT\n"
    assert parse(line) == ["LEFT"]


def test_move():
    line = "MOVE\n"
    assert parse(line) == ["MOVE"]


def test_right():
    line = "RIGHT\n"
    assert parse(line) == ["RIGHT"]


def test_invalid_line():
    line = "PLACE 1,2,EASTx\n"
    cmd = parse(line)
    assert isinstance(cmd, list) and not len(cmd)

    line = "PLACE 1,x2,EASTx\n"
    cmd = parse(line)
    assert isinstance(cmd, list) and not len(cmd)

    line = "1,2,EAST\n"
    cmd = parse(line)
    assert isinstance(cmd, list) and not len(cmd)
