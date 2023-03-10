import pyautogui as pag
import cv2
from keyboard import wait


print ("Наведи курсор на секстанты в валютной вкладке тайника.\n")

while True:
	wait ("F2")
	if pag.locateCenterOnScreen (image = r"images\Selected sextant in currency tab.PNG",
								 region = (7, 130, 570, 570),
								 confidence = 0.9):
		print ("Есть выделенные секстанты в валютной вкладке тайника!")