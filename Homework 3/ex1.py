month = int(input('Введите номер месяца 1 - 12: '))

# Способ через список
# month_list = ["Зима", "Весна", "Лето", "Осень"]
# if month == 1 or month == 2 or month == 12:
#     print(month_list[0])
# elif month == 3 or month == 4 or month == 5:
#     print(month_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(month_list[2])
# else:
#     print(month_list[3])


# Способ через словарь
mont_dict = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for k, v in mont_dict.items():
    if month in v:
        print(k)

#В данном примере решение через словарь логичнее, т.к. массив элементов неизменяемый
