import pyautogui as pag
from keyboard import wait


current_size_of_screen = pag.size ( )
print (f"Текущее разрешение экрана: {current_size_of_screen[0]}x{current_size_of_screen[1]}.")
print ( )
print ("Нажми \"F2\", чтобы узнать координаты местоположения курсора.\n\n")


count = 1
while True:
	wait ("F2")
	current_coordinates_of_mouse_cursor = pag.position ( )
	print (f"Пуск №{count}:",
			"{" + f"{current_coordinates_of_mouse_cursor[0]};", f"{current_coordinates_of_mouse_cursor[1]}" +"}")
	count += 1