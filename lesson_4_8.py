# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце

sizes = 10
weights = 15
name = 'Иван'
surnames = "Петров"


def my_func():
    dic = {}
    for i in globals():
        if i[-1] == "s":
            dic[i[:-1]] = globals().get(i)
            globals()[i] = None
    for i in dic:
        globals()[i] = dic.get(i)


my_func()

print(globals())
