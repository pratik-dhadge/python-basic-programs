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