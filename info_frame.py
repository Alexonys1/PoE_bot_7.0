from tkinter import Tk, Frame, Label, LabelFrame
from tkinter import W

from frame_pattern import FramePattern

from program_exceptions import ArgumentError


class InfoFrame (FramePattern):
	def __init__ (self, root_window: Tk | Frame | LabelFrame):
		super().__init__(root_window = root_window)
		self._LAST_USED_ROW = 0
		self.run ( )

	def run (self) -> None:
		self._create_info_frame ( )
		self._show_all_labels ( )

	def _create_info_frame (self) -> None:
		self._info_frame = LabelFrame (self._ROOT_WINDOW,
									   text = "Настройка вкладок тайника:")

	def _show_all_labels (self) -> None:      #|                                         |#
		self._add_label_to_info_frame (text = "Секстанты и компасы берутся из тайника,", underline = 0)
		self._add_label_to_info_frame (text = "из вкладки \"Валюта\" тёмно-красного цвета.", fg = "darkred")
		self._add_label_to_info_frame (text = "Готовые компасы перекладываются в", underline = 0)
		self._add_label_to_info_frame (text = "хранилище гильдии, в вкладку \"4\"")
		self._add_label_to_info_frame (text = "зелёного цвета.", fg = "darkgreen")
		self._add_label_to_info_frame (text = "Реализация \"Если кончилось место, то", underline = 0, fg = "darkblue")
		self._add_label_to_info_frame (text = "перекладывать в новую вкладку\"", fg = "darkblue")
		self._add_label_to_info_frame (text = "пока не осуществлена.", fg = "darkblue")
											  #|                                         |#

	def _add_label_to_info_frame (self, *args, **kwargs) -> None:
		label = Label (self._info_frame, *args, **kwargs)
		label.grid (row = self._LAST_USED_ROW,
				 column = 0,
				 sticky = W)
		self._move_to_next_row ( )

	def _move_to_next_row (self) -> None:
		self._LAST_USED_ROW += 1

	def grid (self, row: int) -> None:
		self._check_row (row)
		self._info_frame.grid (row = row,
							column = 0)

	def _check_row (self, row: int) -> None:
		if not isinstance (row, int):
			raise ArgumentError (row, "row", "set_row", self.__class__.__name__)
