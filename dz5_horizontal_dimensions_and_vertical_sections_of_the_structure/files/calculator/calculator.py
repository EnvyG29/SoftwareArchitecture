from .operators import sum_operator as sum_o
from .operators import subtract_operator as sub_o
from .operators import multiplication_operator as multi_o
from .operators import division_operator as div_o


class Calculator:
    @staticmethod
    def add(a: 'int|float', b: 'int|float') -> 'int|float':
        res = sum_o.SumOperator(a, b)
        return res.sum_operator()

    @staticmethod
    def subtract(a: 'int|float', b: 'int|float') -> 'int|float':
        res = sub_o.SubtractOperator(a, b)
        return res.subtract_operator()

    @staticmethod
    def multiplication(a: 'int|float', b: 'int|float') -> 'int|float':
        res = multi_o.MultiplicationOperator(a, b)
        return res.multiplication_operator()

    @staticmethod
    def division(a: 'int|float', b: 'int|float') -> 'int|float':
        res = div_o.DivisionOperator(a, b)
        return res.division_operator()
