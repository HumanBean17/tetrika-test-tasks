"""

Ответ: 871853874

"""

def is_alph(c):
    if (c > 64 and c < 91) or (c > 96 and c < 123):
        return True
    return False

def count_alph_sum(string):
    s = 0
    for c in string:
        alph_num = ord(c)
        if is_alph(alph_num):
            s += (alph_num - 64)
    return s

def get_ans(names):
    s = 0
    for i in range(0, len(names)):
        s += count_alph_sum(names[i]) * (i + 1)
    return s

names = sorted(open("names.txt", "r").read().split(","))

print(get_ans(names))