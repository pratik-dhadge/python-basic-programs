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
