n = int(input("Enter a number of elements: "))
num_list = []
for i in range(n):
    x = int(input("Enter a number: "))
    if x<100:
        num_list.append(x)
    else:
        num_list.append('Over')
print(num_list)