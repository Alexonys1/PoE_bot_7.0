from tkinter import Tk, Toplevel, Label
from tkinter import RIDGE

from frame_pattern import FramePattern

from pyautogui import size


class ErrorWindow (FramePattern):
	def run (self) -> None:
		self._error_window = Toplevel (self._ROOT_WINDOW)
		self._configure_error_window ( )
		self._add_label_with_error_text ( )
		self._set_focus ( )

	def _configure_error_window (self) -> None:
		self._error_window.title ("Ошибка")
		self._error_window.geometry ("220x90")
		self._error_window.resizable (False, False)
		self._error_window.iconbitmap (r"..\images\Error.ico")

	def _add_label_with_error_text (self) -> None:
		Label (self._error_window,
			   height = 200,
			   width = 100,
			   text = f"Разрешение экрана не\nсовпадает с 1280x1024!\nПрограмма будет работать\nнекорректно!",
			   relief = RIDGE,
			   fg = "red",
			   font = "bold"
			  ).pack ( )

	def _set_focus (self) -> None:
		self._error_window.grab_set ( )
		self._error_window.focus_set ( )
		self._error_window.wait_window ( )