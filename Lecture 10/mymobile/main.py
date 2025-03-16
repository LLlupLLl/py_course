'''
Task: Программа мобильный телефон
Author: Алексей Гладкий
Date: 16.03.2025
'''
import mobile_phone_class

def main():
    menu = """
    1 - включить телефон
    2 - выключить телефон
    3 - позвонить
    -1 - выход\n
    Выбрать пункт меню: """


    operation = int(input(menu))

    while operation != -1:
        if operation == 1:
            print(f'\n{mobile_phone_class.phone1.turn_on()}')
        elif operation == 2:
            print(f'\n{mobile_phone_class.phone1.turn_off()}')
        elif operation == 3:
            print(f'\n{mobile_phone_class.phone1.call('911')}')
        operation = int(input(menu))


if __name__ == '__main__':
    print('main.py was started')
    main()
