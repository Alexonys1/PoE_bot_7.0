import time
import pyautogui as pag
from tkinter import BooleanVar
from typing import Callable, Generator
from point_coordinates import Point, Region
from poe_finder import find_and_open_poe
from random import randint, uniform
from screenshot_to_text import make_screenshot_and_get_text_from_it
from coincidence_checker import CoincidenceChecker
from place_coordinates_and_names_of_images import *
from program_exceptions import *
# Также есть зависимость от opencv (cv2)


class Roller:
    def __init__ (self, dict_of_search_parameters: dict[str, BooleanVar],
                        function_for_set_sextants_for_counter: Callable[[int], None],
                        function_for_set_compasses_for_counter: Callable[[int], None],
                        function_for_text_output: Callable[[str], None]):
        self._search_parameters = dict_of_search_parameters
        self._set_sextants_for_counter = function_for_set_sextants_for_counter
        self._set_compasses_for_counter = function_for_set_compasses_for_counter
        self._text_output = function_for_text_output

        self._CLASS_NAME = __class__.__name__
        self._SEXTANT_COUNT = 0
        self._COMPASS_COUNT = 0


    def run_roll (self) -> None:
        self._initialize_variables_of_methods ( )

        try:
            find_and_open_poe ( )
        except PoeNotFound as error_text:
            self._text_output (error_text)
        else:
            self._run_main_cycle ( )
            self._show_end_message ( )

    def _initialize_variables_of_methods (self) -> None:
        self._CURRENCY_INVENTORY_TAB_IS_OPEN = False
        self._BIG_GUILD_TAB_IS_OPEN = False
        self._CRAFT_PLACE_IS_EMPTY = False
        self._SEXTANTS_ARE_IN_CURRENCY_TAB = True
        self._COMPASSES_ARE_IN_CURRENCY_TAB = True
        self._screenshot_text = ""
        self._coincidence_checker = CoincidenceChecker ( )

    def _run_main_cycle (self) -> None:
        while self._SEXTANTS_ARE_IN_CURRENCY_TAB and self._COMPASSES_ARE_IN_CURRENCY_TAB:
            self._body_of_main_cycle ( )

    def _body_of_main_cycle (self) -> None:
        self._open_stash ( )
        self._open_currency_tab_if_it_is_not_open ( )
        try:
            self._find_and_take_sextants_in_currency_tab ( )
            self._find_and_take_compasses_in_currency_tab ( )
        except (SextantsInCurrencyTabNotFound, CompassesInCurrencyTabNotFound) as error_text:
            self._text_output (error_text)
        else:
            self._open_atlas_and_inventory ( )
            self._run_roll_cycle ( )

            self._close_atlas_and_inventory ( )
            self._open_guild_stash ( )
            self._open_big_guild_tab_if_it_is_not_open ( )
            self._unload_charged_compasses_in_guild_stash ( )
            self._close_guild_stash ( )


    def _move_to_point (self, point: Point,
                        x_dispersion: int = 0,
                        y_dispersion: int = 0,
                        duration: float = -1) -> None:
        self._check_point (point = point,
                     method_name = self._move_to_point.__name__)
        duration = self._check_and_get_standart_duration_if_duration_is_negative (duration)
        point.add_dispersion (x_dispersion, y_dispersion)
        pag.moveTo (*point, duration = duration)

    def _check_point (self, point: Point, method_name: str) -> None:
        if not isinstance (point, Point):
            raise PointArgumentError (argument = point, argument_name = "point",
                    name_of_method_or_function = method_name,
                                    class_name = self._CLASS_NAME)

    def _check_and_get_standart_duration_if_duration_is_negative (self, duration: float) -> float:
        self._check_duration (duration)
        if duration < 0:
            return self._standart_duration
        else:
            return duration

    def _check_duration (self, duration: int | float) -> None:
        if not isinstance (duration, (int, float)):
            raise IntOrFloatArgumentError (argument = duration,
                                      argument_name = "duration",
                         name_of_method_or_function = self._check_and_get_standart_duration_if_duration_is_negative.__name__,
                                         class_name = self._CLASS_NAME)

    @property
    def _standart_duration (self) -> float:
        return uniform (0.11, 0.42)


    def _open_stash (self) -> None:
        self._move_to_point_with_small_dispersion (coordinates_of_stash)
        self._left_mouse_click ( )
        self._text_output ("Открыт тайник.\n\n")

    def _move_to_point_with_small_dispersion (self, point: Point, duration: float = -1) -> None:
        self._move_to_point (point = point, x_dispersion = self._get_small_dispersion ( ),
                                            y_dispersion = self._get_small_dispersion ( ),
                                            duration = duration)

    def _get_small_dispersion (self) -> int:
        return randint (-4, 4)

    def _left_mouse_click (self) -> None:
        pag.click (button = "left")

    def _right_mouse_click (self) -> None:
        pag.click (button = "right")


    def _open_currency_tab_if_it_is_not_open (self) -> None:
        if not self._CURRENCY_INVENTORY_TAB_IS_OPEN:
            self._move_to_point_with_small_dispersion (coordinates_of_currency_tab_in_inventory)
            self._left_mouse_click ( )
            self._CURRENCY_INVENTORY_TAB_IS_OPEN = True


    def _find_and_take_sextants_in_currency_tab (self) -> None:
        self._move_to_point_with_small_dispersion (coordinates_of_sextant_in_currency_tab)
        self._check_if_sextant_is_in_currency_tab ( )
        if self._SEXTANTS_ARE_IN_CURRENCY_TAB:
            self._take_as_many_sextants_as_necessary ( )
            self._check_if_sextant_is_in_currency_tab ( )
            self._SEXTANTS_ARE_IN_INVENTORY = True
        else:
            self._SEXTANTS_ARE_IN_INVENTORY = False
            raise SextantsInCurrencyTabNotFound ( )

    def _check_if_sextant_is_in_currency_tab (self) -> None:
        coordinates = pag.locateCenterOnScreen (image = name_of_image_with_selected_sextant_in_currency_tab,
                                          region = stash_region,
                                          confidence = 0.88)
        if coordinates: self._SEXTANTS_ARE_IN_CURRENCY_TAB = True
        else: self._SEXTANTS_ARE_IN_CURRENCY_TAB = False

    def _take_as_many_sextants_as_necessary (self) -> None:
        sextant_pack_number = 0
        self._hold_down_ctrl ( )
        for empty_cell_number in self._get_generator_with_coordinates_of_empty_inventory_cells (
                region = sextant_region_in_inventory):
            self._left_mouse_click ( )
            sextant_pack_number += 1
            time.sleep (uniform (0.04, 0.1))
        self._text_output (f"Загружено {self._pack_number_to_prepared_string(sextant_pack_number)} секстантов.\n\n")
        self._release_ctrl ( )

    def _hold_down_ctrl (self) -> None:
        pag.keyDown ("ctrl")

    def _release_ctrl (self) -> None:
        pag.keyUp ("ctrl")

    def _hold_down_shift (self) -> None:
        pag.keyDown ("shift")

    def _release_shift (self) -> None:
        pag.keyUp ("shift")

    def _get_generator_with_coordinates_of_empty_inventory_cells (self, region: Region) -> Generator:
        return pag.locateAllOnScreen (image = image_name_of_empty_inventory_cell,
                                      region = region,
                                      confidence = 0.88)

    def _pack_number_to_prepared_string (self, pack_number: int) -> str:
        if pack_number == 1: return f"{pack_number} пак"
        elif 2 <= pack_number <= 4: return f"{pack_number} пака"
        elif 5 <= pack_number <= 10 or pack_number == 0: return f"{pack_number} паков"
        else: raise ValueError (f"Аргумент метода {self._pack_number_to_prepared_string.__name__} " +
                                 "должен быть в пределах диапозона целых чисел от 1 до 10!\n" +
                                 f"{pack_number} ∉ " + "{1; 10}")


    def _find_and_take_compasses_in_currency_tab (self) -> None:
        self._move_to_point_with_small_dispersion (coordinates_of_compass_in_currency_tab)
        self._check_if_compass_is_in_currency_tab ( )
        if self._COMPASSES_ARE_IN_CURRENCY_TAB:
            self._take_as_many_compasses_as_necessary ( )
            self._check_if_compass_is_in_currency_tab ( )
            self._COMPASSES_ARE_IN_INVENTORY = True
        else:
            self._COMPASSES_ARE_IN_INVENTORY = False
            raise CompassesInCurrencyTabNotFound ( )

    def _check_if_compass_is_in_currency_tab (self) -> None:
        coordinates = pag.locateOnScreen (image = name_of_image_with_selected_compass_in_currency_tab,
                                          region = stash_region,
                                          confidence = 0.88)
        if coordinates: self._COMPASSES_ARE_IN_CURRENCY_TAB = True
        else: self._COMPASSES_ARE_IN_CURRENCY_TAB = False

    def _take_as_many_compasses_as_necessary (self) -> None:
        compass_pack_number = 0
        self._hold_down_ctrl ( )
        for empty_inventory_cell_number in self._get_generator_with_coordinates_of_empty_inventory_cells (
                region = compass_region_in_inventory):
            self._left_mouse_click ( )
            compass_pack_number += 1
            time.sleep (uniform (0.04, 0.1))
        self._text_output (f"Загружено {self._pack_number_to_prepared_string(compass_pack_number)} компасов.\n\n")
        self._release_ctrl ( )


    def _open_atlas_and_inventory (self) -> None:
        pag.press ('g')
        time.sleep (0.1)
        pag.press ('i')


    def _run_roll_cycle (self) -> None:
        while self._SEXTANTS_ARE_IN_INVENTORY and self._COMPASSES_ARE_IN_INVENTORY:
            self._body_of_roll_cycle ( )

    def _body_of_roll_cycle (self) -> None:
        if self._CRAFT_PLACE_IS_EMPTY:
            self._roll ( )
            self._packaging_of_charged_compass_if_sextants_are_in_inventory ( )
        else:
            self._move_to_craft_place ( )
            if self._needed_parameters_are_in_craft_place ( ):
                self._packaging_of_charged_compass_if_sextants_are_in_inventory ( )
            self._CRAFT_PLACE_IS_EMPTY = True

    def _roll (self) -> None:
        coordinates_of_sextant_in_inventory = self._get_coordinates_of_sextant_in_inventory ( )
        if coordinates_of_sextant_in_inventory:
            self._hold_down_shift ( )
            self._move_to_point (coordinates_of_sextant_in_inventory)
            self._right_mouse_click ( )
            self._move_to_craft_place ( )
            self._roll_required_charged_compass ( )
        else:
            self._SEXTANTS_ARE_IN_INVENTORY = False

    def _get_coordinates_of_sextant_in_inventory (self) -> Point:
        coordinates_of_sextant_in_inventory = pag.locateCenterOnScreen (
                image = name_of_image_with_unselected_sextant_in_inventory,
                region = sextant_region_in_inventory,
                confidence = 0.88)
        if coordinates_of_sextant_in_inventory: return Point (*coordinates_of_sextant_in_inventory)
        else: return None

    def _move_to_craft_place (self) -> None:    
        self._move_to_point (coordinates_of_craft_place, x_dispersion = randint (-1, 1),
                                                         y_dispersion = randint (-1, 1))

    def _needed_parameters_are_in_craft_place (self) -> bool:
        self._screenshot_text = make_screenshot_and_get_text_from_it ( )
        self._text_output (f"{self._screenshot_text}\n")
        self._coincidence_checker.set_text_to_check (self._screenshot_text)
        self._sextants_are_not_in_inventory_if_found_three_coincidences ( )
        if self._search_required_parameters ( ) or not self._SEXTANTS_ARE_IN_INVENTORY:
            return True
        else:
            return False

    def _search_required_parameters (self) -> bool:
        for parameter in self._search_parameters:
            if parameter.upper() in self._screenshot_text and \
            self._search_parameters[parameter].get():
                return True
        return False

    def _sextants_are_not_in_inventory_if_found_three_coincidences (self) -> None:
        if self._coincidence_checker.are_three_coincedences ( ):
            self._SEXTANTS_ARE_IN_INVENTORY = False
            self._SEXTANTS_ARE_IN_CURRENCY_TAB = False

    def _roll_required_charged_compass (self) -> None:
        while True:
            self._left_mouse_click ( )
            self._SEXTANT_COUNT += 1; self._set_sextants_for_counter (self._SEXTANT_COUNT)
            time.sleep (uniform (0.11, 0.2))
            if self._needed_parameters_are_in_craft_place ( ):
                self._release_shift ( ); break


    def _packaging_of_charged_compass_if_sextants_are_in_inventory (self) -> None:
        if self._SEXTANTS_ARE_IN_INVENTORY:
            self._move_to_found_unselected_compass ( )
            self._right_mouse_click ( )
            self._move_to_craft_place ( )
            self._left_mouse_click ( )
            self._COMPASS_COUNT += 1; self._set_compasses_for_counter (self._COMPASS_COUNT)
            self._move_to_any_empty_cell_in_inventory ( )
            self._left_mouse_click ( )

    def _move_to_found_unselected_compass (self) -> None:
        coordinates_of_unselected_compass_in_inventory = self._get_coordinates_of_unselected_compass_in_inventory ( )
        if coordinates_of_unselected_compass_in_inventory:
            self._move_to_point_with_small_dispersion (coordinates_of_unselected_compass_in_inventory)
        else:
            self._move_to_point (coordinates_of_place_near_craft_place_where_there_is_nothing,
                                 x_dispersion = randint (-4, 4),
                                 y_dispersion = randint (-4, 4))
            coordinates_of_unselected_compass_in_inventory = self._get_coordinates_of_unselected_compass_in_inventory ( )
            self._move_to_point_with_small_dispersion (coordinates_of_unselected_compass_in_inventory)

    def _get_coordinates_of_unselected_compass_in_inventory (self) -> Point:
        coordinates_of_unselected_compass_in_inventory = pag.locateCenterOnScreen (
                image = name_of_image_with_unselected_compass_in_inventory,
                region = compass_region_in_inventory,
                confidence = 0.88)
        if coordinates_of_unselected_compass_in_inventory:
            return Point (*coordinates_of_unselected_compass_in_inventory)
        else:
            return None

    def _move_to_any_empty_cell_in_inventory (self) -> None:
        coordinates_of_empty_cell_in_inventory = pag.locateCenterOnScreen (
                image = image_name_of_empty_inventory_cell,
                region = region_of_charged_compasses_in_inventory,
                confidence = 0.88)
        coordinates_of_empty_cell_in_inventory = Point (*coordinates_of_empty_cell_in_inventory)
        self._move_to_point_with_small_dispersion (coordinates_of_empty_cell_in_inventory)


    def _close_atlas_and_inventory (self) -> None:
        self._press_esc ( )

    def _press_esc (self) -> None:
        pag.press ("esc")


    def _open_guild_stash (self) -> None:
        self._move_to_point_with_small_dispersion (coordinates_of_guild_stash)
        self._left_mouse_click ( )
        self._text_output ("Открыто хранилище гильдии.\n\n")


    def _open_big_guild_tab_if_it_is_not_open (self) -> None:
        if not self._BIG_GUILD_TAB_IS_OPEN:
            self._move_to_point_with_small_dispersion (coordinates_of_big_guild_tab_in_guild_stash)
            self._left_mouse_click ( )
            self._BIG_GUILD_TAB_IS_OPEN = True


    def _unload_charged_compasses_in_guild_stash (self) -> None:
        unloaded_compass = 1
        self._hold_down_ctrl ( )
        for coordinates_of_charged_compass in self._get_generator_with_coordinates_of_charged_compasses_in_inventory (region_of_charged_compasses_in_inventory):
            pag.moveTo (coordinates_of_charged_compass, duration = self._standart_duration)
            self._left_mouse_click ( )
            unloaded_compass += 1
        self._text_output (f"Переложено {unloaded_compass} заряженных компасов в хранилище гильдии.\n\n")
        self._release_ctrl ( )

    def _get_generator_with_coordinates_of_charged_compasses_in_inventory (self, region: Region) -> Generator:
        return pag.locateAllOnScreen (image = name_of_image_with_unselected_charged_compass_in_inventory,
                                      region = region,
                                      confidence = 0.9)


    def _close_guild_stash (self) -> None:
        self._press_esc ( )


    def _show_end_message (self) -> None:
        self._text_output ("ПРОГРАММА ЗАКОНЧИЛА СВОЮ РАБОТУ,\n")
        self._text_output ("так как закончились ")
        if not self._SEXTANTS_ARE_IN_CURRENCY_TAB:
            self._text_output ("секстанты.\n")
        elif not self._COMPASSES_ARE_IN_CURRENCY_TAB:
            self._text_output ("компасы.\n")    



if __name__ == "__main__":
    search_parameters = {"Затычка": True}
    roller = Roller (search_parameters, lambda num: print (f"Секстантов потрачено: {num}\n"),
                     lambda num: print (f"Компасов потрачено: {num}\n"),
                     lambda text: print ("#Вывод текста#:", text, end="\n\n"))
    roller.run_roll ( )