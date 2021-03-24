# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

new_tovar = {}
general_list = []
res_list = []
i = 0
while True:
    a = input('Название товара: ')
    a1 = int(input("Цена товара: "))
    a2 = int(input("Количество товара: "))
    a3 = int(input("Введите единицу измерения: 1-шт., 2-кг., 3-л.: "))
    if a3 <= 3:
        if a3 >= 1:
            i += 1
            new_tovar["Название"] = a
            new_tovar["Цена"] = a1
            new_tovar["Количество"] = a2
            if a3 == 1:
                new_tovar["единица измерения"] = "шт."
            elif a3 == 2:
                new_tovar["единица измерения"] = "кг."
            elif a3 == 3:
                new_tovar["единица измерения"] = "л."
        tuple1 = (i, new_tovar)
        general_list.append(tuple1)
        print(general_list)
        dict_tovar = dict(general_list)
        search1 = [tovar["Название"] for tovar in dict_tovar.values()]
        print(f"Название:, {search1},")
        search2 = [tovar["Цена"] for tovar in dict_tovar.values()]
        print(f"Цена:, {search2},")
        search3 = [tovar["Количество"] for tovar in dict_tovar.values()]
        print(f"Количество:, {search3},")
        search4 = [tovar["единица измерения"] for tovar in dict_tovar.values()]
        for item in search4:
            if item not in res_list:
                res_list.append(item)
        print(f"единица измерения: {res_list}")
    else:
        print("Вы ошиблись, попробуйте снова")
    c = input('Добавить товар? Any Key/No ')
    if c.lower() == 'n':
        break