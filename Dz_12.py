# 1
# Реализовать декоратор ЧЕРЕЗ КЛАСС!, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

# from datetime import datetime
#
# class FuncNameTime:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         if not args and not kwargs:
#             parameter = f'без параметров'
#         elif not kwargs:
#             parameter = f'c позиционными параметрами{args}'
#         elif not args:
#             parameter = f'c именнованными параметрами{kwargs}'
#         else:
#             parameter = f'c позиционными параметрами{args} и именнованными параметрами{kwargs}'
#         print(f'Функция {self.func.__name__} вызвана в {datetime.now()} {parameter}')
#         func_resalt = self.func(*args, **kwargs)
#         return func_resalt
#
# @FuncNameTime
# def add(a=2, b=5):
#     return a + b
#
# print(add(1, 4))
# print(add(a=2, b=3))
# print(add(3, b=5))
# print(add())

# 2
# Добавить обработку исключений в следующие задания:

    # 3* (из ДЗ номер 3)
    # Написать мини-игру «Камень ножницы бумага с ботом», в которой пользователь должен выбрать либо камень,
    # либо ножницы, либо бумагу. Бот делает случайный выбор (случайное число).
    # Вывести результат если, например, игрок выбрал бумагу, а бот ножницы:
    # Бот выбрал ножницы, вы проиграли!
    # Подсказка: я не показывала, как в Pyhon получить случайное число, попробуйте найти это сами

class Otherwise(Exception):
    pass

from random import randint

greetings = print('Приветствую вас! Вам нужно выбрать один из вариантов ответа, введя номер:\n '
                  '1 Камень\n 2 Ножницы\n 3 Бумага')
try:
    answer_user = int(input('Ваш выбор: '))
except ValueError:
    print("Вы ввели недопустимое значение")
else:
    answer_bot = randint(1, 3)
    print(answer_bot)
    if answer_user == 1:
        if answer_bot == 2:
            print('Бот выбрал Ножницы, вы победили!')
        elif answer_bot == 3:
            print('Бот выбрал Бумага, вы проиграли!')
        else:
            print('Бот тоже выбрал Камень, ничья!')
    elif answer_user == 2:
        if answer_bot == 1:
            print('Бот выбрал Камень, вы проиграли!')
        elif answer_bot == 3:
            print('Бот выбрал Бумага, вы победили!')
        else:
            print('Бот тоже выбрал Ножницы, ничья!')
    elif answer_user == 3:
        if answer_bot == 1:
            print('Бот выбрал Камень, вы победили!')
        elif answer_bot == 2:
            print('Бот выбрал Ножницы, вы проиграли!')
        else:
            print('Бот тоже выбрал Бумага, ничья!')
    else:
        raise Otherwise("Вы ввели недопустимое число")

    # 2 (из ДЗ номер 5)
    # Написать функцию, которая принимает целое число n и выводит числа от 0 до n.
    # Если число является четным, вывести квадрат числа, вместо числа.
    # Если число делится на 7 и на 4 одновременно, процесс останавливается.
    # Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.

# class EnteredNumberError(Exception):
#     pass
#
#
# def random_list_numbers(num: int):
#     list_ = [0]
#     index = 1
#     if type(num) != int or num < 0:
#             raise EnteredNumberError("the entered data is not a number, or is a negative number")
#     elif num % 2 == 0:
#         num = num ** 2
#         while index <= num:
#             if index % 7 == 0 and index % 4 == 0:
#                 raise EnteredNumberError("forced stop")
#             else:
#                 list_.append(index)
#             index += 1
#         return list_
#     else:
#         while index <= num:
#             if index % 7 == 0 and index % 4 == 0:
#                 raise EnteredNumberError("forced stop")
#             else:
#                 list_.append(index)
#             index += 1
#         return list_
#
#
# try:
#     print(random_list_numbers(4))
#     print(random_list_numbers(-4))
#     print(random_list_numbers("sef"))
#     print(random_list_numbers(28))
# except EnteredNumberError:
#     print("invalid value entered")