# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def my_func(text):
    a = text.split(".")[1]
    b = text.split('\\')[-1].split(".")[0]
    c = text.split(a)[0]
    return c, b, a


text = r"C:\Users\pnsmi\YandexDisk\Learning\Python_improved\Homeworks\homework_5_2.py"
print(my_func(text))
