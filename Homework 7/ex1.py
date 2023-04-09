import time


class TrafficLight():
    colors = {'Красный': 7, 'Желтый': 2, 'Зеленый': int(input(
        'Ожидание красного - 7 секунд, ожидание желтого - 2 секунды. Введите количество секунд для ожидания зеленого цвета: '))}
    color = ''

    def SetColor(self):
        for col, CountSec in self.colors.items():
            self.color = col
            print(f'Сейчас горит {col} цвет. Он будет гореть {CountSec} секунд')
            time.sleep(CountSec)
            print(f'{col} цвет горел {CountSec} секунд.')


if __name__ == '__main__':
    TrafficLight().SetColor()

'''

решение найденное в интернетах :)))


from time import sleep as wait
from datetime import datetime as d_t

class TrafficLight:
    colors = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    color = ''

    def burn(self):
        for color, sw_time in self.colors.items():
            self.color = color
            start_state_time = d_t.now()

            print(f"Светофор горит цветом '{self.color}' {sw_time} секунды ")

            wait(sw_time)

            print(f"Светофор закончил гореть цветом '{self.color}' " 
                  f"{(d_t.now() - start_state_time).seconds} секунды ")


if __name__ == '__main__':
    TrafficLight().burn()
    
    
'''
