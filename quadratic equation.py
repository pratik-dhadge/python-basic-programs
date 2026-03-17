#5 For Solving Quadratic Equation
import math
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=float(input("Enter the third number: "))
d=b*b-4*a*c
if d>=0:
    root_1 = (-b + math.sqrt(d)) / (2 * a)
    root_2 = (-b - math.sqrt(d)) / (2 * a)
    print("The First root is:", root_1)
    print("The Second root is:", root_2)
else:
    print('Root is complex')