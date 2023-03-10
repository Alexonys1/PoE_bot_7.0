import json

from tkinter import Tk, Frame, LabelFrame, Checkbutton, Button
from tkinter import W, E, BooleanVar

from math import ceil

from dict_of_search_parameters import create_dict_of_search_parameters
from frame_pattern import FramePattern


class FrameOfCheckButtons (FramePattern):
    def __init__ (self, root_window: Tk | Frame | LabelFrame):
        super().__init__(root_window = root_window)
        self._dict_of_search_parameters = create_dict_of_search_parameters ( )

    @property
    def dict_of_search_parameters (self) -> dict[str, BooleanVar]:
        return self._dict_of_search_parameters

    def run (self) -> None:
        self._create_frame_of_check_buttons ( )
        self._create_check_buttons ( )
        self._create_button_that_switch_on_all_check_buttons ( )
        self._create_button_that_switch_off_all_check_buttons ( )

    def _create_frame_of_check_buttons (self) -> None:
        self._frame_of_check_buttons = LabelFrame (self._ROOT_WINDOW, text = "Поиск свойств:")
        self._frame_of_check_buttons.grid (row = 0, column = 0, padx = 25, pady = 15)

    def _create_check_buttons (self) -> None:
        self._initialize_row_and_column ( )

        for check_button_text, check_button_position in self._dict_of_search_parameters.items ( ):
            check_button_position.set (True)
            self._create_one_check_button (check_button_text, check_button_position)
            self._move_to_next_row ( )
            self._create_second_column_if_necessary ( )

    def _initialize_row_and_column (self) -> None:
        self._ROW = 0
        self._COLUMN = 0

    def _create_one_check_button (self, check_button_text: str,
                                    check_button_position: BooleanVar) -> None:
        Checkbutton (self._frame_of_check_buttons,
                     text = check_button_text,
                     variable = check_button_position,
                     font = ("Bold", 9, "italic")
                    ).grid (row = self._ROW,
                            column = self._COLUMN,
                            sticky = W)

    def _move_to_next_row (self) -> None:
        self._ROW += 1

    def _create_second_column_if_necessary (self) -> None:
        self._CHECK_BUTTONS_IN_FIRST_COLUMN = ceil (len (self._dict_of_search_parameters) / 2)

        if self._ROW == self._CHECK_BUTTONS_IN_FIRST_COLUMN:
            self._ROW = 0
            self._COLUMN += 1

    def _create_button_that_switch_on_all_check_buttons (self) -> None:
        Button (self._frame_of_check_buttons,
                text = "Выделить всё",
                command = self._switch_on_all_check_buttons,
                underline = 0,
                activeforeground = "green"
               ).grid (row = self._CHECK_BUTTONS_IN_FIRST_COLUMN + 1,
                       column = 0,
                       sticky = W)

    def _create_button_that_switch_off_all_check_buttons (self) -> None:
        Button (self._frame_of_check_buttons,
                text = "Снять выделение",
                command = self._switch_off_all_check_buttons,
                underline = 0,
                activeforeground = "red"
               ).grid (row = self._CHECK_BUTTONS_IN_FIRST_COLUMN + 1,
                       column = 1,
                       sticky = E)

    def _switch_on_all_check_buttons (self) -> None:
        for dict_key in self._dict_of_search_parameters:
            self._dict_of_search_parameters[dict_key].set (True)

    def _switch_off_all_check_buttons (self) -> None:
        for dict_key in self._dict_of_search_parameters:
            self._dict_of_search_parameters[dict_key].set (False)

    def save_parameters (self) -> None:
        new_dict_of_search_parameters = self._create_new_dict_of_search_parameters ( )

        with open (r"..\saved_search_parameters.json", "w") as write_file:
            json.dump (new_dict_of_search_parameters, write_file)

    def _create_new_dict_of_search_parameters (self) -> dict[str, bool]:
        new_dict_of_search_parameters = { }

        for check_button_text, check_button_position in self._dict_of_search_parameters.items ( ):
            new_dict_of_search_parameters[check_button_text] = check_button_position.get ( )

        return new_dict_of_search_parameters

    def load_parameters (self) -> None:
        with open (r"..\saved_search_parameters.json", "r") as read_file:
            saved_dict_of_search_parameters = json.load (read_file)

        for dict_key, check_button_position in saved_dict_of_search_parameters.items ( ):
            self._dict_of_search_parameters[dict_key].set (check_button_position)
