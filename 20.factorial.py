number = int(input("Enter a non-negative integer: "))

if number < 0:
	print("Factorial is not defined for negative numbers.")
else:
	factorial = 1
	for value in range(1, number + 1):
		factorial *= value

	print(f"Factorial of {number} is {factorial}")
