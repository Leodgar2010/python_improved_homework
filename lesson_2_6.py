# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
account_value = 0
money_amount = 0
comission = 0
MIN_COMISSION = 30
MAX_COMISSION = 600
PERCENT = 0.03
tax = 0
percentage = 0
count = 0
while True:
    action = int(input("Выберите действие: пополнить - 1, снять - 2, выйти - 3 "))
    if account_value > 5000000:
        tax = 0.1
    else:
        tax = 0
    print(f"К операции будет применен налог на богатство {tax * 100}%.")
    while True:
        if action == 1:

            money_amount = int(input("Какую сумму кратную 50 вы желате внести? "))
            tax_value = money_amount * tax
            if money_amount % 50 == 0:
                account_value = account_value + money_amount - tax_value
                break
        elif action == 2:
            money_amount = int(input("Какую сумму кратную 50 вы желате снять? "))
            tax_value = money_amount * tax
            if money_amount % 50 == 0:
                if account_value - money_amount - tax_value < 0:
                    print("На счете недостаточно денег")
                    break
                comission = money_amount * 0.015
                if comission < MIN_COMISSION:
                    comission = MIN_COMISSION
                if comission > MAX_COMISSION:
                    comission = MAX_COMISSION
                account_value = account_value - money_amount - comission - tax_value
                print(f"Комиссия за снятие {comission}")
                break
        elif action == 3:
            print("Всего доброго!")
            break
    count += 1
    if count % 3 == 0:
        percentage = account_value * PERCENT
        print(f"Начисленные проценты = {percentage}")
    account_value = account_value + percentage
    print(f"Остаток на счете {account_value}")
    percentage = 0
    flag = (input("Вы закончили работу с банкоматом? 1-да  "))
    if flag == "1":
        break
