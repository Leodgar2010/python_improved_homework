# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def my_func(**kwargs):
    dic = {}
    for i, j in kwargs.items():
        if isinstance(j, list) or isinstance(j, dict) or isinstance(j, set):
            dic[str(j)] = i
        else:
            dic[j] = i
    print(dic)


my_func(a=[1, 2, 3], b={2}, c={3: 'value'}, d="output")
