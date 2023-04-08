# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.

import random

class RandomIter:

    def __init__(self, random_num_first: int, random_num_second: int, random_num_stop: int = None):
        self.random_num_first = random_num_first
        self.random_num_second = random_num_second
        self.random_num_stop = random_num_stop

    def __next__(self):
        num = random.randint(self.random_num_first,self.random_num_second)
        if self.random_num_stop == num:
            raise StopIteration
        return num

    def __iter__(self):
        return self

random_num_first = 1
random_num_second = 5
random_num_stop = 2
# random_iterator_stop = RandomIter(random_num_first, random_num_second, random_num_stop)
# for num in random_iterator_stop:
#     print(num)

# random_iterator_nonstop = RandomIter(random_num_first, random_num_second)
# for num in random_iterator_nonstop:
#     print(num)


def random_generator(random_num_first: int, random_num_second: int, random_num_stop: int = None):
    while True:
        num = random.randint(random_num_first, random_num_second)
        if num == random_num_stop:
            break
        yield num


endless_generator = random_generator(1, 5, 2)
for num in endless_generator:
    print(num)