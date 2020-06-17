"""

Вопросы:
- Какая сложность у вашего алгоритма?
- Можно ли его оптимизировать?

Ответ:
Сложность данного алгоритма составляет O(n).
 
seq = {key for (key) in array} - одна итерация, т.е. = n

for key in seq:
    ... - одна итерация = n

O(n) = n + n

Проверка наличия пары во множестве производится за const время (хэш функция)

"""

import random


def search_pairs(array, k):
    seq = {key for (key) in array}
    retval = []
    for key in seq:
        if (k - key in seq) and (key <= k - key):
            retval.append(tuple([key, k - key]))
    return retval

print(search_pairs(random.sample(range(0, 100), 40), 24))