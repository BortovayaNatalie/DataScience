# 2. Для списка реализовать обмен значений соседних
# элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для
# заполнения списка элементов необходимо использовать
# функцию input().

s = input("Ввод: ")
from itertools import chain
if (len(s)) / 2 > 0:
    a = list(chain.from_iterable(zip(s[1:-1:2], s[::2])))
    b = list(s[:-2:-1])
    print(a + b)
else:
    print(a)

