"""

Факториал числа n равен произведению всех чисел от 1 до n, то есть:
n! = 1 * 2 * 3 * ... * n

Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.

def get_zeros(n):
....

print(get_zeros(5))
OUT: >> 1

print(get_zeros(12))
OUT: >> 2

----------------------------------------------------------------

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