from toyro.util import rotate_unit_vector


def test_rotate_unit_vector():
    assert rotate_unit_vector((0, 1), "RIGHT") == (1, 0)
    assert rotate_unit_vector((-1, 0), "LEFT") == (0, -1)
