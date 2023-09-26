"""Принцип открытости/закрытости """

from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        return f"{self.name} started. Ready to go!"

    def stop(self):
        return f"{self.name} stopped. Parked safely."


class Moto(Vehicle):
    def start(self):
        return f"{self.name} started. Wheelie!"

    def stop(self):
        return f"{self.name} stopped. Stoppie."


def race(vehicle):
    print(vehicle.start())
    print(vehicle.stop())


car = Car("BMW", 200)
moto = Moto("Honda", 250)


race(car)
race(moto)

"""В этом примере есть абстрактный базовый класс `Vehicle`, который определяет общие методы `start` и `stop`. 
Затем мы создаем два подкласса `Car` и `Bicycle`, которые наследуются от `Vehicle` и реализуют свою собственную логику для методов `start` и `stop`.

Функция `race` принимает объект `Vehicle` в качестве аргумента и вызывает его методы `start` и `stop`. 
Благодаря LSP, мы можем передавать любые подклассы `Vehicle` в `race`, так как они гарантированно предоставляют те же самые методы.

Таким образом, код демонстрирует принцип подстановки Барбары Лисков (LSP), который говорит о том, 
что подклассы должны быть взаимозаменяемыми с базовым классом, не нарушая ожидаемую функциональность."""
