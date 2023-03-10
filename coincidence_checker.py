from screenshot_to_text import make_screenshot_and_get_text_from_it
from program_exceptions import StrArgumentError
from keyboard import wait


class CoincidenceChecker:
	def __init__ (self):
		self._coincidence_counter = 0
		self._old_text = ""

	def set_text_to_check (self, new_text: str) -> None:
		self._check_text (new_text)
		self._add_one_to_counter_if_old_and_new_text_match (new_text)
		self._reset_counter_if_old_and_new_text_do_not_match (new_text)
		self._old_text = new_text

	def _check_text (self, text: str) -> None:
		if not isinstance (text, str):
			raise StrArgumentError (text, "text",
									self.set_text_to_check.__name__,
									__class__.__name__)

	def _add_one_to_counter_if_old_and_new_text_match (self, text: str) -> None:
		if self._old_text == text:
			self._coincidence_counter += 1

	def _reset_counter_if_old_and_new_text_do_not_match (self, text: str) -> None:
		if self._old_text != text:
			self._coincidence_counter = 0

	def are_three_coincedences (self) -> bool:
		if self._coincidence_counter == 3:
			return True
		else:
			return False

	def get_coincedences_counter (self) -> int:
		return self._coincidence_counter


if __name__ == '__main__':
	button_to_press = "F2"

	print ("Если текст над курсором совпадёт 3 раза подряд, то программа сообщит об этом.")
	print (f"Нажми \"{button_to_press}\", чтобы сделать скриншот.\n")

	press_counter = 1
	coincidence_checker = CoincidenceChecker ( )
	while not coincidence_checker.are_three_coincedences ( ):
		wait (button_to_press)
		coincidence_checker.set_text_to_check (make_screenshot_and_get_text_from_it ( ))
		print (f"Сделан скриншот №{press_counter}:", "состояние счётчика совпадений:",
				coincidence_checker.get_coincedences_counter ( ))
		press_counter += 1

	print ("\nОбнаружено 3 совпадения подряд.")