from calculator import sum

if __name__=='__main__':
	try:
		number1 = int(input("Set a number: "))
		number2 = int(input("Set other number: "))
		result = sum(number1, number2)
		print(result)
	except:
		print("Erro to set a number")