"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


def byte_count(var):
    for line in var:
        time_count = bytes(line, 'utf-8')
        print('Тип переменной: {}'.format(type(time_count)), end=' : ')
        print('Содержание переменной - {}'.format(time_count), end=' : ')
        print('Длина строки: {}'.format(len(time_count)))


list_word_in_byte = ['class', 'function', 'method']
if __name__ == '__main__':
    byte_count(list_word_in_byte)
