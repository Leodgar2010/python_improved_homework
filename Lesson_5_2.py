# Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

text = "Мой дядя самых честных правил когда не в шутку занемог"
dic= ({i: ord(i) for i in set(text)})