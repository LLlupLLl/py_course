'''
Task: Программа расчета годового киллометража велосипедистов
Author: Алексей Гладкий
Date: 223.02.2025
'''
import cyclist_logic as cl

def main():
    menu = """
    1 - добавить нового велосипедиста
    2 - добавить дистанцию
    3 - рассчитать киллометраж за год
    -1 - выход\n"""



    operation = int(input(menu))  # Пользователь выбирает операцию.

    while operation != -1:  # Условие выхода из программы.
        if operation == 1:
            cl.add_new_cyclist()  # Добавление велосипедиста.
        elif operation == 2:
            cl.add_new_distance()  # Добавление дистанции.
        elif operation == 3:
            cl.calculation_avg_distance()  # Расчет годового киллометража.
        operation = int(input(menu))


if __name__ == '__main__':
    print('main.py was started')
    main()
