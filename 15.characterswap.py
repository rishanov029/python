first = input("Enter the first string: ")
second = input("Enter the second string: ")

if len(first) > 1 and len(second) > 1:
	first, second = (
		first[0] + second[1] + first[2:],
		second[0] + first[1] + second[2:],
	)

print(first + " " + second)
