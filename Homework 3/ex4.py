# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()


# первый способ
def my_func(a, b, c):
    z = [a, b, c]
    z.sort()
    print('Отсортированный список: ', z)
    z.pop(0)
    print('Список без минимального элемента: ', z)
    print('Сумма = ', sum(z))

my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')))

# второй способ

def my_func(a, b, c):
    z = [a, b, c]
    print('Первоначальные элементы: ', z)
    z.remove(min(a, b, c))
    print('После удаления минимального значения списка: ', z)
    print(sum(z))

my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')))