from typing import Any

from abc import ABC, abstractmethod


class Error (Exception):
    def __init__ (self, text: str = '', class_name: str = ''):
        if text:
            self.error_text = str (text)
        else:
            self.error_text = self._show_fallback_error_text ( )

        self._class_name = class_name

    def _show_fallback_error_text (self) -> str:
        return "Произошла ошибка!"

    def __str__ (self) -> str:
        return self.error_text


class MovementPatternRedefinitionError (Error):
    def _show_fallback_error_text (self) -> str:
        return "\nМетод _initializing_start_values класса\n{self.class_name} ДОЛЖЕН быть переопределён!"



class ArgumentError (Exception):
    def __init__ (self, argument: Any,
                  argument_name: str,
                  name_of_method_or_function: str,
                  class_name: str = ""):
        self.argument = argument
        self.argument_name = argument_name
        self.name_of_method_or_function = name_of_method_or_function
        self.class_name = class_name

        self._create_error_text ( )

    def _create_error_text (self) -> None:
        if self.class_name:
            self.error_text = self._show_error_text_with_class_name ( )
        else:
            self.error_text = self._show_error_text_without_class_name ( )

    def _show_error_text_with_class_name (self) -> str:
        return f"В аргументе {self.argument_name}, метода {self.name_of_method_or_function} класса {self.class_name}, есть ошибка!\n{self.argument_name} is {self._argument_type}."

    def _show_error_text_without_class_name (self) -> str:
        return f"В аргументе {self.argument_name}, функции {self.name_of_method_or_function}, есть ошибка!\n{self.argument_name} is {self._argument_type}."

    @property
    def _argument_type (self) -> str:
        return str (type (self.argument).__name__)

    def __str__ (self) -> str:
        return self.error_text


class IntArgumentError (ArgumentError):
    def _show_error_text_with_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, метода {self.name_of_method_or_function} класса {self.class_name}, ДОЛЖЕН быть целочисленным, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not int!"

    def _show_error_text_without_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, функции {self.name_of_method_or_function}, ДОЛЖЕН быть целочисленным, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not int!"


class IntOrFloatArgumentError (ArgumentError):
    def _show_error_text_with_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, метода {self.name_of_method_or_function} класса {self.class_name}, ДОЛЖЕН быть целочисленным или дробным, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not int or float!"

    def _show_error_text_without_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, функции {self.name_of_method_or_function}, ДОЛЖЕН быть целочисленным или дробным, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not int or float!"


class StrArgumentError (ArgumentError):
    def _show_error_text_with_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, метода {self.name_of_method_or_function} класса {self.class_name}, ДОЛЖЕН быть строкой, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not str!"

    def _show_error_text_without_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, функции {self.name_of_method_or_function}, ДОЛЖЕН быть строкой, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not str!"


class TkArgumentError (ArgumentError):
    def _show_error_text_with_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, метода {self.name_of_method_or_function} класса {self.class_name}, ДОЛЖЕН быть Tk, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not Tk!"

    def _show_error_text_without_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, функции {self.name_of_method_or_function}, ДОЛЖЕН быть Tk, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not Tk!"


class PointArgumentError (ArgumentError):
    def _show_error_text_with_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, метода {self.name_of_method_or_function} класса {self.class_name}, ДОЛЖЕН быть Point, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not Point!"

    def _show_error_text_without_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, функции {self.name_of_method_or_function}, ДОЛЖЕН быть Point, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not Point!"


class RegionArgumentError (ArgumentError):
    def _show_error_text_with_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, метода {self.name_of_method_or_function} класса {self.class_name}, ДОЛЖЕН быть Region, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not Region!"

    def _show_error_text_without_class_name (self) -> str:
        return f"Аргумент {self.argument_name}, функции {self.name_of_method_or_function}, ДОЛЖЕН быть Region, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not Region!"



class ClassConstructorArgumentError (Exception, ABC):
    def __init__ (self, argument: Any,
                   argument_name: str,
                      class_name: str):
        self.argument = argument
        self.argument_name = argument_name
        self.class_name = class_name

        self.error_text = self._create_error_text ( )

    @abstractmethod
    def _create_error_text (self) -> str:
        """Функция для создания текста ошибки внутри класса"""

    @property
    def _argument_type (self) -> str:
        return str (type (self.argument).__name__)

    def __str__ (self) -> str:
        return self.error_text


class TkOrFrameOrLabelFrameArgumentInInitError (ClassConstructorArgumentError):
    def _create_error_text (self) -> str:
        return f"Аргумент {self.argument_name}, констуктора класса {self.class_name}, ДОЛЖЕН быть экземпляром класса Tk, Frame или LabelFrame, а не {self._argument_type}!\n{self.argument_name} is {self._argument_type} but not Tk, Frame or LabelFrame!"



class SomethingNotFound (Exception):
    def __init__ (self):
        pass


class TabNotFound (SomethingNotFound):
    def __str__ (self) -> str:
        return "Не найдена вкладка тайника/хранилища гильдии!\n"


class SextantsInCurrencyTabNotFound (SomethingNotFound):
    def __str__ (self) -> str:
        return "Нет секстантов в валютной вкладке!\n\n"


class SextantsInInventoryNotFound (SomethingNotFound):
    def __str__ (self) -> str:
        return "Нет секстантов в инвентаре!\n\n"


class CompassesInCurrencyTabNotFound (SomethingNotFound):
    def __str__ (self) -> str:
        return "Нет компасов в валютной вкладке!\n\n"


class PoeNotFound (SomethingNotFound):
    def __str__ (self) -> str:
        return "Не найдена иконка ПоЕ на панели задач!\nВозможно, оно не включено.\n\n"
