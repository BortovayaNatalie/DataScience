# 5. Запросите у пользователя значения выручки
# и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка
# больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала
# с прибылью, вычислите рентабельность выручки (соотношение
# прибыли к выручке). Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчете на одного сотрудника.

kassa = int(input("Введите сумму выручки: "))
lost = int(input("Введите сумму издержек: "))
if kassa > lost:
    a = (kassa - lost)/kassa
    print(f"Поздравляю! Вы с прибылью. "
          f"Рентабельность выручки = {a}")
    b = int(input("Введите число сотрудников: "))
    c = (kassa - lost)/b
    print(f'Прибыль фирмы в расчете на одного сотрудника: {c}')
else:
    print("Sorry, you fired.")