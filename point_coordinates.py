from typing import NamedTuple

from program_exceptions import IntArgumentError


class Point:
    def __init__ (self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def add_x_dispersion (self, x_dispersion: int) -> None:
        self._check_x_dispersion (x_dispersion)
        self.x_coordinate += x_dispersion

    def add_y_dispersion (self, y_dispersion: int) -> None:
        self._check_y_dispersion (y_dispersion)
        self.y_coordinate += y_dispersion

    def _check_x_dispersion (self, number: int) -> None:
        if not isinstance (number, int):
            raise IntArgumentError (number, "x_dispersion",
                                    self.add_x_dispersion.__name__,
                                    __class__.__name__)

    def _check_y_dispersion (self, number: int) -> None:
        if not isinstance (number, int):
            raise IntArgumentError (number, "y_dispersion",
                                    self.add_y_dispersion.__name__,
                                    __class__.__name__)

    def add_dispersion (self, x_dispersion: int, y_dispersion: int) -> None:
        self.add_x_dispersion (x_dispersion)
        self.add_y_dispersion (y_dispersion)

    def __add__ (self, other_point):
        return Point (self.x_coordinate + other_point.x_coordinate,
                      self.y_coordinate + other_point.y_coordinate)

    def __iadd__ (self, other_point):
        return Point (self.x_coordinate + other_point.x_coordinate,
                      self.y_coordinate + other_point.y_coordinate)

    def __sub__ (self, other_point):
        return Point (self.x_coordinate - other_point.x_coordinate,
                      self.y_coordinate - other_point.y_coordinate)

    def __isub__ (self, other_point):
        return Point (self.x_coordinate - other_point.x_coordinate,
                      self.y_coordinate - other_point.y_coordinate)

    def __str__ (self):
        return f"{__class__.__name__}{self.x_coordinate, self.y_coordinate}"

    def __len__ (self):
        return 2

    def __iter__ (self):
        self._iter_state = "x"
        return self

    def __next__ (self):
        if self._iter_state == "x":
            self._iter_state = "y"
            return self.x_coordinate
        elif self._iter_state == "y":
            self._iter_state = ''
            return self.y_coordinate
        else:
            raise StopIteration

    def __reversed__ (self):
        return self.y_coordinate, self.x_coordinate


class Region (NamedTuple):
    x_coordinate_of_upper_left_corner : int
    y_coordinate_of_upper_left_corner : int
    width : int
    height : int

class Box (NamedTuple):
    left : int
    top : int
    width : int
    height : int



if __name__ == "__main__":
    testPoint = Point (10, 70)
    print (*testPoint)
    testPoint += Point (10, 30)
    print (testPoint)
