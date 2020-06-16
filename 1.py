"""
Дан массив целых чисел array и целое число k. Нужно вывести все уникальные пары чисел из массива, сумма которых равна k.

Примечание: под уникальностью понимается следующее: если ответу удовлетворяет несколько пар вида (a, b) и (b, a), то достаточно вывести только одну пару (a, b).


def search_pairs(array, k):
....


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

OUT: >> [(1, 4), (2, 3)]



Вопросы:
- Какая сложность у вашего алгоритма?
- Можно ли его оптимизировать?

Сложность данного алгоритма составляет O(n/2).
 
seq = {key for (key) in array} - одна итерация, т.е. = n

for key in seq:
    ... - одна итерация, которая прерывается когда мы достигаем середины множества (в худшем случае - элементы входного массива не повторяются) = n/2

O(n/2) = n + n/2

Проверка наличия пары во множестве производится за const время (хэш функция)

"""

import random

def get_tuple(num_1, num_2):
    if num_1 > num_2:
        return tuple([num_2, num_1])
    return tuple([num_1, num_2])


def search_pairs(array, k):
    seq = {key for (key) in array}
    retval = []
    for key in seq:
        tpl = get_tuple(key, k - key)
        if (k - key in seq) and (tpl not in retval):
            retval.append(tpl)
        elif tpl in retval:
            break
    return retval

print(search_pairs(random.sample(range(0, 100), 40), 24))