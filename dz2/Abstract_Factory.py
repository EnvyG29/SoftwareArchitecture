from abc import ABC, abstractmethod


# Абстрактный класс продукта A
class AbstractProductA(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Абстрактный класс продукта B
class AbstractProductB(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Конкретный продукт A1
class ConcreteProductA1(AbstractProductA):
    def operation(self) -> str:
        return "ConcreteProductA1"


# Конкретный продукт A2
class ConcreteProductA2(AbstractProductA):
    def operation(self) -> str:
        return "ConcreteProductA2"


# Конкретный продукт B1
class ConcreteProductB1(AbstractProductB):
    def operation(self) -> str:
        return "ConcreteProductB1"


# Конкретный продукт B2
class ConcreteProductB2(AbstractProductB):
    def operation(self) -> str:
        return "ConcreteProductB2"


# Абстрактная фабрика
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


# Конкретная фабрика 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


# Конкретная фабрика 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


if __name__ == "__main__":
    factory = ConcreteFactory1()
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_a.operation())
    print(product_b.operation())

    factory = ConcreteFactory2()
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_a.operation())
    print(product_b.operation())

"""Данный код реализует паттерн "Абстрактная фабрика". 
В коде определены абстрактные классы `AbstractProductA` и `AbstractProductB`, 
которые представляют абстрактные продукты A и B соответственно. 
У каждого из этих классов есть абстрактный метод `operation`, 
который должен быть реализован в конкретных продуктах.
Затем определены конкретные классы `ConcreteProductA1`, `ConcreteProductA2`, 
`ConcreteProductB1` и `ConcreteProductB2`, 
которые наследуются от абстрактных классов и реализуют их методы `operation`. 
Каждый из этих классов представляет конкретный продукт.
Далее определен абстрактный класс `AbstractFactory`, который представляет абстрактную фабрику. 
У этого класса есть два абстрактных метода `create_product_a` и `create_product_b`, 
которые должны быть реализованы в конкретных фабриках.
Затем определены конкретные классы `ConcreteFactory1` и `ConcreteFactory2`, 
которые наследуются от абстрактного класса `AbstractFactory` и реализуют его методы 
`create_product_a` и `create_product_b`. 
Каждый из этих классов представляет конкретную фабрику, 
которая создает свои конкретные продукты.

В блоке кода `if __name__ == "__main__":` 
создается объект класса `ConcreteFactory1` и вызываются его методы `create_product_a` 
и `create_product_b`, чтобы получить конкретные продукты A1 и B1. 
Затем создается объект класса `ConcreteFactory2` и вызываются его методы `create_product_a` 
и `create_product_b`, чтобы получить конкретные продукты A2 и B2. 
Результаты операций продуктов выводятся на экран."""