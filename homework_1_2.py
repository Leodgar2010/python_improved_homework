# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
import sys

LOWER_LIMIT = 0
MAX_LIMIT = 100000
a= ""
while True:
    number = int(input(f"Введите целое число больше {LOWER_LIMIT}  и меньше {MAX_LIMIT}: "))
    if number == 0:
        a = "не"
        break
    elif LOWER_LIMIT < number < MAX_LIMIT+1:
        break
    else: print("Вы ввели число за передлами дапазона.")

divider = number - 1;
while divider > 1:
    if number % divider == 0:
        a= "не "
        break
    divider -= 1
print(f"Число {a}являтся простым.")
