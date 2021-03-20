a = int(input("Введите расстояние: "))
b = int(input("Введите желаемый результат: "))
res = 0
if a >= b :
    print("У вас и так все хорошо.")
while a < b:
    a = a * 1.1
    res += 1
    if a >= b :
        print(f"За {res} дней")