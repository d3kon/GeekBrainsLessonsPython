N = abs(int(input('Введите количество элементов массива: ')))
items_entered = input("Введите через пробел элементы списка: ").split()
items = list(map(int, items_entered))
print(items)
if len(items) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - items[0])
    index = 0
    for i in range(1, N):
        count = abs(X - items[i])
        if count < min:
            min = count
            index = i
    print(
        f'Число {items[index]} в списке items наиболее близко по величине к числу {X}, их разница составляет {abs(X - items[index])}')