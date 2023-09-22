# Продукт
class Product:
    def __init__(self):
        self.parts = []

    # Добавить часть в продукт
    def add_part(self, part: str):
        self.parts.append(part)

    # Вывести список частей продукта
    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}")


# Абстрактный строитель
class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    # Получить готовый продукт
    def get_result(self) -> Product:
        pass


# Конкретный строитель 1
class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A1")

    def build_part_b(self):
        self.product.add_part("Part B1")

    def build_part_c(self):
        self.product.add_part("Part C1")

    def get_result(self) -> Product:
        return self.product


# Конкретный строитель 2
class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A2")

    def build_part_b(self):
        self.product.add_part("Part B2")

    def build_part_c(self):
        self.product.add_part("Part C2")

    def get_result(self) -> Product:
        return self.product


# Директор
class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    # Строить продукт пошагово
    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


if __name__ == "__main__":
    builder1 = ConcreteBuilder1()
    director1 = Director(builder1)
    director1.construct()
    product1 = builder1.get_result()
    product1.list_parts()

    builder2 = ConcreteBuilder2()
    director2 = Director(builder2)
    director2.construct()
    product2 = builder2.get_result()
    product2.list_parts()

"""Данный код реализует паттерн проектирования Строитель (Builder). 
В начале определен класс "Product", который представляет продукт, который мы строим. 
Он имеет методы для добавления частей в продукт и вывода списка частей.
Затем определен абстрактный класс "Builder", который представляет абстрактного строителя. 
В нем определены методы для построения различных частей продукта и получения готового продукта.
Далее определены два конкретных класса строителей: "ConcreteBuilder1" и "ConcreteBuilder2".
Каждый из них наследует абстрактный класс "Builder" и реализует его методы построения частей продукта.
У каждого строителя есть свой экземпляр класса "Product", с которым он работает.
Затем определен класс "Director", который представляет директора, который управляет строителем и определяет последовательность шагов построения продукта. 
У него есть метод "construct", который вызывает методы строителя для построения различных частей продукта.

В блоке "main" создаются два экземпляра конкретных строителей и директоров, и вызываются соответствующие методы для построения продуктов. 
Затем вызывается метод "list_parts" для вывода списков частей каждого продукта.
Таким образом, данный код позволяет создавать продукты различной структуры, используя разные строители и директоров. 
Это позволяет отделить процесс построения продукта от его представления, 
что упрощает добавление новых типов продуктов и изменение процесса их построения."""
