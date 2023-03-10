from tkinter import Tk, Frame, Label, LabelFrame

from frame_pattern import FramePattern

from program_exceptions import IntArgumentError


class Counters (FramePattern):
	def __init__ (self, root_window: Tk | Frame | LabelFrame, row: int):
		super().__init__(root_window = root_window)
		self._LAST_USED_ROW = row
		self._check_last_used_row ( )

	def _check_last_used_row (self) -> None:
		if not isinstance (self._LAST_USED_ROW, int):
			raise IntArgumentError (self._LAST_USED_ROW, "row",
                                    "__init__", self.__class__.__name__)

	def run (self) -> None:
		self._join_sextant_counter ( )
		self._join_compass_counter ( )

	def move_to_next_last_used_row (function: callable) -> callable:
		def call_function_and_move_to_next_last_used_row (self, *args, **kwargs):
			function (self, *args, **kwargs)
			self._LAST_USED_ROW += 1
		return call_function_and_move_to_next_last_used_row

	@move_to_next_last_used_row
	def _join_sextant_counter (self) -> None:
		self.label_of_sextant_counter = Label (self._ROOT_WINDOW,
											   text = "Секстантов потрачено: 0",
											   font = 10
											  )
		self.label_of_sextant_counter.grid (row = self._LAST_USED_ROW,
											column = 0,
											pady = 3)

	@move_to_next_last_used_row
	def _join_compass_counter (self) -> None:
		self.label_of_compass_counter = Label (self._ROOT_WINDOW,
											   text = "Компасов потрачено: 0",
											   font = 10
											  )
		self.label_of_compass_counter.grid (row = self._LAST_USED_ROW,
											column = 0,
											pady = 3)

	def set_sextants_for_counter (self, number_of_sextants: int) -> None:
		self._check_sextants (number_of_sextants)
		self.label_of_sextant_counter.configure (
			text = f"Секстантов потрачено: {number_of_sextants}")

	def set_compasses_for_counter (self, number_of_compasses: int) -> None:
		self._check_compasses (number_of_compasses)
		self.label_of_compass_counter.configure (
			text = f"Компасов потрачено: {number_of_compasses}")

	def _check_sextants (self, number: int) -> None:
		if not isinstance (number, int):
			raise IntArgumentError (number, "number_of_sextants",
                                    "set_sextants_for_counter",
                                    __class__.__name__)
		elif number < 0:
			raise ValueError ("Аргумент number_of_sextants, метода set_sextants_for_counter, " +
							 f"класса {__class__.__name__}, отрицателен!\n" +
							 f"{number} < 0.")

	def _check_compasses (self, number: int) -> None:
		if not isinstance (number, int):
			raise IntArgumentError (number, "number_of_compasses",
                                    "set_compasses_for_counter",
                                    __class__.__name__)
		elif number < 0:
			raise ValueError ("Аргумент number_of_compasses, метода set_compasses_for_counter, " +
							 f"класса {__class__.__name__}, отрицателен!\n" +
							 f"{number} < 0.")

	def _move_to_next_last_used_row (self) -> None:
		self._LAST_USED_ROW += 1

	def get_last_used_row (self) -> int:
		return self._LAST_USED_ROW - 1
