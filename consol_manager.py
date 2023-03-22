from victory import vic
from bank_account import bank_acount
import os
import shutil

'''
В коде задействованы генераторы списков для более компактной записи циклов for. 
Также используются тернарные операторы для проверки условия и выполнения действий 
в зависимости от выбранного пункта меню.
Вместо использования append() в списке lst_name, добавляем элементы в список через генератор списков, 
чтобы уменьшить количество строк кода.
Также убраны дублирование ввода названий папок и файлов, используя генераторы списков вместо циклов for.
'''


def s_dir(show=True):
    lst_name = [file.name if not show and os.path.isdir(file) else print('   ', file.name) for file in
                os.scandir(os.getcwd())]
    return [name for name in lst_name if name is not None]


def s_file(show=True):
    lst_name = [file.name if not show and os.path.isfile(file) else print('   ', file.name) for file in
                os.scandir(os.getcwd())]
    return [name for name in lst_name if name is not None]


while True:
    print('*' * 50)
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Сохранить содержимое рабочей директории в файл')
    print('13. Выход')
    print('*' * 50)

    choice = input('Выберете пункт меню: ')
    if choice == '1':
        kol = int(input('Введите количество создаваемых папок: '))
        [os.mkdir(input('Введите название папки: ')) if not os.path.exists(input('Введите название папки: '))
         else print("Папка уже существует") for i in range(kol)]
    elif choice == '2':
        os.rmdir(input("Введите название папки/файла: "))
    elif choice == '3':
        print("1. Скопировать файл")
        print("2. Скопировать папку")
        choice = input('Выберите пункт меню: ')
        name_fol = input("Введите название папки/файла: ")
        new_name_fol = input("Введите новое название папки/файла: ")
        if choice == '1':
            shutil.copy(name_fol, new_name_fol) if os.path.isfile(name_fol) else print(f"{name_fol} не является файлом")
        elif choice == '2':
            shutil.copytree(name_fol, new_name_fol) if os.path.isdir(name_fol) else print(
                f"{name_fol} не является папкой")
    elif choice == '4':
        print(sorted(os.listdir()))
    elif choice == '5':
        [print(fol) for fol in os.listdir() if os.path.isdir(fol)]
    elif choice == '6':
        [print(on_file) for on_file in os.listdir() if os.path.isfile(on_file)]
    elif choice == '7':
        print(os.name)
    elif choice == '8':
        print(os.getlogin())
    elif choice == '9':
        vic()
    elif choice == '10':
        bank_acount()
    elif choice == '11':
        os.chdir('D:\\PycharmProjects\\UII DZ\\DZ_Lesson 4_moduls\\new')
        print('Директория изменилась на: ', os.getcwd())
    elif choice == '12':
        l_dir = s_dir(show=False)
        l_file = s_file(show=False)
        data = f"files: {', '.join(i for i in l_file)}\ndirs: {', '.join(i for i in l_dir)}"
        with open('files_dirs.txt', 'w') as f:
            f.write(data)
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')
