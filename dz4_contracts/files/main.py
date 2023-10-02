from abc import ABC, abstractmethod
from colorama import Fore
from contracts import contract


class Vehicle(ABC):
    """Интерфейс Vehicle(Транспортное средство) обладает минимальным набором методами,
    которые необходимо реализовать в наследующих классах"""
    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def min_fuel_level_sensor(self):
        raise NotImplementedError

    @abstractmethod
    def sensor_reading(self, km: float):
        raise NotImplementedError

    @abstractmethod
    def check_petrol(self, current_liters: float):
        raise NotImplementedError


def emergency_stop(func):
    """Функция используется как контрактная.
    Если параметр принимаемой функции не будет соответствовать условию value > 0,
    работа программы прервется с ошибкой 'Аварийная остановка. В системе нет топлива'.
    """
    def f(self, value: float):
        assert value > 0, "Аварийная остановка. В системе нет топлива"
        return func(self, value)
    return f


class Car(Vehicle):
    """Класс Car(автомобиль) наследует все обязательные методы Vehicle"""

    @contract
    def __init__(self, type_car: str, tank: 'int, >5', current_fuel_level: 'float|int, >=0', fuel_consumption: 'float|int, >0.1'):
        """Метод инициализации. Имеет декоратор метода contract из библиотеки contracts.
        При невалидном вводе данных при создании класса, программа прекратит работу с ошибкой.
        Значение tank(топливный бак) не может быть меньше 5.
        Если значение current_fuel_level(текущий уровень топлива) будет превышать значение tank,
        значение current_fuel_level будет приравнено значению tank."""

        self.type_car = type_car
        self.tank = tank
        if current_fuel_level > tank:
            self.current_fuel_level = tank
        else:
            self.current_fuel_level = current_fuel_level
        self.fuel_consumption = fuel_consumption
        self.engine_ON: bool = False

    def start(self):
        """Метод запуска двигателя"""
        self.engine_ON = True
        print("Двигатель запущен.")

    def stop(self):
        """Метод выключения зажигания"""
        self.engine_ON = False
        print("Двигатель остановлен.")

    def min_fuel_level_sensor(self):
        """Метод контроля уровня топлива и выводящий сообщение о переходе на резервный запас."""
        if self.current_fuel_level < self.tank * 0.15:
            print(f"{Fore.YELLOW}Низкий уровень топлива{Fore.RESET}")

    def sensor_reading(self, km: float):
        """Метод выводящий показания датчиков"""
        print(f"{km}км проехал, {self.current_fuel_level:.2f} литров топлива осталось")

    @emergency_stop
    def check_petrol(self, current_liters: float):
        """Метод контроля уровня топлива.
        Имеется декоратор с контрактной функцией."""
        pass


class Driving:
    """Класс вождения"""
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def start_vehicle(self):
        self.vehicle.start()

    def __drive(self, km: int):
        """Метод вождения транспортным средством.
        Каждые 10 километров будут выводиться данные с датчиков и сообщения о неисправностях"""
        for i in range(1, km + 1):
            self.vehicle.current_fuel_level -= self.vehicle.fuel_consumption * 0.01
            if i % 10 == 0 or i == km:
                self.vehicle.min_fuel_level_sensor()
                self.vehicle.sensor_reading(i)
            c_f_l = self.vehicle.current_fuel_level
            self.vehicle.check_petrol(c_f_l)

    def driving(self, km: int):
        """Метод проверки работы мотора перед движением транспорта"""
        if self.vehicle.engine_ON:
            self.__drive(km)
        else:
            print("Двигатель не запущен")

    def stop_vehicle(self):
        self.vehicle.stop()


def main():
    # Пример использования программы
    car = Car("Truck", 1000, 700, 35)   # Создан грузовик
    driving = Driving(car)   # Создан модуль управления
    driving.start_vehicle()   # Запуск двигателя
    driving.driving(1950)   # Отправлен в рейс
    driving.stop_vehicle()   # выключение зажигания
    driving.driving(50)   # Попытка поехать с выключенным зажиганием


if __name__ == '__main__':
    main()
