# cardinal direction
NORTH = "NORTH"
SOUTH = "SOUTH"
WEST = "WEST"
EAST = "EAST"

LEFT = "LEFT"
RIGHT = "RIGHT"


DIRECTION_TO_UNIT_VECTOR = {
    NORTH: (0, 1),
    SOUTH: (0, -1),
    EAST: (1, 0),
    WEST: (-1, 0)
}

UNIT_VECTOR_TO_DIRECTION = dict(
    zip(DIRECTION_TO_UNIT_VECTOR.values(), DIRECTION_TO_UNIT_VECTOR.keys()))

ROTATION_TO_DEGREE = {
    LEFT: 90,
    RIGHT: -90
}
