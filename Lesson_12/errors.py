class UserException(Exception):
    pass
class FoolCheckError (UserException):
    def __init__(self, name, value, start, stop):
        self.name = name
        self.value = value
        self.start = start
        self.stop = stop
    def __str__(self):
        return f"Значение {self.name} должно быть в заданном диапазоне " \
               f"от {self.start} до {self.stop} . Вы ввели {self.value}."

