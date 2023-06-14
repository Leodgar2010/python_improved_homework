# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список


def options():
    return int(input("Выберите действие: пополнить - 1, снять - 2, выйти - 3 "))


def tax(account_value):
    if account_value >= 5000000:
        return 0.1
    else:
        return 0


def income(account_value, tax, arr):
    money_amount = int(input("Какую сумму кратную 50 вы желате внести? "))
    if money_amount % 50 == 0:
        account_value = account_value + money_amount - tax * money_amount
        arr.append(money_amount)
    return account_value


def outcome(account_value, COMISSION, tax, arr):
    money_amount = int(input("Какую сумму кратную 50 вы желате снять? "))
    if money_amount % 50 == 0:
        if account_value - money_amount - tax < 0:
            print("На счете недостаточно денег")
            return account_value
        comission = money_amount * COMISSION
        if comission < MIN_COMISSION:
            comission = MIN_COMISSION
        if comission > MAX_COMISSION:
            comission = MAX_COMISSION
        account_value = account_value - money_amount - comission - tax * money_amount
        arr.append(money_amount)
        print(f"Комиссия за снятие {comission}")
        return account_value


account_value = 0
money_amount = 0
COMISSION = 0.015
comission = 0
MIN_COMISSION = 30
MAX_COMISSION = 600
PERCENT = 0.03
percentage = 0
count = 0
arr = []
while True:
    action = options()
    tax_value = tax(account_value)
    print(f"К операции будет применен налог на богатство {tax_value * 100}%.")
    while True:
        if action == 1:
            account_value = income(account_value, tax_value, arr)
            break
        elif action == 2:
            account_value = outcome(account_value, COMISSION, tax_value, arr)
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
print(arr)
