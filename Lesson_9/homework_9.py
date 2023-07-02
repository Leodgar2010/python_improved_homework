# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения
# с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json
import math
import csv
from random import randint


def csv_gen(a=randint(100, 1000)):
    with open(f"source.csv", 'w') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL, dialect='unix')
        for i in range(a):
            lst = [int(randint(1, 100)) for i in range(3)]
            wr.writerow(lst)


#
def json_deco(func):
    result = {}
    with (open(f"source.csv", 'r', encoding='UTF-8') as f,
          open(f"output.json", 'w', encoding='UTF-8') as f2):
        data = csv.reader(f)
        for i in data:
            if i != None:
                result[",".join(i)] = (func(*(int(j) for j in i)))
        json.dump(result, f2, indent=2)
    return func


def deco_csv_source(func):
    result = {}
    with open(f"source.csv", 'r', encoding='UTF-8') as f:
        data = csv.reader(f)
        for i in data:
            result[",".join(i)] = (func(*(int(j) for j in i)))
        for k, v in result.items():
            print(f"Аргументы: {k} Результат {v}")
    return func


@json_deco
@deco_csv_source
def homework_9(a, b, c):
    if a == 0:
        return None
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        return [(-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a)]
    elif dis == 0:
        return [(-b / (2 * a))]
    else:
        x = (- b / (2 * a))
        return [f"{x}+ i*{sqrt_val}", f"{x}- i*{sqrt_val}"]


if __name__ == "__main__":
    csv_gen()
    homework_9
