# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.
import random


def Search(MyNumber , compNumber, count):
    try:
        if MyNumber == compNumber:
            print(f'Молодец! Угадал! Я загадал {compNumber}')
            return
        elif count == 0:
            print(f'Не угадал за 10 попыток! Мое число {compNumber}')
            return
        else:
            return Search(int(input('Введите другое число:')), compNumber, count - 1)

    except ValueError:
        print('Вы ввели не число или пустое значение!')
        return


def main():
    Search(int(input('Введите ваше число: ')), random.randint(0, 100), 10)


if __name__ == '__main__':
    main()
