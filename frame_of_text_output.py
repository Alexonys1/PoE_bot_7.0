from tkinter import LabelFrame
from tkinter import N, E, S, W, SUNKEN, WORD, INSERT

from tkinter.scrolledtext import ScrolledText

from frame_pattern import FramePattern


class FrameOfTextOutput (FramePattern):
	def run (self) -> None:
		self._create_frame_of_text_output ( )
		self._create_text_output_place ( )
		self._add_hello_text_to_text_output_place ( )

	def _create_frame_of_text_output (self) -> None:
		self._frame_of_text_output = LabelFrame (self._ROOT_WINDOW,
												text = "Окно вывода последних событий:")
		self._frame_of_text_output.grid (row = 0,
										column = 1,
										padx = 25,
										pady = 15,
										sticky = N+E+S+W)

	def _create_text_output_place (self) -> None:
		self._text_output_place = ScrolledText (self._frame_of_text_output,
												width=42,
												height=31,
												relief=SUNKEN,
												bd=2,
												font=("Arial", 10, "bold"),
												wrap=WORD)
		self._text_output_place.grid (row = 0, column = 0)

	def _add_hello_text_to_text_output_place (self) -> None:
		self.add_text_to_text_output_place ("WARNING! Перед тем как запустить\nпрограмму, убедись, что PoE уже открыто и\n")
		self.add_text_to_text_output_place ("что тайник расположен справа от\nперсонажа, а хранилище гильдии - слева.\n\n")
		self.add_text_to_text_output_place ("Настрой вкладки тайника и нажми\nкнопку \"СТАРТ!\"\n\n")
		self.add_text_to_text_output_place (f"{'/-/-' * 18} \n\n\n\n")

	def add_text_to_text_output_place (self, text: str) -> None:
		self._text_output_place.insert (INSERT, str (text))
