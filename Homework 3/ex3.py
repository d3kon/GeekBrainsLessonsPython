# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456
def data_people(**kwargs):
    print(kwargs["name"], kwargs["s_name"], kwargs["year"], 'года рождения, проживает в городе ', kwargs["live_town"], ', email:', kwargs["email"], ', телефон: ', kwargs["phone"])
try:
    data_people(name=input('Ввведите имя: '),
                s_name=input('Введите фамилию: '),
                year=int(input('Введите год рождения: ')),
                live_town=input('Введите город проживания: '),
                email=input('Ввведите email: '),
                phone=int(input('Ввведите номер телефона: ')))
except ValueError:
    print('Неккоректные данные, повторите ввод')