# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!


def a(n, x): return x + a(n-1, x * -0.5) if n else 0


n = float(input('Введите количество чисел: '))
print(f'Сумма = {a(n, 1)}')
