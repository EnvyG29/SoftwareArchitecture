"""Принцип инверсии зависимостей"""

from abc import ABC, abstractmethod


# Интерфейс зависимости
class NotificationDependency(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


# Класс, реализующий зависимость от интерфейса
class EmailNotification(NotificationDependency):
    def send_notification(self, message: str):
        print("Sending email notification:", message)


# Класс, требующий зависимость
class UserManagement:
    def __init__(self, notification_dependency: NotificationDependency):
        self.notification_dependency = notification_dependency

    def create_user(self, username: str):
        print("User created:", username)
        self.notification_dependency.send_notification(f"New user created: {username}")


if __name__ == '__main__':
    email_notification = EmailNotification()
    user_management = UserManagement(email_notification)

    user_management.create_user("Mr. Anderson")


"""Таким образом, пример демонстрирует принцип Dependency Inversion Principle (DIP), 
где класс `UserManagement` зависит от абстракции (интерфейса) `NotificationDependency`, а не от конкретной реализации. 
Это позволяет легко заменять различные реализации `NotificationDependency`, такие как `EmailNotification`, 
без изменения кода класса `UserManagement`, и делает классы более гибкими и переиспользуемыми."""