"""Интерфейс модуля управления пользователем"""
from abc import ABC, abstractmethod


class IView(ABC):
    @abstractmethod
    def run_calculator(self):
        pass

    @abstractmethod
    def memory(self):
        pass
