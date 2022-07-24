import math
from typing import Tuple

DIRECTION_TO_UNIT_VECTOR = {
    "NORTH": (0, 1),
    "SOUTH": (0, -1),
    "EAST": (1, 0),
    "WEST": (-1, 0)
}

UNIT_VECTOR_TO_DIRECTION = dict(
    zip(DIRECTION_TO_UNIT_VECTOR.values(), DIRECTION_TO_UNIT_VECTOR.keys()))

ROTATION_TO_DEGREE = {
    "LEFT": 90,
    "RIGHT": -90
}


def to_unit_vector(direction: str) -> Tuple[int, int]:
    return DIRECTION_TO_UNIT_VECTOR[direction]


def to_direction(unit_vector: Tuple[int, int]) -> str:
    return UNIT_VECTOR_TO_DIRECTION[unit_vector]


def sind(deg: int) -> float:
    return math.sin(math.radians(deg))


def cosd(deg: int) -> float:
    return math.cos(math.radians(deg))


def rotate_unit_vector(unit_vector: Tuple[int, int], rotation: str) -> Tuple[int, int]:
    deg = ROTATION_TO_DEGREE[rotation]
    unit_i = round(cosd(deg)*unit_vector[0] - sind(deg)*unit_vector[1])
    unit_j = round(sind(deg)*unit_vector[0] + cosd(deg)*unit_vector[1])
    return (unit_i, unit_j)
