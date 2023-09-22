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