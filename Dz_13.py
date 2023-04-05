# 1. Написать бесконечный итератор, который возвращает случайно число в заданном диапазоне.
# Реализовать через класс-итератор и через функцию-генератор.
# Протестировать обе реализации в цикле for.

# Дополнительно (если есть время) добавить параметр стоп-число: как только генератор
# выдает стоп-число, он заканчивает генерировать новые.

import random

class RandomIter:

    def __init__(self, random_num: int, random_num_stop: int = None):
        self.random_num = random_num
        self.random_num_stop = random_num_stop

    def __next__(self):
        if self.random_num_stop == self.random_num:
            raise StopIteration
        result = self.random_num
        self.random_num += 1
        return result

    def __iter__(self):
        return self

random_num = random.randint(1,5)
random_num_stop = random_num + random.randint(5,7)
random_iterator_stop = RandomIter(random_num, random_num_stop)
for num in random_iterator_stop:
    print(num)

random_iterator_nonstop = RandomIter(random_num)
for num in random_iterator_nonstop:
    print(num)


def random_generator(random_num: int, random_num_stop: int = None):
    while True:
        if random_num == random_num_stop:
            break
        yield random_num
        random_num += 1

endless_generator = random_generator(random_num, random_num_stop)
for num in endless_generator:
    print(num)