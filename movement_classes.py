from point_coordinates import Point
from program_exceptions import IntArgumentError, MovementPatternRedefinitionError


class MovementPattern:
    """
      # Для определения новой move-функции нужно создать новый класс,
        наследованный от MoveFunc, и ОБЯЗАТЕЛЬНО переопределить
        метод "_initializing_initial_values(self)" под
        собственные нужды.
    """

    def moveTo (self):
        pass

    def get_coordinates (self, cell_number : int,
                                dispersion : int = 0) -> Point:
        """Функция для получения координат указанной ячейки."""

        self._cell_number = cell_number
        self._dispersion = dispersion

        self._initializing_start_values ( )

        self._check_cell_number ( )
        self._check_dispersion ( )

        self._calc_coordinates ( )
        self._add_dispersion ( )

        return Point (x_coordinate = self._X,
                      y_coordinate = self._Y)

    def _initializing_start_values (self) -> None:
        self._START_X, self._START_Y = 0, 0
        self._set_initial_values_for_X_and_Y ( )

        self._MIN_CELL_NUMBER = 1
        self._MAX_CELL_NUMBER = 1

        self._GAP = 0
        self._ROW = 1
        self._LAST_ROW = 1

        self._CLASS_NAME = __class__.__name__

        raise MovementPatternRedefinitionError ( )

    def _check_cell_number (self) -> None:
        self._check_int_cell_number ( )
        self._check_whether_cell_number_is_in_specified_range ( )

    def _check_int_cell_number (self) -> None:
        if not isinstance (self._cell_number, int):
            raise IntArgumentError (self._cell_number, "cell_number",
                                    "get_coordinates", self._CLASS_NAME)

    def _check_whether_cell_number_is_in_specified_range (self) -> None:
        if not (self._MIN_CELL_NUMBER <= self._cell_number <= self._MAX_CELL_NUMBER):
            raise ValueError ("\nАргумент cell_number функции get_coordinates\n"
                                            f"класса {self._CLASS_NAME} находится\n"
                                             "за пределами множества целых чисел "
                                            f"{self._format_set_of_valid_values}!\n"
                                            f"#| {self._cell_number} ∉ "
                                            f"{self._format_set_of_valid_values} |#")

    @property
    def _format_set_of_valid_values (self) -> str:
        return '{' + f"{self._MIN_CELL_NUMBER}; {self._MAX_CELL_NUMBER}" + '}'

    def _check_dispersion (self) -> None:
        self._check_int_dispersion ( )

    def _check_int_dispersion (self) -> None:
        if not isinstance (self._dispersion, int):
            raise IntArgumentError (self._dispersion, "dispersion",
                                    "get_coordinates", self._CLASS_NAME)

    def _set_initial_values_for_X_and_Y (self) -> None:
        self._X = self._START_X
        self._Y = self._START_Y

    def _calc_coordinates (self) -> None:
        for CELL in range (1, self._cell_number):
            self._Y += self._GAP
            self._ROW += 1
            self._shift_column_if_necessary ( )

    def _shift_column_if_necessary (self) -> None:
        if self._ROW // (self._LAST_ROW + 1):
            self._X += self._GAP
            self._Y = self._START_Y
            self._ROW = 1

    def _add_dispersion (self) -> None:
        self._X += self._dispersion
        self._Y += self._dispersion


class MovementInInventory (MovementPattern):
    def _initializing_start_values (self) -> None:
        self._START_X, self._START_Y = 725, 568
        self._set_initial_values_for_X_and_Y ( )

        self._MIN_CELL_NUMBER = 1
        self._MAX_CELL_NUMBER = 60

        self._GAP = 47
        self._ROW = 1
        self._LAST_ROW = 5

        self._CLASS_NAME = __class__.__name__

class MovementInStandartStashSection (MovementPattern):
    def _initializing_start_values (self) -> None:
        self._START_X, self._START_Y = 36, 158
        self._set_initial_values_for_X_and_Y ( )

        self._MIN_CELL_NUMBER = 1
        self._MAX_CELL_NUMBER = 144

        self._GAP = 47
        self._ROW = 1
        self._LAST_ROW = 12

class MovementInLargeStashSection (MovementPattern):
    def _initializing_start_values (self) -> None:
        self._START_X, self._START_Y = 25, 152
        self._set_initial_values_for_X_and_Y ( )

        self._MIN_CELL_NUMBER = 1
        self._MAX_CELL_NUMBER = 576

        self._GAP = 23
        self._ROW = 1
        self._LAST_ROW = 24


if __name__ == "__main__":
    test = MovementInInventory ( )
    coordinates = test.get_coordinates (76)
    print (coordinates)
    print ( )
