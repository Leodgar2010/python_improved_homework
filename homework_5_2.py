# Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str с
# указанием процентов вида “10.25%”. В результате получаем словарь с
# именем в качестве ключа и суммой премии в качестве значения. Сумма
# рассчитывается как ставка умноженная на процент премии

x= zip (["Петя", "Вася", "Миша"], [10000, 15000, 20000], ["7.15%", '4.8%', '10.25%'])
dic = {i: (j*float(k.strip('%'))/100) for i,j,k in x}
print (dic)