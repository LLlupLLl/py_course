""" # Домашняя работа 3.1.
hat_list = [1, 2, 3, 4, 5]  # Создаем список.

print(f'Длина списка - {len(hat_list)}')

hat_list.insert(
    2, int(input("Введи число:")))  # Добавление нового элемента списка.
hat_list.pop()  # Удаление последнего элемента списка.

print(f'Новый список - {hat_list}')
print(f'Длина нового списка - {len(hat_list)}')


# Домашняя работа 3.3.
# Создаем список. Запрашиваем кол-во элементов, затем вводим их.
list = [int(input('Введите элемент списка: ')) for i in range(int(input(
        'Введите количество элементов списка: ')))]
print(f'\nИсходный список - {list}')

# Cортировка пузырьком.
swapped = True
while swapped:
    swapped = False
    for i in range(len(list)-1):
        if list[i] > list[i+1]:  
            list[i], list[i+1] = list[i+1], list[i]
            swapped = True
print(f'\nОтсортированный список - {list}')


# Домашняя работа 3.5.
# Вывод суммы элементов списка.
print(f'\nСумма элементов - {sum([int(value) for value in input(
        'Введите через пробел элементы: ').split()])}')
 """