"""Принцип разделения интерфейсов"""

from abc import ABC, abstractmethod


# Интерфейс, описывающий функциональность для работы с электронными устройствами
class IElectronicDevice(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass


# Класс, реализующий функциональность электронных устройств
class ElectronicDevice(IElectronicDevice):
    def power_on(self):
        print("Powering on the electronic device.")

    def power_off(self):
        print("Powering off the electronic device.")


# Интерфейс, описывающий функциональность для работы с аудиоустройствами
class IAudioDevice(ABC):
    @abstractmethod
    def play_sound(self):
        pass

    @abstractmethod
    def stop_sound(self):
        pass


# Класс, реализующий функциональность аудиоустройств
class AudioDevice(IAudioDevice):
    def play_sound(self):
        print("Playing sound.")

    def stop_sound(self):
        print("Stopping sound.")


# Класс, который объединяет обе функциональности
class AllInOneDevice(IElectronicDevice, IAudioDevice):
    def power_on(self):
        print("Powering on the all-in-one device.")

    def power_off(self):
        print("Powering off the all-in-one device.")

    def play_sound(self):
        print("Playing sound on the all-in-one device.")

    def stop_sound(self):
        print("Stopping sound on the all-in-one device.")


if __name__ == '__main__':
    electronic_device = ElectronicDevice()
    audio_device = AudioDevice()
    all_in_one_device = AllInOneDevice()

    electronic_device.power_on()
    electronic_device.power_off()

    audio_device.play_sound()
    audio_device.stop_sound()

    all_in_one_device.power_on()
    all_in_one_device.power_off()
    all_in_one_device.play_sound()
    all_in_one_device.stop_sound()


"""В этом примере определяются интерфейсы `IElectronicDevice` и `IAudioDevice`, 
описывающие функциональности для работы с электронными устройствами и аудиоустройствами соответственно. 
Затем классы `ElectronicDevice` и `AudioDevice` реализуют эти интерфейсы. 
Класс `AllInOneDevice` объединяет обе функциональности, реализуя оба интерфейса.

Таким образом, код демонстрирует основные принципы Interface Segregation Principle (ISP),
где интерфейсы предоставляют наборы методов, относящихся только к определенным функциональностям, 
а классы реализуют только необходимые интерфейсы в зависимости от своих требований."""
