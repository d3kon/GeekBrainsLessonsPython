# -- coding: cp1251 --

def calc():
	operation = input('������� �������� *, +, -, /: ')

	a = input('������� ������ �����: ')
	b = input('������� ������ �����: ')

	try:
		a, b = int(a), int(b)
	except:
		print("������� �� �����")
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
				print(" �������� ��������")
				return calc()

def main():
	calc()

if __name__ == '__main__':
	main()