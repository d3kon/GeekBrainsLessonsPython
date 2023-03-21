# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.
# Пример:
# Введите выручку фирмы: 1000
# Введите издержки фирмы: 500
# Финансовый результат - прибыль. Ее величина: 500
# Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
# Рентабельность выручки = 0.5
# Введите численность сотрудников фирмы: 10
# Прибыль фирмы в расчете на одного сотрудника = 50.0
profit = int(input('Введите выручку фирмы: '))
expenses =int(input('Введите издержки фирмы: '))
if profit > expenses:
  print('Финансовый результат - прибыль. Ее величина: ', profit - expenses)
  print('Рентабельность выручки = ', expenses / profit)
  staff = int(input('Введите численность сотрудников фирмы: '))
  print('Прибыль фирмы в расчете на одного сотрудника = ', (profit - expenses) / staff)
else:
  print('Вы в убытке.')