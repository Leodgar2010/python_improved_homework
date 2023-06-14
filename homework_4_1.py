# Напишите функцию для транспонирования матрицы
def my_func(matrix):
    arr = []
    for i in range(len(matrix)):
        arr_internal = []
        for k in range(len(matrix[i])):
            arr_internal.append(matrix[k][i])
        arr.append(arr_internal)
    return arr


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_func(matrix))
