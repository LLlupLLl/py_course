import cyclist_logic

def show_cyclists():
    '''Функция вывода списка велосипедистов с тренировками'''
    if len(cyclist_logic.annual_distance) == 0:
        print(f'\nДанные о велосипедистах отсутствуют')
    elif len(cyclist_logic.annual_distance) > 0:
        print('\nСписок велосипедистов:')
        for k, v in cyclist_logic.annual_distance.items():
                print(f'\nИмя: {k} | тренировки: {v}')
