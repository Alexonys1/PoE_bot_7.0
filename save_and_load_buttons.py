from tkinter import Tk, Frame, LabelFrame, PhotoImage, Label, Button

from frame_pattern import FramePattern


class SaveAndLoadButtons (FramePattern):
	def __init__ (self, root_window: Tk | Frame | LabelFrame, row: int,
						function_for_save_parameters: callable,
						function_for_load_parameters: callable):
		super().__init__(root_window = root_window)
		self._LAST_USED_ROW = row
		self.save_parameters = function_for_save_parameters
		self.load_parameters = function_for_load_parameters

	def run (self) -> None:
		self._create_frame_of_two_buttons_with_images ( )
		self._create_save_button ( )
		self._create_load_button ( )
		self._create_image_for_save_button ( )
		self._create_image_for_load_button ( )

	def _create_frame_of_two_buttons_with_images (self) -> None:
		self.frame_of_two_buttons = Frame (self._ROOT_WINDOW)
		self.frame_of_two_buttons.grid (row = self._LAST_USED_ROW,
										column = 0,
										pady = 10)
		self._COLUMN_OF_BUTTONS = 0
		self._COLUMN_OF_IMAGES = 1

	def _create_save_button (self) -> None:
		Button (self.frame_of_two_buttons,
				text = "Сохранить настройки",
				command = self.save_parameters
			   ).grid (row = 0, column = self._COLUMN_OF_BUTTONS)

	def _create_load_button (self) -> None:
		Button (self.frame_of_two_buttons,
				text = "Загрузить настройки",
				command = self.load_parameters
			   ).grid (row = 1, column = self._COLUMN_OF_BUTTONS)

	def _create_image_for_save_button (self) -> None:
		self.image_of_save_floppy_disk = PhotoImage (file = r"..\images\Save floppy disk.png")
		# Фото должно быть в глобальной области видимости,
		# иначе tkinter сочтёт его за мусор и не отобразит.
		# Фото должно быть в формате PNG!
		Label (self.frame_of_two_buttons,
			   image = self.image_of_save_floppy_disk
			  ).grid (row = 0, column = self._COLUMN_OF_IMAGES)

	def _create_image_for_load_button (self) -> None:
		self.image_of_load_floppy_disk = PhotoImage (file = r"..\images\Load floppy disk.png")
		# Фото должно быть в глобальной области видимости,
		# иначе tkinter сочтёт его за мусор и не отобразит.
		# Фото должно быть в формате PNG!
		Label (self.frame_of_two_buttons,
			   image = self.image_of_load_floppy_disk
			  ).grid (row = 1, column = self._COLUMN_OF_IMAGES)
