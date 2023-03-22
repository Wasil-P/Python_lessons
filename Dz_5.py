# 1
# Написать функцию, которая проверяет является ли целое число четным.
# Функция возвращает True, если число четное, False если нет.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.
# Ввод и вывод результата производится вне функции проверки

# def even_number(number: int) -> int:
#     if type(number) == int:
#         if number % 2 == 0:
#             return True
#         elif number % 2 != 0:
#             return False
#     else:
#         return "the entered data is not a number"
# print(even_number(4))
# print(even_number(5))
# print(even_number("fg"))


# 2
# Написать функцию, которая принимает число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Для проверки на четность использовать функцию из задания 1.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.

# def random_list_numbers(num: int) ->list:
#     list_ = [0]
#     index = 1
#     if type(num) != int or num < 0:
#         return "the entered data is not a number"
#     elif num % 2 == 0:
#         num = num ** 2
#         while index <= num:
#             if index % 7 == 0 and index % 4 == 0:
#                 break
#             else:
#                 list_.append(index)
#                 index += 1
#         return list_
#     else:
#         while index <= num:
#             if index % 7 == 0 and index % 4 == 0:
#                 break
#             else:
#                 list_.append(index)
#                 index += 1
#         return list_
# print(random_list_numbers(3))
# print(random_list_numbers(4))
# print(random_list_numbers(20))
# print(random_list_numbers(-20))
# print(random_list_numbers("sef"))




