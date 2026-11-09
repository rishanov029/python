items = input("Enter numbers separated by commas: ").split(",")
print(sum(int(item) for item in items if item.strip()))
