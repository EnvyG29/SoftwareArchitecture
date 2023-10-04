"""Модуль управления"""

from abc import ABC
from .i_view import IView
from .input_output import InputOutput
from ..calculator.calculator import Calculator
from ..data_base.db import DataBaseManager


class ConsoleView(IView, ABC):
    def __init__(self):
        self.calc = Calculator()
        self.i_o = InputOutput()
        self.db = DataBaseManager()

    def run_calculator(self):
        res = self.calc.add(self.i_o.get_in(), self.i_o.get_in())
        self.i_o.display_out(res)

    def memory(self):
        self.db.save(data)
        self.db.fetch()

