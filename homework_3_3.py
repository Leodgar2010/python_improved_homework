# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
backpack_volume = 6.5
volume = 0
items = {"спички": 0.01, "палатка": 4.5, "вода": 5, "нож": 0.2, "лопата": 0.5, "котелок": 1}
items_to_go = {}
for i in items:
    if volume + items.get(i) < backpack_volume:
        volume = volume + items.get(i)
        items_to_go[i] = items.get(i)
    else:
        break
print(items_to_go)
