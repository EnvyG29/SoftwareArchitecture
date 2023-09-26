"""Принцип подстановки Барбары Лисков"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area


def main():
    rectangle = Rectangle(5, 10)
    circle = Circle(7)

    calculator = AreaCalculator()
    shapes = [rectangle, circle]
    total_area = calculator.calculate_area(shapes)
    print(f"Total area: {total_area}")


if __name__ == "__main__":
    main()

"""В этом примере программа демонстрирует принцип открытости/закрытости (OCP), который гласит, 
что классы должны быть открыты для расширения, но закрыты для модификации. 

- Абстрактный класс `Shape` определяет интерфейс для фигур и содержит абстрактный метод `area()`, 
    который должен быть реализован в каждой конкретной фигуре.
- `Rectangle` и `Circle` - конкретные фигуры, которые наследуются от абстрактного класса `Shape`. 
    Каждая фигура реализует метод `area()` в соответствии с ее уникальными правилами вычисления площади.
- `AreaCalculator` - класс, который использует принцип OCP. Он принимает список фигур и вычисляет общую площадь, 
    не изменяя свой код при добавлении новых типов фигур. Нам не нужно изменять код класса `AreaCalculator`, 
    чтобы он работал с новыми фигурами - мы просто добавляем новую фигуру, реализующую интерфейс `Shape`.

Таким образом, код следует принципу открытости/закрытости (OCP), потому что он открыт для расширения новыми типами фигур, 
но закрыт для изменений в существующих классах при добавлении новых типов фигур."""
