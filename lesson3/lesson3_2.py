#2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def describe_user(name, family, birth, city, email, phone):
    """Выводит данные пользователя в одну строку"""
    full_data = f"{name}, {family}, {birth}, {city}, {email}, {phone}"
    return full_data.title()
user = describe_user(name='Noname', family='Nofamily', birth='0000',
                  city='Neverland', email='aaa@mail.ru',
                  phone='999-999-99-99-99')
print(user)

