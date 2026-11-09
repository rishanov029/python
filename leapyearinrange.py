syear = int(input("Enter year1: "))
eyear = int(input("Enter year2: "))
for i in range(syear,eyear+1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            print(i)