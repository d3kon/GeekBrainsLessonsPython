class Road:
    def __init__(self, _length, _width, weight, thickness):
        self._length = float(_length)
        self._width = float(_width)
        self.weight = float(weight)
        self.thickness = float(thickness)

    def WAsph(self):
        length = self._length
        width = self._width
        weight = self.weight
        thickness = self.thickness
        if length <= 0 or width <= 0 or weight <= 0 or thickness <= 0:
            print('Одно из значений равно нулю!')
        else:
            WeightAllRoad = length * width * weight * (thickness / 100) / 1000
            return f"Масса асфальта\n{length} м * {width} м * {weight} кг * {thickness} см = {WeightAllRoad} т"


if __name__ == '__main__':
    try:
        a = input('Введите длину полотна в метрах: ')
        b = input('Введите ширину полотна в метрах: ')
        c = input('Введите вес квадрата полотна в кг: ')
        d = input('Введите толщину полотна в см: ')
        print(Road(a, b, c, d).WAsph())
    except ValueError:
        print('Какой - то элемент введен неверно!')
