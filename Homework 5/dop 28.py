# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)

if __name__ == '__main__':
    print(summa(int(input('Введите первое число: ')), int(input('Введите второе число: '))))