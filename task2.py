"""

Вариант 6, Работа со строками
2.Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная,
 то длина первой части должна быть на один символ больше).
 Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

"""


def split_string(input_string):

    string_length = len(input_string)
    flag_on_parity = string_length%2
    if flag_on_parity == 0:
        string_middle = int(string_length/2)
    else:
        string_middle = int(string_length/2) + 1
    new_string = input_string[string_middle:] + input_string[:string_middle]
    print("Новая строка: ", new_string)

input_string = input("Введите строку\n")

split_string(input_string)