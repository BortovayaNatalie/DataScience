# 3 Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна,
# лето, осень). Напишите решения через list и dict.

s = int(input("Вводите номер месяца: "))

dict = {1: "Зима", 2: "Зима", 12: "Зима",
        3: "Весна", 4: "Весна", 5: "Весна",
        6: "Лето", 7: "Лето", 8: "Лето",
        9: "Осень", 10: "Осень", 11: "Осень",}
print(dict.get(s))

a = ("Зима", "Зима", "Весна", "Весна", "Весна",
     "Лето", "Лето", "Лето",
     "Осень", "Осень", "Осень", "Зима")
print(a[s-1])