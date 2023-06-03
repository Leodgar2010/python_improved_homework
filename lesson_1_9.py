# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# a = 2
# b = 2
# while a < 10:
#     print(a, "x", b, "=", a * b)
#     if b > 9:
#         a = a + 1
#         b = 1
#     b += 1
table_shape = [[2, 3, 4, 5], [6, 7, 8, 9]]
FIRST_NUMBER = 2
LAST_NUMBER = 10
print ("\t\t\t\tТ А Б Л И Ц А\tУ М Н О Ж Е Н И Я")
for a in table_shape:
    if a != 0:
        print('')
    for b in range(FIRST_NUMBER, LAST_NUMBER + 1):
        for k in range(0, len(table_shape[0])):
            print(f"{a[k]} X {b} = {a[k] * b}\t\t", end="")
        print('')
