n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter a number: ")))

print("List:", lst)
print("Squared list:", [x**2 for x in lst])
