from copy import deepcopy


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