"""Принцип единой ответственности"""


class Animal:
    def __init__(self, name):
        self.name = name


class Flyable:
    def fly(self):
        pass


class Walkable:
    def walk(self):
        pass


class Talking:
    def talk(self):
        pass


class Raven(Animal, Flyable, Walkable, Talking):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} is flying")

    def walk(self):
        print(f"{self.name} is walking")

    def talk(self):
        print(f"{self.name} say is Nevermore")


def main():
    raven = Raven("Lord")
    raven.fly()
    raven.walk()
    raven.talk()


if __name__ == "__main__":
    main()
"""
Этот код демонстрирует принцип SOLID - "Принцип единственной ответственности" (Single Responsibility Principle, SRP). 
Каждый класс имеет только одну ответственность.

- `Animal` - класс, представляющий животное. Он отвечает только за хранение имени животного.
- `Flyable`, `Walkable`, `Swimmable` - интерфейсы, определяющие дополнительные возможности животных. 
    Они содержат только методы, отвечающие за соответствующие действия.
- `Duck` - класс, представляющий утку. Он наследует от класса `Animal` и реализует интерфейсы `Flyable`, `Walkable`, `Swimmable`. 
    Класс `Duck` имеет только одну ответственность - описывать поведение утки.

Этот пример кода является всего лишь одним из множества способов демонстрации принципов SOLID. 
Важно помнить, что SOLID - это не набор жестких правил, а набор принципов, которые помогают разработчикам создавать гибкий и расширяемый код.
"""
