# 1) Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import my_func
n = my_func.get_int('How many numbers will be entered? ')
list_num, sum_num = [], 0
while n > 0:
    list_num.append(my_func.get_int('Enter a number: '))
    n -= 1
for i in range(1,len(list_num), 2 ):
    sum_num += list_num[i]
print(f'The resulting list: {list_num}')
print(f'Sum of odd elements = {sum_num}')

