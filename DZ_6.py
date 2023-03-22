# 1
# Написать лямбда функцию определяющую чётное/нечётное. Функция принимает параметр число и если чётное то
# выдаёт слово “чётное”, если нет - то “нечётное”.

# parity_definition = lambda num_user: "чётное" if num_user % 2 == 0 else "нечётное"
# print(parity_definition(4))
# print(parity_definition(5))


# 2
# Дан список чисел. Вернуть список где при помощи функции map() каждое число
# переведено в строку В качестве функции в map() каждое число использовать lambda

# list_ = [4, 1, 12]
# string = list(map(lambda num: str(num), list_))
# print(string)

# 3
# При помощи функции filter() из котрежа слов отфильтровать только те, которые являю полиндромами
#
# words = ("gaag", "true", "false", "boob")
# print(list(filter(lambda word: word == word[::-1], words)))

# 4
# Написать декоратор к функциям который бы считал и выводил
# время выполнения.
# Подсказка: from datetime import datetime time = datetime.now()

# import random
# from datetime import datetime
# from functools import wraps
# from typing import Callable
#
# def decoration(fun: Callable) -> Callable:
#     @wraps(fun)
#     def function(*args):
#         time_now = datetime.now()
#         resalt = fun(*args)
#         time_ago = datetime.now()
#         print(f"Время выполнения : {time_ago - time_now}")
#         return resalt
#     return function
#
#
# @decoration
# def even_number(number: int) -> int:
#     if type(number) == int:
#         if number % 2 == 0:
#             return True
#         elif number % 2 != 0:
#             return False
#     else:
#         return "the entered data is not a number"
# print(even_number(4))
#
# @decoration
# def get_number_of_pairs(nums: list[int], target_sum: int) -> int:
#     """
#     В заданном списке находит количество пар элементов, сумма которых равна заданному числу.
#     Примеры:
#     [1,1,1], target_sum = 2 -> 2
#     [1,2,3], target_sum = 3 -> 2
#     """
#     n = len(nums)
#     total_number = 0
#     for i in range(n):
#         sum_ = 0
#         for j in range(i, n):
#             sum_ += nums[j]
#             if sum_ == target_sum:
#                 total_number += 1
#     return total_number
#
#
# print(get_number_of_pairs([random.randint(-10, 10) for _ in range(100)], 2))