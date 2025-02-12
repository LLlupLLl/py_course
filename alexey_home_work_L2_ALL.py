""" # Домашняя работа к лекции 2.

# Домашняя работа калькулятор.
msg = "Введите целое число: "
first_number, second_number = int(input(msg)), int(input(msg))

# Вычисления выражений.
print('\nРезультат вычислений: + - * /')
print(f'{first_number} + {second_number} = {first_number + second_number}')
print(f'{first_number} - {second_number} = {first_number - second_number}')
print(f'{first_number} * {second_number} = {first_number * second_number}')
print(f'{first_number} / {second_number} = {first_number / second_number}')


# Домашняя работа 2.1.
msg = 'Введите число '
first_number = int(input(f'{msg}1: '))
second_number = int(input(f'{msg}2: '))
third_number = int(input(f'{msg}3: '))
fourth_number = int(input(f'{msg}4: ')) 

# Поиск наибольшего числа.
if first_number > second_number:
    max_number_first_pair = first_number
else:
    max_number_first_pair = second_number
if third_number > fourth_number:
    max_number_second_pair = third_number
else:
    max_number_second_pair = fourth_number
if max_number_first_pair > max_number_second_pair:
    largest_number = max_number_first_pair
else:
    largest_number = max_number_second_pair

# Вывод наибольшего числа.
print('\nНаибольшее число -', largest_number)


# Домашняя работа 2.6.
operation = input('Введите операцию(+,-,*,/ или exit) ')
msg = 'Введите число: '

# Цикл с вычислениями калькулятора.
while operation != 'exit':
    first_number = int(input(msg))
    second_number = int(input(msg))
    if operation == '+':
        print(f'\n{first_number} + {second_number} = {
            first_number + second_number}')
    elif operation == '-':
        print(f'\n{first_number} - {second_number} = {
            first_number - second_number}')
    elif operation == '*':
        print(f'\n{first_number} * {second_number} = {
            first_number * second_number}')    
    elif operation == '/':
        print(f'\n{first_number} / {second_number} = {
            first_number / second_number}')
    else:
        print('Введите одну из перечисленных операции(+,-,*,/ или exit)')
    operation = input('Введите операцию(+,-,*,/ или exit) ')

print('\Вычисления окончены')
 """