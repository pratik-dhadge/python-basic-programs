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