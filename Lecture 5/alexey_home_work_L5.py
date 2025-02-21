# # Home work 5.1.
# def is_year_leap(year):  # Функция для опредения года.
#     if year % 400 == 0 or \
#         year % 4 == 0 and year % 100 != 0:  # Условие для высокосного года.
#         return True
#     return False  # Условие для невысокосного года.


# test_data = [1500, 1900, 2000, 2016, 1987]
# test_results = [False, False, True, True, False]

# for year, result in zip(test_data, test_results):
#     if is_year_leap(year) == result:
#         print(year, 'is leap?-->', result)
#     else:
#         print(year, 'from your func -->', is_year_leap)
#         print('but expected -->', result)

# # Home work 5.4.
# number = int(input('Введите число Фибоначчи: '))

# def fibonacci(number):
#     '''Вычисление числа Фибоначчи'''
#     if number < 1:
#         return 0
#     if number < 3:
#         return 1

#     fib1 = fib2 = 1
#     for i in range(2, number):
#         fib1, fib2 = fib2, fib1+fib2
#     return fib2


# print(f'\n{number}-ое(ье) число Фибоначчи = {fibonacci(number)}')
