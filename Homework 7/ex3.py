class Worker():

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
