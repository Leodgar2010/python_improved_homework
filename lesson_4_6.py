# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
def my_func(arr, start, stop):
    if stop > len(arr):
        stop = len(arr)
    if start < len(arr):
        start = arr[0]

        # [start+1, stop])
    return sum(arr[(start + 1):(stop - 1)])


arr = [1, 2, 3, 4, 5, 6, 7]
print(my_func(arr, -10, 100))
