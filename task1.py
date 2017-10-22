"""

Вариант 6
6.Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
Вклад составляет X рублей Y копеек. Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год
в рублях и копейках. Дробная часть копеек отбрасывается.

"""


def contribution_counter(p, x, y):
    p_in_fraction = p/100
    all_in_y = x * 100 + y  # Все в копейки
    percent_of_all = all_in_y * p_in_fraction  # Процент от копеек
    all_with_percent = percent_of_all + all_in_y

    x_in_a_year = int(all_with_percent/100)
    y_in_a_year = int(all_with_percent%100)
    print("Количество рублей вклада, полученных через год = ", x_in_a_year)
    print("Количество копеек вклада, полученных через год = ", y_in_a_year)

p = int(input("Введите P - величину процентной ставки. Число должно быть целое, <100\n"))
x = int(input("Введите X - количество рублей вклада. Число должно быть целое\n"))
y = int(input("Введите Y - количество копеек вклада. Число должно быть целое\n"))

contribution_counter(p, x, y)