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

def result (func):
    with open(f"{func.__name__}.csv", 'r', encoding='UTF-8') as f:
        for i in csv.reader(f):
            a, b, c, = i
            yield f"{i}",func(int(a), int(b), int(c))

def csv_gen(func, a=randint(100,1000)):
    with open(f"{func.__name__}.csv", 'w') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL, dialect='unix')
        for i in range(a):
            lst = [int(randint(1, 100)) for i in range(3)]
            wr.writerow(lst)

def json_deco(func):
    dic ={}
    csv_gen(func)
    for i in result(func):
        dic[i[0]]=i[1]
    with open(f"{func.__name__}.json", 'w', encoding='UTF-8') as f2:
        json.dump(dic, f2, indent=1)


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

    json_deco(homework_9)