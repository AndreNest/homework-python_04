# 3) Сгенерируйте список на 30 элементов.
# Отсортируйте список по возрастанию, методом сортировки выбором.
import random
import my_func
def create_list(n,a,b):
    new_list = []
    for i in range(n):
        new_list.append(random.randint(a, b+1))
    print(f'No sorted list: {new_list}')
    return  new_list

def sort_list(array):
    for i in range(0, len(array) - 1):
        min_value = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_value]:
                min_value = j
        array[i], array[min_value] = array[min_value], array[i]
    return array


sorted_list = sort_list(create_list(my_func.get_int('How many elements: '), my_func.get_int('Minimum value: '), my_func.get_int('Maximum value: ')))
print(f'Sorted list: {sorted_list}')
