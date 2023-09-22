from copy import deepcopy

"""Библиотека `copy` в Python предоставляет функциональность для создания глубоких копий (deep copy) объектов. 
Глубокая копия означает создание нового объекта, который является полностью независимым от исходного объекта, 
включая все его вложенные объекты."""


# Прототип
class Prototype:
    # Создать копию объекта
    def clone(self):
        pass


# Конкретный прототип 1
class ConcretePrototype1(Prototype):
    def __init__(self, name: str):
        self.name = name

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"ConcretePrototype1: {self.name}"


# Конкретный прототип 2
class ConcretePrototype2(Prototype):
    def __init__(self, number: int):
        self.number = number

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"ConcretePrototype2: {self.number}"


if __name__ == "__main__":
    prototype1 = ConcretePrototype1("Prototype 1")
    clone1 = prototype1.clone()
    print(clone1)

    prototype2 = ConcretePrototype2(123)
    clone2 = prototype2.clone()
    print(clone2)

"""Этот код демонстрирует паттерн Прототип. 
В коде определен абстрактный класс Prototype, который имеет метод clone(). 
Этот метод должен быть реализован в каждом конкретном прототипе.
Затем определены два конкретных прототипа: ConcretePrototype1 и ConcretePrototype2. 
Оба класса наследуют абстрактный класс Prototype и реализуют метод clone(). 
ConcretePrototype1 имеет атрибут name, а ConcretePrototype2 - атрибут number.

В блоке кода, который начинается с "if name == 'main':", 
создаются экземпляры конкретных прототипов и вызывается метод clone() для создания их копий. 
Затем выводятся результаты клонирования.
Если выполнить этот код, он создаст экземпляры ConcretePrototype1 и ConcretePrototype2, 
а затем создаст их копии с помощью метода clone(). Результаты клонирования выводятся на экран."""
