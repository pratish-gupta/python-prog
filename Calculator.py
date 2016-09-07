while True:
	print("-----------------------")
	print("Calculator Options")
	print("-----------------------")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Quit")
	user_input =input("Enter the Option :")
	if user_input == 5:
		break
	if user_input == 1:
		num1=float(input("Enter the First Number :"))
		num2=float(input("Enter the Second Number :"))
		result=str(num1+num2)
		print("The answer is :"+result)
		print("                      ")
