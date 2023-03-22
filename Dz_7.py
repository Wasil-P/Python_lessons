# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров

from datetime import datetime
from typing import Callable
from functools import wraps

def func_time_name(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        if not args and not kwargs:
            parameter = f'без параметров'
        elif not kwargs:
            parameter = f'c позиционными параметрами{args}'
        elif not args:
            parameter = f'c именнованными параметрами{kwargs}'
        else:
            parameter = f'c позиционными параметрами{args} и именнованными параметрами{kwargs}'
        print(f'Функция {func.__name__} вызвана в {datetime.now()} {parameter}')
        func_resalt = func(*args, **kwargs)
        return func_resalt
    return inner


@func_time_name
def add(a=2, b=5):
    return a + b
print(add(1, 4))
print(add(a=2, b=3))
print(add(3, b=5))
print(add())