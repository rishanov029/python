num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

a, b = abs(num1), abs(num2)
while b:
	a, b = b, a % b

print("GCD:", a)
