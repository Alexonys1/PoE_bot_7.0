from tkinter import Tk

from frame_of_check_buttons import FrameOfCheckButtons
from frame_of_text_output import FrameOfTextOutput
from control_frame import ControlFrame
from error_window import ErrorWindow


class MainWindow:
	def __init__ (self):
		self._root = Tk ( )

		self._root.title ("Программа для ролла секстантов v7.0")
		self._root.geometry ("1030x570")
		self._root.resizable (False, False)
		self._root.iconbitmap (r"..\images\Симпсон.ico")

	def run (self) -> None:
		self._run_first_frame ( )
		self._run_second_frame ( )
		self._run_third_frame ( )

		self._call_error_window_if_necessary ( )

		self._root.mainloop ( )

	def _run_first_frame (self) -> None:
		self.frame_of_check_buttons = FrameOfCheckButtons (root_window = self._root)
		self.frame_of_check_buttons.run ( )

	def _run_second_frame (self) -> None:
		self.frame_of_text_output = FrameOfTextOutput (root_window = self._root)
		self.frame_of_text_output.run ( )

	def _run_third_frame (self) -> None:
		self.control_frame = ControlFrame (
			root_window = self._root,
			dict_of_search_parameters = self.frame_of_check_buttons.dict_of_search_parameters,
			function_for_save_parameters = self._save_parameters,
			function_for_load_parameters = self._load_parameters,
			function_for_text_output = self.frame_of_text_output.add_text_to_text_output_place)
		self.control_frame.run ( )

	def _save_parameters (self) -> None:
		self.frame_of_check_buttons.save_parameters ( )
		self.frame_of_text_output.add_text_to_text_output_place (
            "Текущие настройки свойств сохранены!\n\n")

	def _load_parameters (self) -> None:
		try:
			self.frame_of_check_buttons.load_parameters ( )
		except FileNotFoundError:
			self.frame_of_text_output.add_text_to_text_output_place (
				"Нет сохранённого файла с настройками свойств!\n\n")
		else:
			self.frame_of_text_output.add_text_to_text_output_place (
                "Загружены настройки свойств!\n\n")

	def _call_error_window_if_necessary (self) -> None:
		self.state_of_program = self.control_frame.state_of_program
		if not self.state_of_program:
			self._create_error_window ( )

	def _create_error_window (self) -> None:
		error_window = ErrorWindow (root_window = self._root)
		error_window.run ( )



if __name__ == '__main__':
	main_window = MainWindow ( )
	main_window.run ( )
