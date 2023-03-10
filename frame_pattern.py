from tkinter import Tk, Frame, LabelFrame

from abc import ABC, abstractmethod

from program_exceptions import TkOrFrameOrLabelFrameArgumentInInitError


class FramePattern (ABC):
    def __init__ (self, root_window: Tk | Frame | LabelFrame):
        self._ROOT_WINDOW = root_window
        self._check_root_window ( )

    def _check_root_window (self) -> None:
        if not isinstance (self._ROOT_WINDOW, (Tk, Frame, LabelFrame)):
            raise TkOrFrameOrLabelFrameArgumentInInitError (self._ROOT_WINDOW,
                                                            "root_window",
                                                            __class__.__name__)

    @abstractmethod
    def run ( ) -> None:
        """Функция для создания/запуска рамки"""
