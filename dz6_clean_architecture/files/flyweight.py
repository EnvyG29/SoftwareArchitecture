"""Легковес (Flyweight): Легковес используется для оптимизации работы с большим количеством мелких объектов.
Паттерн разделяет общие данные между несколькими объектами, чтобы уменьшить использование памяти.
Это особенно полезно, когда создание и хранение каждого объекта требует значительных ресурсов,
а компактные объекты могут быть повторно использованы."""


# Легковес
class Flyweight:
    def operation(self, extrinsic_state):
        pass


# Конкретный легковес
class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print(f"Выполнение операции с легковесом. Внешнее состояние: {extrinsic_state}")


# Фабрика легковесов
class FlyweightFactory:
    flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteFlyweight()
        return self.flyweights[key]


# Пример использования
factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("key1")
flyweight1.operation("state1")

flyweight2 = factory.get_flyweight("key2")
flyweight2.operation("state2")
