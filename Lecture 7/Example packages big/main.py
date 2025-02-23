'''
Task: Программа расчета годового киллометража велосипедистов
Author: Алексей Гладкий
Date: 223.02.2025
'''
from packages.cyclist import cyclist_logic as cl, exports as ce, stat as cs
from packages.crm import cyclist_logic as ccl, exports as cce, stat as ccs

def main():
    menu = """
    1 - добавить нового велосипедиста
    2 - добавить дистанцию
    3 - рассчитать киллометраж за год
    -1 - выход\n"""


    ccs.stat()

    operation = int(input(menu))  # Пользователь выбирает операцию.

    while operation != -1:  # Условие выхода из программы.
        if operation == 1:
            ccl.add_new_cyclist()  # Добавление велосипедиста.
        elif operation == 2:
            ccl.add_new_distance()  # Добавление дистанции.
        elif operation == 3:
            ccl.calculation_avg_distance()  # Расчет годового киллометража.
        operation = int(input(menu))

    cce.export()

    print('Part 2')
    cs.stat()

    operation = int(input(menu))  # Пользователь выбирает операцию.

    while operation != -1:  # Условие выхода из программы.
        if operation == 1:
            cl.add_new_cyclist()  # Добавление велосипедиста.
        elif operation == 2:
            cl.add_new_distance()  # Добавление дистанции.
        elif operation == 3:
            cl.calculation_avg_distance()  # Расчет годового киллометража.
        operation = int(input(menu))

    ce.export()

if __name__ == '__main__':
    print('main.py was started')
    main()
