#3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(seq):
    m1 = m2 = None
    for i in seq:
        if m2 is None:
            m2 = i
        elif m1 is None:
            if i > m2:
                m1, m2 = m2, i
            else:
                m1 = i
        elif i > m2:
            m1, m2 = m2, i
        elif i > m1:
            m1 = i
    return(m1 + m2)

a = [1, 2, 39]
count = my_func(a)
print(count)
