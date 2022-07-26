from typing import Tuple, Optional
from toyro.exceptions import NotPlacedException, InvalidCoordException
from toyro.table import Table
from toyro.utils.method import rotate_unit_vector, to_direction, to_unit_vector


class Robot:

    def __init__(self):
        self._x = None
        self._y = None
        self._unit_vector = None

    def place(self, x: int, y: int, f: str, table: Table):
        if not table.is_coord_valid(x, y):
            raise InvalidCoordException(f"Invalid coords ({x}, {y}) given")

        self._x = x
        self._y = y
        self._unit_vector = to_unit_vector(f)

    def throw_exception_if_not_placed(func):
        def wrapper(self,  *args,  **kwargs):
            if not self.is_placed():
                raise NotPlacedException(
                    f"The robot is not placed on the table")
            return func(self, *args,  **kwargs)
        return wrapper

    @throw_exception_if_not_placed
    def move(self, table: Table):
        x, y = self._x + self._unit_vector[0], self._y + self._unit_vector[1]
        if not table.is_coord_valid(x, y):
            raise InvalidCoordException(
                f"The robot cannot move to the position ({x}, {y})")

        self._x = x
        self._y = y

    @throw_exception_if_not_placed
    def rotate(self, rotation: str):
        self._unit_vector = rotate_unit_vector(self._unit_vector, rotation)

    @throw_exception_if_not_placed
    def report(self) -> Tuple[int, int, str]:
        direction = to_direction(self._unit_vector)
        return (self._x, self._y, direction)

    def is_placed(self) -> bool:
        return self._x is not None and self._y is not None and self._unit_vector is not None
