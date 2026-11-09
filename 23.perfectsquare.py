from math import isqrt


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

numbers = []
for number in range(max(start, 1000), min(end, 9999) + 1):
	root = isqrt(number)
	if root * root == number and all(int(digit) % 2 == 0 for digit in str(number)):
		numbers.append(number)

print(numbers)
