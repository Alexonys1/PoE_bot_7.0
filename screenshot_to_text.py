from point_coordinates import Point, Region

import pyautogui as pag

from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from keyboard import wait


def make_screenshot_and_get_text_from_it ( ) -> str:
	screenshot_path = r"C:\Users\Public\Pictures\Фото свойств.png"
	_make_screenshot (screenshot_path = screenshot_path, region = _get_screenshot_area ( ))
	screenshot = _make_black_and_white_screenshot (screenshot_path = screenshot_path)
	return pytesseract.image_to_string (screenshot, lang = "rus").upper ( )


def _make_screenshot (screenshot_path: str, *args, **kwargs) -> None:
	pag.screenshot (screenshot_path, *args, **kwargs)


def _get_screenshot_area ( ) -> Region:
	upper_left_corner_of_screenshot_area = _get_current_cursor_position() - _get_point_for_distance()
	width_and_height_of_screenshot_area = Point (x_coordinate = 690, y_coordinate = 260)

	return Region (*upper_left_corner_of_screenshot_area, *width_and_height_of_screenshot_area)


def _get_current_cursor_position ( ) -> Point:
	return Point (*pag.position ( ))


def _get_point_for_distance ( ) -> Point:
	return Point (x_coordinate = 340, y_coordinate = 320)


def _make_black_and_white_screenshot (screenshot_path: str) -> Image:
	screenshot = Image.open (screenshot_path)
	thresh = 80
	la = lambda x: 255 if x > thresh else 0
	screenshot = screenshot.convert ('L').point (la, mode='1')
	return screenshot



if __name__ == "__main__":
	print ("Нажми \"F2\" для запуска.", end="\n\n")
	wait ("F2")
	print (make_screenshot_and_get_text_from_it ( ))