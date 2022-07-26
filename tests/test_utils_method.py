from toyro.utils.method import rotate_unit_vector, to_direction


def test_rotate_unit_vector():
    assert rotate_unit_vector((0, 1), "RIGHT") == (1, 0)
    assert rotate_unit_vector((-1, 0), "LEFT") == (0, -1)


def test_to_direction():
    assert to_direction(((0, 1))) == "NORTH"
    assert to_direction(((1, 0))) == "EAST"
    assert to_direction(((0, -1))) == "SOUTH"
    assert to_direction(((-1, 0))) == "WEST"
