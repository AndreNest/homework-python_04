# 2) Написать программу, которая генерирует двумерный массив на A x B элементов
# ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки
# (не пользуемся встроенными методами подсчета суммы)
import my_func
def create_2d_list(a, b):
    list_2d = []
    for i in range(a):
        list_2dd = []
        for k in range(b):
            list_2dd.append(my_func.get_int('Insert num: '))
        list_2d.append(list_2dd)
    return list_2d

def ar_mean_and_print(arr):
    for line in arr:
        for el in line:
            print(el, end=" ")
        print()
    num_line = 0
    for line in arr:
        sum_line = 0
        for el in line:
            sum_line = sum_line + el
        num_line += 1
        print(f'In line {num_line} sum of the elements = {sum_line}')


ar_mean_and_print(create_2d_list(my_func.get_int('Insert num "A": '), my_func.get_int('Insert num "B": ')))