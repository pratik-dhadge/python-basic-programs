
#2 Addition of 2 no
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
c=a+b
print(c)

#3 Area of Triangle
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = (base * height) / 2
print("The area of the triangle is:", area)

#4 Square of any No
v=int(input("Enter the value of v: "))
print("square of the value is:", v*v)

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

#6 Swap to variable
a=int(input("a=: "))
b=int(input("b: "))
temp=a
a=b
b=temp
print('After Swapping=')
print('a=',a)
print('b=',b)

#7 Generate Random Number given range
import random
start=int(input("Enter the start number: "))
end=int(input("Enter the end number: "))
num=random.randint(start,end)
print("Random number is: ", num)

#8 kilometer to miles
km=float(input("Enter Kilometer"))
miles=km*0.621371
print("The miles is: ", miles)

#9 Celcius to Fahrenhite
celcius=float(input("Enter Celcius"))
fahrenheit=(celcius*9/5)+32
print("The fahrenheit is: ", fahrenheit)

#10 Check no is positive or negative
a=int(input("Enter a number: "))
if a>0:
    print("a is positive")
elif a==0:
    print("a is zero")
else:
    print("a is negative")

#11 Check No is Even Or odd
a=int(input("Enter a number: "))
if a%2==0:
    print("a is even")
else:
    print("a is odd")

#12 check Leap Year
a=int(input("Enter Year: "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print("Year is Leap=",a)
else:
    print("Year is not Leap")

#13 Largest Among 3 no
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

if a == b == c:
    print("All numbers are equal")
elif a >= b and a >= c:
    print("a is largest no =", a)
elif b >= a and b >= c:
    print("b is largest no =", b)
else:
    print("c is largest no =", c)

#14 check prime no
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")

#15 all prime no in an interval
s_n = int(input("Enter starting number: "))
e_n = int(input("Enter ending number: "))
count = 0
for num in range(s_n, e_n + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            count += 1
print("Total prime numbers =", count)

#16 find factorial of no.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)

#17 Display multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#18 print the fibonacci no
n = int(input("Enter number of terms: "))
a = 0
b = 1
print(a)
print(b)
for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c

#19 Check Armstrong No
num = int(input("Enter number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp // 10
if num == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")

#20 Armstrong No in an interval

s_n = int(input("Enter starting number: "))
e_n = int(input("Enter ending number: "))
for num in range(s_n, e_n + 1):
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit**3
        temp = temp // 10

    if num == sum:
        print(num)

#21 display calender
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
print(calendar.month(year, month))

#22 fibonacci sequence using recursion
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter number of terms: "))
for i in range(n):
    print(fib(i))

#23
