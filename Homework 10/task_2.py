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


def Byte(var):
    for line in var:
        print('Тип переменной: {}'.format(type(line)), end=' : ')
        print('Содержание переменной - {}'.format(line), end=' : ')
        print('Длина строки: {}'.format(len(line)))


list_word_in_byte = [b'class', b'function', b'method']
if __name__ == '__main__':
    Byte(list_word_in_byte)

