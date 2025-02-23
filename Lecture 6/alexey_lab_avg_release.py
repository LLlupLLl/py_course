'''
Task: Программа расчета годового киллометража велосипедистов
Author: Алексей Гладкий
Date: 16.02.2025
'''
annual_distance = {}

def main():
    menu = """
    1 - добавить нового велосипедиста
    2 - добавить дистанцию
    3 - рассчитать киллометраж за год
    -1 - выход\n"""

    operation = int(input(menu))  # Пользователь выбирает операцию.

    while operation != -1:  # Условие выхода из программы.
        if operation == 1:
            add_new_cyclist()  # Добавление велосипедиста.
        elif operation == 2:
            add_new_distance()  # Добавление дистанции.
        elif operation == 3:
            calculation_avg_distance()  # Расчет годового киллометража.
        operation = int(input(menu))


def add_new_cyclist():
    '''Функция добавления нового велосипедиста.'''
    name = input('\nВведите имя: ')
    if name not in annual_distance:
        annual_distance[name] = ()
        print(f'\nВелосипедист успешно создан')
    else:
        print(f'\nВелосипедист уже был создан')


def add_new_distance():
    '''Функция добавления дистанции.'''
    name = input('\nВведите имя: ')
    if name in annual_distance:
        distance = int(input('\nВведите дистанцию: '))
        annual_distance[name] += (distance, )
        print(f'\nДистанция успешно добавлена')
    else:
        print(f'\nВелосипедиста еще не существует')

def calculation_avg_distance():
    '''Функция расчета годового киллометража.'''
    if len(annual_distance) == 0:
        print(f'\nДанные о тренировках отсутствуют')
    elif len(annual_distance) > 0:
        for name in annual_distance.keys():
            distance = annual_distance[name]
            if len(distance) > 0:
                print(f'\nУ {name} годовой киллометраж равен {sum(distance)} км')
            else:
                print(f'\nУ {name} нет тренировок')


main()
