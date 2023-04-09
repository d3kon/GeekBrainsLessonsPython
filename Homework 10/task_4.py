"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def encode_and_decode(default_list):
    new_list = []
    for i in default_list:
        print(f'Строковое представление {i} в байтовом представлении: ', i.encode('utf-8'))
        new_list.append(i.encode('utf-8'))
    print('')
    for i in new_list:
        print(f'Байтовое представление {i} в строковом представлении: ', i.decode('utf-8'))


my_list = ['разработка', 'администрирование', 'protocol', 'standart']
if __name__ == '__main__':
    encode_and_decode(my_list)
