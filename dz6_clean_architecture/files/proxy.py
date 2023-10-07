"""Прокси (Proxy): Прокси используется, когда требуется контролировать или добавить дополнительные функции к доступу к объекту без изменения его кода.
Например, прокси может использоваться для проверки прав доступа пользователя, кеширования данных или отложенной загрузки.
Прокси предоставляет такой же интерфейс, как и оригинальный объект, что делает его незаметным для клиента."""


# Общий интерфейс
class Subject:
    def request(self):
        pass


# Реальный объект
class RealSubject(Subject):
    def request(self):
        print("Выполнение реального запроса")


# Прокси объект
class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        # Ленивая инициализация реального объекта
        if self.real_subject is None:
            self.real_subject = RealSubject()
        self.real_subject.request()


# Пример использования
proxy = Proxy(None)
proxy.request()
