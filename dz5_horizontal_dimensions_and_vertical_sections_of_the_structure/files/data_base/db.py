"""База данных калькулятора"""


class DataBaseManager:
    @staticmethod
    def save(data):
        print("Сохранено", data)

    @staticmethod
    def fetch():
        return "данные из базы"
