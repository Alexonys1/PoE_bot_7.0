from tkinter import Tk, Frame, LabelFrame, Button, BooleanVar
from tkinter import N, E, S, W

from frame_pattern import FramePattern

from size_labels import SizeLabels
from info_frame import InfoFrame
from roller import Roller
from counters import Counters
from save_and_load_buttons import SaveAndLoadButtons

from pyautogui import FailSafeException, keyUp


class ControlFrame (FramePattern):
	def __init__ (self, root_window: Tk | Frame | LabelFrame,
						dict_of_search_parameters: dict[str, BooleanVar],
						function_for_save_parameters: callable,
						function_for_load_parameters: callable,
						function_for_text_output: callable):
		super().__init__(root_window = root_window)
		self._dict_of_search_parameters = dict_of_search_parameters
		self._function_for_save_parameters = function_for_save_parameters
		self._function_for_load_parameters = function_for_load_parameters
		self._function_for_text_output = function_for_text_output
		self._LAST_USED_ROW = 0

	def run (self) -> None:
		self._create_control_frame ( )
		self._join_info_frame ( )
		self._join_start_button ( )
		self._join_size_labels ( )
		self._join_counters ( )
		self._join_save_and_load_buttons ( )

	def _create_control_frame (self) -> None:
		self._control_frame = Frame (self._ROOT_WINDOW)
		self._control_frame.grid (row = 0,
							   column = 2,
							     padx = 15,
							     pady = 15,
							   sticky = N+E+S+W)

	def move_to_next_last_used_row (function: callable) -> callable:
		def call_function_and_move_to_next_last_used_row (self, *args, **kwargs):
			print ("Создан новый объект в классе", __class__.__name__,
				   "на ряду №", self._LAST_USED_ROW)
			function (self, *args, **kwargs)
			self._LAST_USED_ROW += 1
		return call_function_and_move_to_next_last_used_row

	@move_to_next_last_used_row
	def _join_info_frame (self) -> None:
		self._info_frame = InfoFrame (root_window = self._control_frame)
		self._info_frame.grid (self._LAST_USED_ROW)

	@move_to_next_last_used_row
	def _join_start_button (self) -> None:
		Button (self._control_frame,
				text = "СТАРТ!",
				font="60",
				bg="orange",
				fg="red",
				activebackground="orange",
				activeforeground="green",
				command=self._run_roll,
				width=26,
				height=4
			   ).grid (row = self._LAST_USED_ROW,
			   		column = 0,
			   		padx = 13,
			   		pady = 10,
			   		sticky = W)

	def _run_roll (self) -> None:
		if self.size_labels.IS_NORMAL_STATE_OF_PROGRAM:
			self._function_for_text_output ("\"СТАРТ!\" НАЖАТ!\n\n")
			self._roller = Roller (dict_of_search_parameters = self._dict_of_search_parameters,
                    function_for_set_sextants_for_counter = self.counters.set_sextants_for_counter,
                    function_for_set_compasses_for_counter = self.counters.set_compasses_for_counter,
                    function_for_text_output = self._function_for_text_output)
			self._roller.run_roll ( )
		else:
			self._function_for_text_output ("Программа не может быть запущена, так как ")
			self._function_for_text_output (f"текущее разрешение не {self.size_labels.format_required_screen_size}!\n\n")

	@move_to_next_last_used_row
	def _join_size_labels (self) -> None:
		self.size_labels = SizeLabels (root_window = self._control_frame,
									   row = self._LAST_USED_ROW)
		self.size_labels.run ( )
		self._LAST_USED_ROW = self.size_labels.get_last_used_row ( )

	@move_to_next_last_used_row
	def _join_counters (self) -> None:
		self.counters = Counters (root_window = self._control_frame,
								  row = self._LAST_USED_ROW)
		self.counters.run ( )
		self._LAST_USED_ROW = self.counters.get_last_used_row ( )

	@move_to_next_last_used_row
	def _join_save_and_load_buttons (self) -> None:
		self.save_and_load_buttons = SaveAndLoadButtons (
			root_window = self._control_frame, row = self._LAST_USED_ROW,
			function_for_save_parameters = self._function_for_save_parameters,
			function_for_load_parameters = self._function_for_load_parameters)
		self.save_and_load_buttons.run ( )

	@property
	def state_of_program (self) -> bool:
		return self.size_labels.IS_NORMAL_STATE_OF_PROGRAM
