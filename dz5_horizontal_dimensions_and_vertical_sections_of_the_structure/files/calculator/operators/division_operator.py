"""Модуль отвечающий за деления"""


class DivisionOperator:
    def __init__(self, a: 'int|float', b: 'int|float'):
        self.arg1 = a
        self.arg2 = b

    def division_operator(self) -> 'float':
        return self.arg1 / self.arg2
