numbers = []
sqrtnumbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter number: ")))
print("Numbers:",numbers)
print("Square numbers")

for num in numbers:
    sqrtnumbers.append(num**2)
print(sqrtnumbers)