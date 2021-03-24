# 5. Реализовать структуру «Рейтинг», представляющую
# собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.

list_r = []
while True:
    a = int(input('Ведите число: '))
    idx = None
    for i, num in enumerate(list_r):
        if a > num:
            idx = a
        break

    if idx is None:
        list_r.append(a)
    else:
        list_r.insert(idx, a)

        print(list_r)

    c = input('Добавить число? Any Key/No ')
    if c.lower() == 'n':
        break
