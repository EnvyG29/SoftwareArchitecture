class Singleton:
    _instance = None

    # Получить экземпляр класса
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 is singleton2)

"""Класс Singleton реализует паттерн проектирования Singleton, 
который гарантирует, что у класса есть только один экземпляр, 
и предоставляет глобальную точку доступа к этому экземпляру.
В данной реализации используется статическая переменная _instance, 
которая хранит созданный экземпляр класса.
Метод new проверяет, если экземпляр класса еще не создан (переменная _instance равна None), 
то создает его с использованием метода new у родительского класса. Если экземпляр уже существует,
 то метод просто возвращает его.
 
Далее, в блоке кода, который выполняется только если скрипт запущен напрямую (if name == "main"),
создаются два экземпляра класса Singleton и сохраняются в переменные singleton1 и singleton2. 
Затем происходит сравнение singleton1 и singleton2 по оператору "is", и результат выводится на экран. 
Если результат True, то это означает, что обе переменные ссылаются на один и тот же экземпляр класса,
и класс Singleton работает правильно."""
