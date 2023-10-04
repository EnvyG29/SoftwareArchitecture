"""Модуль отвечающий за вычитание"""


class SubtractOperator:
    def __init__(self, a: 'int|float', b: 'int|float'):
        self.arg1 = a
        self.arg2 = b

    def subtract_operator(self) -> 'int|float':
        return self.arg1 - self.arg2
