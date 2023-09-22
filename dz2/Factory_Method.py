from abc import ABC, abstractmethod


# Абстрактный класс продукта
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Конкретный продукт A
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "ConcreteProductA"


# Конкретный продукт B
class ConcreteProductB(Product):
    def operation(self) -> str:
        return "ConcreteProductB"


# Абстрактный класс создателя
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


# Конкретный создатель A
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


# Конкретный создатель B
class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


if __name__ == "__main__":
    creator = ConcreteCreatorA()
    print(creator.some_operation())

    creator = ConcreteCreatorB()
    print(creator.some_operation())