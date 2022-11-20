import os
import json


def bank_acount(balans=0, history_balans=[], order_history=[]):
    if os.path.exists('history_balans_order.txt'):
        with open('history_balans_order.txt', 'r') as f_bo:
            balans, history_balans, order_history = json.load(f_bo)
        print('Выписка сформирована')
    else:
        balans = 0
        history_balans = []
        order_history = []

    while True:
        print('*' * 20)
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Остаток на счете')
        print('5. Выход')
        print('*' * 20)

        choice = input('Введите пункт меню: ')

        if choice == '1':
            add_cash = int(input('Введите сумму пополнения, без копеек: '))
            balans += add_cash
            history_balans.append((f'Пополнение на: {add_cash}'))
        elif choice == '2':
            order_cash = int(input('Введите сумму покупки, без копеек: '))
            if order_cash > balans:
                print(f'Недостаточно средств, остаток равен {balans}. Пополните баланс!')
            else:
                order = input('Наименование покупки: ')
                order_history.append((f'Наименование товара: {order}, Стоимость товра: {order_cash}'))
                balans -= order_cash
                history_balans.append(('Сприсание на: ', -order_cash))
        elif choice == '3':
            if len(order_history) == 0:
                print('Покупок не было')
            else:
                print(order_history)
        elif choice == '4':
            print('~*~/' * 5)
            print(f'Ваш остаток: {balans}')
            print('~*~/' * 5)
        elif choice == '5':
            with open('history_balans_order.txt', 'w') as f_bo:
                json.dump((balans, history_balans, order_history), f_bo, ensure_ascii=False)
            break
        else:
            print('Не верный пункт меню')
    return balans, history_balans, order_history


bank_acount()