# write a lambda function to find area of square, rectangle and triangle
a = int(input("Enter the sides of square: "))
square_area = lambda x: x ** 2
print("Area of square:", square_area(a))

b = int(input("Enter the length of rectangle: "))
c = int(input("Enter the width of rectangle: "))
rectangle_area = lambda l, w: l * w
print("Area of rectangle:", rectangle_area(b, c))

d = int(input("Enter the base of triangle: "))
e = int(input("Enter the height of triangle: "))
triangle_area = lambda base, height: 0.5 * base * height
print("Area of triangle:", triangle_area(d, e))