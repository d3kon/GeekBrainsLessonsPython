class NoneZero:
    def __set__(self, instance, value):
        if value == '':
            raise ValueError("Введено пустое значение!!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = NoneZero()
    surname = NoneZero()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Работника зовут {self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    n = input('Введите имя сотрудника: ')
    s = input('Введите фамилию сотрудника: ')
    p = input('Введите должность сотрудника: ')
    w = int(input('Введите зарплату сотрудника: '))
    b = int(input('Введите премию сотрудника: '))
    print(Position(n, s, p, w, b).get_full_name())
    print(f'Его должность: {Position(n, s, p, w, b).position}')
    print(f'Его полная зарплата: {Position(n, s, p, w, b).get_total_income()}')


# ВТОРОЙ ПРИМЕР
class NoneString:
    def __set__(self, instance, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Не может строкой")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Road:
    height = NoneString()
    thickness = NoneString()

    def __init__(self, length, width, height=25, thickness=0.05):
        self._length = length
        self._width = width
        self.height = height
        self.thickness = thickness

    def weight(self):
        return self._length * self._width * self.height * self.thickness


if __name__ == '__main__':
    result = Road(20, 5000).weight()
    print(f'\n{result / 1000} тонн')
