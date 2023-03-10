import cv2
import pyautogui as pag

from point_coordinates import Region

from program_exceptions import PoeNotFound


def find_and_open_poe ( ) -> None:
    poe_coordinates = pag.locateOnScreen (image = _get_name_of_poe_image ( ),
                                          region = _get_region_find_poe ( ),
                                          confidence = 0.9)
    if poe_coordinates:
        pag.moveTo (poe_coordinates)
        pag.click (button = "left")
    else:
        raise PoeNotFound ( )

def _get_name_of_poe_image ( ) -> str:
    return r"..\images\PoE.PNG"

def _get_region_find_poe ( ) -> Region:
    return Region (0, 980, 1280, 44)


if __name__ == "__main__":
    find_and_open_poe ( )