annual_distance = {}

def add_new_cyclist():
    '''Функция добавления нового велосипедиста.'''
    name = input('\nВведите имя: ')
    if name not in annual_distance:
        annual_distance.update({name: ()})
        print(f'\nВелосипедист успешно создан')
    else:
        print(f'\nВелосипедист уже был создан')


def add_new_distance():
    '''Функция добавления дистанции.'''
    name = input('\nВведите имя: ')
    if name in annual_distance:
        distance = int(input('\nВведите дистанцию: '))
        annual_distance.update({name: annual_distance.get(name)+(distance, )})
        print(f'\nДистанция успешно добавлена')
    else:
        print(f'\nВелосипедиста еще не существует')


def calculation_avg_distance():
    '''Функция расчета годового киллометража.'''
    if len(annual_distance) == 0:
        print(f'\nДанные о тренировках отсутствуют')
    elif len(annual_distance) > 0:
        for name in annual_distance.keys():
            distance = annual_distance.get(name)
            if len(distance) > 0:
                print(f'\nУ {name} годовой киллометраж равен {sum(distance)} км')
            else:
                print(f'\nУ {name} нет тренировок')


def delete_cyclist():
    '''Функция удаления велосипедиста.'''
    name = input('\nВведите имя: ')
    if name in annual_distance:
        annual_distance.pop(name)
        print(f'\nВелосипедист успешно удален')
    else:
        print(f'\nВелосипедиста не существует')
