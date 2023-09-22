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

"""Данный код реализует паттерн проектирования "Фабричный метод". 
Вначале определен абстрактный класс Product, который представляет абстрактный продукт. 
У него есть абстрактный метод operation, который должен быть реализован в каждом конкретном продукте.
Затем определены два конкретных продукта: ConcreteProductA и ConcreteProductB. 
Они наследуются от класса Product и реализуют его абстрактный метод operation.
Далее определен абстрактный класс Creator, который представляет абстрактного создателя. 
У него есть абстрактный метод factory_method, который должен быть реализован в каждом конкретном создателе. 
Также у него есть метод some_operation, 
который использует factory_method для создания продукта и выполняет некоторую операцию с этим продуктом.
Затем определены два конкретных создателя: ConcreteCreatorA и ConcreteCreatorB. 
Они наследуются от класса Creator и реализуют его абстрактный метод factory_method. 
Каждый из них создает свой собственный конкретный продукт.

В блоке if __name__ == "__main__" создается объект ConcreteCreatorA и вызывается его метод some_operation, 
который создает объект ConcreteProductA и выполняет операцию с ним. 
Затем создается объект ConcreteCreatorB и вызывается его метод some_operation, 
который создает объект ConcreteProductB и выполняет операцию с ним.
Таким образом, весь код отвечает за создание и использование конкретных продуктов с помощью фабричного метода, 
который определен в абстрактном классе Creator."""