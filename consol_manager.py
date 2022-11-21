from victory import vic
from bank_account import bank_acount
import os
import shutil

def s_dir(show=True):

    lst_name = []
    with os.scandir(os.getcwd()) as files:
        for file in files:
            if os.path.isdir(file):
                if show:
                    print('   ', file.name)
                else:
                    lst_name.append(file.name)
    return lst_name

def s_file(show=True):

    lst_name = []
    with os.scandir(os.getcwd()) as files:
        for file in files:
            if os.path.isfile(file):
                if show:
                    print('   ', file.name)
                else:
                    lst_name.append(file.name)
    return lst_name

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

    choice = input('Выберете пунк меню: ')
    if choice == '1':
        kol = int(input('Введите количество создаваемых папок: '))
        for i in range(kol):
            name_fol = input('Введите название папки: ')
            if not os.path.exists(name_fol):
                os.mkdir(name_fol)
            else:
                print("Папка уже существует")
    elif choice == '2':
        name_fol = input("Ввведите название папки/файла: ")
        os.rmdir(name_fol)
    elif choice == '3':
        print("1. Скопировать файл")
        print("2. Скопировать папку")
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            file = input("Ввведите название файла: ")
            new_file = input("Ввведите новое название файла: ")
            shutil.copy(file, new_file)
        if choice == '2':
            name_fol = input("Ввведите название папки: ")
            new_name_fol = input("Ввведите новое название папки: ")
            if os.path.exists(name_fol):
                shutil.copytree(name_fol, new_name_fol)
    elif choice == '4':
        print(sorted(os.listdir()))
    elif choice == '5':
        for fol in os.listdir():
            if os.path.isdir(fol):
                print(fol)
    elif choice == '6':
        for on_file in os.listdir():
            if os.path.isfile(on_file):
                print(on_file)
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
        print('Директрория изменилась на: ', os.getcwd())
    elif choice == '12':
        l_dir = s_dir(show=False)
        l_file = s_file(show=False)
        data = 'files:'
        sep_f_str = ' '
        for i in l_file:
            data += sep_f_str + i
            sep_f_str = ', '
        data += '\ndirs:'
        sep_d_str = ' '
        for i in l_dir:
            data += sep_d_str + i
            sep_d_str = ', '
        with open('files_dirs.txt', 'w') as f:
            f.write(data)
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')
