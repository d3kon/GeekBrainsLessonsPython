from random import randint
N = int(input('Введите количество элементов массива: '))
items = [randint(0, 10) for x in range(N)]
print(items[:N])
number = int(input('Введите число для подсчета количества вхождений: '))
count = 0
for i in items:
    if i == number:
        count += 1
print(count)