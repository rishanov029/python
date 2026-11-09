string = input("Enter a string: ")
count = 0
for i in range(len(string)):
    if string[i] != "":
        count += 1
print("The number of characters in the string is:", count)