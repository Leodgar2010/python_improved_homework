# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.
text = (input("Наберите любой текст: "))
# строка для теста
# text = "мой дядя самых честных правил когда не в шутку занемог"
arr = text.split(" ")
# поиск самого длинного слова
length_of_the_most_longest_word = 0
for i in arr:
    if len(i) > length_of_the_most_longest_word:
        length_of_the_most_longest_word = len(i)
arr.sort()
for k, i in enumerate(arr):
    print(f"{k + 1:<2} {i : >{length_of_the_most_longest_word}}")
