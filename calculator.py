operation = ""
number1 = 0
number2 = 0
answer = 0


def plus(num1,num2):
	num3 = float(num1) + float(num2)
	return num3
	print (num3)
def minus(num1,num2):
	num3 = float(num1) - float(num2)
	return num3
	print (num3)
def mult(num1,num2):
	num3 = float(num1) * float(num2)
	return num3
	print (num3)
def divid(num1,num2):
	num3 = float(num1) / float(num2)
	return num3
	print (num3)
def expo (num1,num2):
	num3 = float(num1) ** float(num2)
	return num3
def modul (num1, num2):
	num3 = float(num1) % float(num2)
	return num3

def main():
	print("Welcome to the text-based Calculator")
	number1 = input('What is your input1?')
	number2 = input('What is your input2?')
	operation = input ('What to do?')

	if operation == "add":
		answer = plus(number1, number2)
		print(answer)
	elif operation == "sub":
		answer = minus(number1, number2)
		print(answer)
	elif operation == "mul":
		answer = mult(number1, number2)
		print(answer)
	elif operation == "div":
		answer = divid(number1, number2)
		print(answer)
	elif operation == "exp":
		answer = expo(number1, number2)
		print(answer)
	elif operation == "mod":
		answer = modul(number1, number2)
		print(answer)
	else:
		print ('input a valid function')

main()
