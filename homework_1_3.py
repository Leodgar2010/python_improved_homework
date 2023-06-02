# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
ATTEMPTS = 10
count = ATTEMPTS
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f"Я загадал число от {LOWER_LIMIT} до {UPPER_LIMIT - 1}. Попробуйте угадать с {count} попыток.")
while count > 0:
    print(f"Попытка №{ATTEMPTS - (count - 1)}")
    a = int(input("Введите число: "))
    if a > num:
        print("меньше")
    elif a < num:
        print("больше")
    else:
        print(f"Вы угадали, это действительно число {num}.")
        quit()
    count = count - 1
print(f"Попытки закончились. Повезёт в следующий раз. Я загадывал число {num}.")
