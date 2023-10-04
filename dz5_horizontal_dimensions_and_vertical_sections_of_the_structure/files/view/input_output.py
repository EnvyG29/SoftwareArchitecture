"""Модуль управления вводом и выводом данных"""

from .in_out_operators.input_operator import InputSlice
from .in_out_operators.output_operator import OutputSlice


class InputOutput:
    @staticmethod
    def get_in():
        get = InputSlice.get_input()
        return get

    @staticmethod
    def display_out(res="None"):
        OutputSlice.get_output(res)
