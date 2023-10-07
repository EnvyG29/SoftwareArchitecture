"""Фасад (Facade): Фасад используется для предоставления унифицированного интерфейса к группе интерфейсов подсистемы.
Фасад обеспечивает простоту работы со сложной системой, скрывая сложную логику и детали реализации подсистемы.
Это позволяет клиентскому коду использовать систему более удобным и понятным способом."""


# Подсистема 1
class Subsystem1:
    def operation1(self):
        print("Выполнение операции 1 подсистемы 1")

    def operation2(self):
        print("Выполнение операции 2 подсистемы 1")


# Подсистема 2
class Subsystem2:
    def operation1(self):
        print("Выполнение операции 1 подсистемы 2")

    def operation2(self):
        print("Выполнение операции 2 подсистемы 2")


# Фасад
class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        self.subsystem1.operation1()
        self.subsystem1.operation2()
        self.subsystem2.operation1()
        self.subsystem2.operation2()


# Пример использования
facade = Facade()
facade.operation()
