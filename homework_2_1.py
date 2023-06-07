number = int(input("Введите целое число "))
hex_number = []
test = hex(number)
while number > 0:
    temp = number % 16
    match temp:
        case 10:
            temp = 'a'
        case 11:
            temp = 'b'
        case 12:
            temp = 'c'
        case 13:
            temp = 'd'
        case 14:
            temp = 'e'
        case 15:
            temp = 'f'
    hex_number.append(str(temp))
    number = number // 16
hex_number.extend(['x', '0'])
hex_number.reverse()
a = "".join(hex_number)
if a == test:
    print(a)
else:
    print("Что-то пошло не так.")
