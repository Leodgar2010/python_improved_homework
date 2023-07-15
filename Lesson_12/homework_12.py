# Создайте класс студента. Используя дескрипторы проверяйте ФИО
# на первую заглавную букву и наличие только букв. Названия предметов
# должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре
# недопустимы. Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100). Также экземпляр должен сообщать средний балл
# по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
from errors import FoolCheckError

ESTIMATE_MIN, ESTIMATE_MAX = 2, 5
TEST_MIN, TEST_MAX = 0, 100


class NameCheck:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):

        if not value.isalpha():
            raise TypeError(f'Значение {value} должно состоять только из букв')
        if not value.istitle():
            raise ValueError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    first_name = NameCheck()
    last_name = NameCheck()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.lesson = Student.lesson_load(self)

    def lesson_load(self):
        with open(f'subject.csv', 'r', encoding="utf-8") as f:
            result = {}
            for i in csv.reader(f):
                result[i[0]] = {'estimate': [], 'test_result': [], 'middle_test': int()}
            return result

    def add_estimate(self, lesson, estimate):
        if ESTIMATE_MIN <= estimate <= ESTIMATE_MAX:
            self.lesson[lesson]['estimate'].append(estimate)
        else:
            raise FoolCheckError('Оценка', estimate, ESTIMATE_MIN, ESTIMATE_MAX)

    def add_test(self, lesson, test):
        a = self.lesson[lesson]['test_result']
        if TEST_MIN <= test <= TEST_MAX:
            a.append(test)
            self.lesson[lesson]['middle_test'] = (sum(a)) / len(a)
        else:
            raise FoolCheckError('Результат теста', test, TEST_MIN, TEST_MAX)

    def middle_estimate(self):
        result = 0
        for i in self.lesson.keys():
            result += sum(self.lesson.get(i).get('estimate'))
        return result

    def create_report(self):
        with open(f'{self.last_name}.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow([i for i in self.lesson.keys()])
            writer.writerow([self.lesson.get(i).get('estimate') for i in self.lesson.keys()])
            writer.writerow([self.lesson.get(i).get('test_result') for i in self.lesson.keys()])

    def __repr__(self):

        return f'Student(first_name={self.first_name}, last_name={self.last_name}, subject ={self.lesson},' \
               f' middle_estimate = {self.middle_estimate()})'


if __name__ == '__main__':
    s1 = Student("Вacя", "Пупкин")
    s1.add_estimate("Математика", 5)
    s1.add_estimate("Физика", 4)
    s1.add_test('Математика', 100)
    s1.add_test('Математика', 50)
    s1.add_test('Физика', 34)
    s1.add_test('Физика', 70)
