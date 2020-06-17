"""

Вопросы:
- Какая сложность у вашего алгоритма?

Ответ: O(n)

Для решения данной задачи была использована статья: https://brilliant.org/wiki/trailing-number-of-zeros/

"""

import math


def get_zeros(n):
    if n <= 0: return 0
    k = math.floor(math.log(n, 5))
    zeroes = 0
    i = 1
    while k > 0:
        zeroes += math.floor(n / math.pow(5, i))
        i += 1
        k -= 1
    return zeroes

print(get_zeros(777))