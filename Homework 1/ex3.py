# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
# Пример:
# Введите число n: 3
# n + nn + nnn = 369
n = int(input('Введите число n: '))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
print('n + nn + nnn = ', n + int(t1) + int(t2))