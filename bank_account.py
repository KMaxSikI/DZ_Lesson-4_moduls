def data_ver(balans):
    while not balans.isdigit():
        balans = int(input('Введите корректную сумму: '))
    return balans

# def test_data_ver():
#     assert isinstance(data_ver())


def bank():
    balans = 0
    history = []

    while True:
        print('*' * 20)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('*' * 20)
        print('-' * 20)
        print(f'Ваш баланс равен {balans}')
        print('-' * 20)

        choice = input('Выберите пункт меню ')
        if choice == '1':
            print('*' * 20)
            cash = int(input('Введите сумму пополнения: '))
            balans += cash
        elif choice == '2':
            print('*' * 20)
            cost = int(input('Введите цену: '))
            print('-' * 20)
            name = input('Наименование покупки: ')
            print('*' * 20)
            if cost > balans:
                print('*' * 20)
                print('Недостаточно средств, пополните баланс!')
                print('*' * 20)
            else:
                balans -= cost
                history.append(f'{name} --> {cost}$')
        elif choice == '3':
            print('*' * 20)
            print(history)
            print('*' * 20)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

    return f'Ваш баланс равен {balans}'

print(bank())
