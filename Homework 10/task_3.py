"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def byte_or_not_byte(list_word):
    for i in list_word:
        s = i.encode('utf-8')
        try:
            if len(s) != len(i):
                raise ValueError
        except ValueError:
            print(f'Слово {i} нельзя записать без функции encode/decode\n')
        else:
            print(f'Слово {i} можно записать без функции encode/decode\n')


word_list = ['attribute', 'класс', 'функция', 'type']
if __name__ == '__main__':
    byte_or_not_byte(word_list)
