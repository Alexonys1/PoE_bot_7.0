import pyautogui as pag
from keyboard import wait


def _get_name_of_required_button ( ) -> str:
	return "F2"


current_size_of_screen = pag.size ( )
print (f"Текущее разрешение экрана: {current_size_of_screen[0]}x{current_size_of_screen[1]}.")
print ( )
print ("Регион - это координаты его верхнего левого угла, его ширина и высота.")


count = 1
while True:
	print ("\nНаведи курсор на верхний левый угол искомого региона и нажми", _get_name_of_required_button() + ".")
	wait (_get_name_of_required_button ( ))
	x_coordinate_of_top_left_corner, y_coordinate_of_top_left_corner = pag.position ( )

	print ("Теперь наведись на нижний правый угол искомого региона и нажми", _get_name_of_required_button() + ".")
	wait (_get_name_of_required_button ( ))
	x_coordinate_of_lower_right_corner, y_coordinate_of_lower_right_corner = pag.position ( )
	print ( )

	print (f"Размеры искомого региона №{count}:")
	print ("X-координата верхнего левого угла:", x_coordinate_of_top_left_corner)
	print ("Y-координата верхнего левого угла:", y_coordinate_of_top_left_corner)
	print ("Ширина:", x_coordinate_of_lower_right_corner - x_coordinate_of_top_left_corner)
	print ("Высота:", y_coordinate_of_lower_right_corner - y_coordinate_of_top_left_corner)

	print ( ); count += 1