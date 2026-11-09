def fibonacci_series(n):
	first, second = 0, 1

	for _ in range(n):
		print(first, end=" ")
		first, second = second, first + second


n = int(input("Enter the number of terms: "))
if n < 0:
	print("Please enter a non-negative number of terms.")
else:
	fibonacci_series(n)
