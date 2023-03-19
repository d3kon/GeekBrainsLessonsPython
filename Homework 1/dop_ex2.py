# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
number = int(input('Введите трехзначное число: '))
n1 = number % 10
n2 = (number % 100) // 10
n3 = number // 100
print(number, ' -> ', n1 + n2 + n3)