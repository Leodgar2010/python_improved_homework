# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.
text = (input("Наберите любой текст: "))
# строка для теста
# text = "мой дядя самых честных правил когда не в шутку занемог"
dic_without_count = {}
for i in range(0, len(text)):
    if text[i] != " " and (text[i] not in dic_without_count.keys()):
        dic_without_count[text[i]] = 1
    elif (text[i] in dic_without_count.keys()):
        dic_without_count[text[i]] += 1
dic_with_count = {}
for i in range(0, len(text)):
    dic_with_count.setdefault(text[i], text.count(text[i]))
print(dic_without_count)
print(dic_with_count)
