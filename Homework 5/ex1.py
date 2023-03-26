# -- coding: cp1251 --

def calc():
	operation = input('Введите операцию *, +, -, /: ')

	a = input('Введите первое число: ')
	b = input('Введите второе число: ')

	try:
		a, b = int(a), int(b)
	except:
		print("Введено не число")
		return calc()
	else:
		match operation:
			case "+":
				print(a + b)
				return calc()
			case "-":
				print(a - b)
				return calc()
			case "/":
				print(a / b)
				return calc()
			case "*":
				print(a * b)
				return calc()
			case "0":
				return
			case _:
				print(" Неверная операция")
				return calc()

def main():
	calc()

if __name__ == '__main__':
	main()