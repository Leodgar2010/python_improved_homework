# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

# словарь с кортежами в качестве значений
camping = {"Вася": ("cпички", "дрова", "котелок"),
           "Петя": ("дрова", "хлеб", "cпички"),
           "Миша": ("cпички", "удочка", "хлеб")}
friend_count = len(camping)
all_friend_item = set()
uniq_items = set()
all_without_one = set()
# преобразование кортежей в множества
for i in camping:
    temp = set()
    for k in camping.get(i):
        temp.add(k)
    camping[i] = temp
print(camping)
# поиск уникальных вещей у всего отряда
for i in camping:
    all_friend_item = camping.get(i).union(all_friend_item)
print(f"Все {friend_count} взяли: {all_friend_item}")
# поиск уникальных вещей у каждого из друзей
for i in camping:
    uniq_item = camping.get(i)
    for k in camping:
        if camping.get(k) != camping.get(i):
            uniq_item = uniq_item.difference(camping.get(k))
    if len(uniq_item) > 0:
        print(f"{i} взял с собой уникальную вещь {uniq_item}")
    else:
        print(f'{i} не взял с собой ничего уникального')
# поиск вещей которые есть у всех кроме одного друга
for i in camping:
    all_other_camping = {}
    all_without_one = set()
    for k in camping:
        if camping.get(i) != camping.get(k):
            all_other_camping[k] = camping.get(k)
    for j in all_other_camping:
        all_without_one = all_other_camping.get(j)
        for f in all_other_camping:
            if all_other_camping.get(f) != all_without_one:
                all_without_one = all_without_one.intersection(all_other_camping.get(f))
    result = all_without_one.difference(camping.get(i))
    if len(result) > 0:
        print(f"{i} не взял с собой {result}")
    else:
        print(f'{i} взял с собой тоже что и кто-то из остальных')
