a = int(input("Введите количество рядов: "))
for i in range(1, a + 1): print(" " * (a - i), "*" * (i + i - 1))
