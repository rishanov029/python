numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    numbers.append(int(input("Enter number: ")))

print("Numbers:",numbers)

print("positive numbers")

for num in numbers:
    if num > 0:
        print(num)