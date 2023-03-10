from tkinter import Tk, Frame, Label, LabelFrame

from pyautogui import Size, size

from frame_pattern import FramePattern

from program_exceptions import IntArgumentError


class SizeLabels (FramePattern):
	def __init__ (self, root_window: Tk | Frame | LabelFrame, row: int):
		super().__init__(root_window = root_window)
		self._LAST_USED_ROW = row
		self._check_last_used_row ( )
		self._initialize_window_sizes ( )
		self._check_state_of_program ( )

	def _check_last_used_row (self) -> None:
		if not isinstance (self._LAST_USED_ROW, int):
			raise IntArgumentError (self._LAST_USED_ROW, "row",
                                    "__init__", __class__.__name__)

	def _initialize_window_sizes (self) -> None:
		self.current_screen_size = str (size ( ))
		self.required_screen_size = "Size(width=1280, height=1024)"

	def _check_state_of_program (self) -> None:
		if self.current_screen_size != self.required_screen_size:
			self.IS_NORMAL_STATE_OF_PROGRAM = False
		else:
			self.IS_NORMAL_STATE_OF_PROGRAM = True

	def run (self) -> None:
		self._create_label_of_current_window_size ( )
		self._create_label_of_state_of_program ( )

	def move_to_next_last_used_row (function: callable) -> callable:
		def call_function_and_move_to_next_last_used_row (self, *args, **kwargs):
			function (self, *args, **kwargs)
			self._LAST_USED_ROW += 1
		return call_function_and_move_to_next_last_used_row

	@move_to_next_last_used_row
	def _create_label_of_current_window_size (self) -> None:
		size_label = Label (self._ROOT_WINDOW,
			text = f"Текущее разрешение экрана: {self.format_current_screen_size}",
			fg = "blue")
		size_label.grid (row = self._LAST_USED_ROW, column = 0)

	@property
	def format_current_screen_size (self) -> str:
		current_screen_size = tuple (size ( ))
		current_screen_size = f"{current_screen_size[0]}x{current_screen_size[1]}"
		return current_screen_size

	@property
	def format_required_screen_size (self) -> str:
		required_screen_size = tuple (eval (self.required_screen_size))
		required_screen_size = f"{required_screen_size[0]}x{required_screen_size[1]}"
		return required_screen_size

	@move_to_next_last_used_row
	def _create_label_of_state_of_program (self) -> None:
		label_of_state_of_program = Label (self._ROOT_WINDOW)

		if self.IS_NORMAL_STATE_OF_PROGRAM:
			label_of_state_of_program.configure (
				text = "Программа запущена в\nстандартном режиме.",
				fg = "darkgreen")
		else:
			label_of_state_of_program.configure (
				text = "Программа не может\nбыть запущена!",
				fg = "red")

		label_of_state_of_program.grid (row = self._LAST_USED_ROW,
										column = 0)

	def _move_to_next_last_uesd_row (self) -> None:
		self._LAST_USED_ROW += 1

	def get_last_used_row (self) -> int:
		return self._LAST_USED_ROW - 1
