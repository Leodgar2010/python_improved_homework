# Создайте функцию генератор чисел Фибоначчи

def fib(number):
    prevnum, nextnum = 0, 1
    for i in range(number):
        yield prevnum
        prevnum, nextnum = nextnum, prevnum + nextnum


print(*fib(10))
