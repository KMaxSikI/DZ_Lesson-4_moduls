import random


def victory():  # Записываем функция и в ней формируем викторину
    if __name__ == '__main__':
        class Famose:  # Создан класс дата рождения + ФИО знаменитости
            def __init__(self, birthday, fio):
                self.birthday = birthday
                self.fio = fio

    b_n = [Famose('09.06.1963', 'Джон Кристофер Депп'), Famose('12.10.1968', 'Хью Джекман'),
           Famose('14.05.1944', 'Джордж Лукас'), Famose('30.09.1964', 'Моника Беллуччи'),
           Famose('30.07.1947', 'Арнольд Шварценеггер'),
           Famose('06.11.1988', 'Эмма Стоун'), Famose('12.11.1982', 'Энн Хэтэуэй'),
           Famose('11.02.1969', 'Дженнифер Энистон'),
           Famose('11.11.1974', 'Леонардо Ди Каприо'), Famose('25.09.1968', 'Уилл Смит')]  # Список дата рождения + имя

    c = random.sample(b_n, 5)  # Рандомный выбор из списка известных людей

    day_month = ('первое', 'второе', 'третье', 'четвёртое',
                 'пятое', 'шестое', 'седьмое', 'восьмое',
                 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                 'двадцать первое', 'двадцать второе', 'двадцать третье',
                 'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                 'тридцатое', 'тридцать первое')  # Переменная в которой строчно перечислены дни в месяце

    month_year = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября',
                  'декабря')  # Переменная в которой строчно перечислены месяцы в году

    counter_right = 0  # Счетчик правильных ответов
    counter_wrong = 0  # Счетчик не правильных ответов

    for i in range(
            len(c)):  # Создаем цикл, который проходится по рандомному списку "c" и проверяет правльность введенных ответов
        print(c[i].fio)
        if c[i].birthday == input('Введите ответ в формате (dd.mm.yyyy): '):
            counter_right += 1
        else:
            counter_wrong += 1
            print('Правильный ответ: ',
                  f'{day_month[int(c[i].birthday.split(".")[0]) - 1]} {month_year[int(c[i].birthday.split(".")[1]) - 1]} {c[i].birthday.split(".")[2]} года')  # Переводим день и месяц в буквенный вид

    ans_right = counter_right * 100 / 5  # Считаем % правильных ответов (5 это количество вопросов)
    ans_wrong = counter_wrong * 100 / 5  # Считаем % не правильных ответов (5 это количество вопросов)

    print('=' * 50)
    print('Количество правильных ответов: ', counter_right)
    print('Количество не правильных ответов: ', counter_wrong)
    print('% правильных ответов: ', ans_right)
    print('% не правильных ответов: ', ans_wrong)
    print('=' * 50)

if __name__ == '__main__':
    victory()  # Запускаем функциию

    que = input('Хочешь повторить ? ')  # После подведения итогов спрашиваем хочет ли игрок пройти её повторно
if __name__ == '__main__':
    while que.lower() != 'no' and que.lower() != 'нет':  # Пока игрок не ответит no/нет, функция будет запускаться и вопрос о повторном участии будет повторяться
        victory()  #
        que = input('Хочешь повторить ? ')  #
        break  # Как только игрок введет no/нет программа остановится
