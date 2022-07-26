from toyro.exceptions.invalid_coord_exception import InvalidCoordException


class Table:
    def __init__(self, length: int, width: int) -> None:
        self._length = length
        self._width = width

    def is_coord_valid(self, x: int, y: int):
        if x >= self._length or x < 0:
            return False
        if y >= self._width or y < 0:
            return False
        return True
