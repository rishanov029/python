class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


length = int(input("Enter length 1: "))
breadth = int(input("Enter breadth 1: "))
r1 = Rectangle(length, breadth)
print("Area of the rectangle:", r1.area())
print("Perimeter of the rectangle:", r1.perimeter())

length = int(input("Enter length 2: "))
breadth = int(input("Enter breadth 2: "))
r2 = Rectangle(length, breadth)
print("Area of the rectangle:", r2.area())
print("Perimeter of the rectangle:", r2.perimeter())

if r1.area() > r2.area():
    print("The first rectangle has the larger area.")
elif r1.area() < r2.area():
    print("The second rectangle has the larger area.")
else:
    print("Both rectangles have the same area.")