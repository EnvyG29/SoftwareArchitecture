"""Мост (Bridge): Мост используется, когда нужно разделить абстракцию от ее реализации,
чтобы они могли изменяться независимо друг от друга. Это особенно полезно, когда существует несколько способов расширять функциональность классов и
эти изменения не должны влиять на другие классы. Мост позволяет связать эти различные реализации, чтобы клиентский код мог работать с абстракцией,
не завися от конкретной реализации."""


# Абстракция
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        self.implementation.do_operation()


# Реализация
class Implementation:
    def do_operation(self):
        pass


# Конкретная реализация
class ConcreteImplementationA(Implementation):
    def do_operation(self):
        print("Выполнение операции с использованием реализации A")


class ConcreteImplementationB(Implementation):
    def do_operation(self):
        print("Выполнение операции с использованием реализации B")


# Пример использования
implementation_a = ConcreteImplementationA()
implementation_b = ConcreteImplementationB()
abstraction = Abstraction(implementation_a)
abstraction.operation()
abstraction.implementation = implementation_b
abstraction.operation()
