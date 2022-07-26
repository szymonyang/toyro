import math
from typing import Tuple
import os
from toyro.constant import DIRECTION_TO_UNIT_VECTOR, UNIT_VECTOR_TO_DIRECTION, ROTATION_TO_DEGREE


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


def get_files(dir):
    return os.listdir(dir)
