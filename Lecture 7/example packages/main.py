'''
Task: Программа расчета годового киллометража велосипедистов
Author: Алексей Гладкий
Date: 223.02.2025
'''
from package_cyclist import stat, cyclist_logic, exports

def main():
    menu = """
    1 - добавить нового велосипедиста
    2 - добавить дистанцию
    3 - рассчитать киллометраж за год
    -1 - выход\n"""


    stat.stat()

    operation = int(input(menu))  # Пользователь выбирает операцию.

    while operation != -1:  # Условие выхода из программы.
        if operation == 1:
            cyclist_logic.add_new_cyclist()  # Добавление велосипедиста.
        elif operation == 2:
            cyclist_logic.add_new_distance()  # Добавление дистанции.
        elif operation == 3:
            cyclist_logic.calculation_avg_distance()  # Расчет годового киллометража.
        operation = int(input(menu))

    exports.export()

if __name__ == '__main__':
    print('main.py was started')
    main()
