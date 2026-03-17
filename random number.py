#7 Generate Random Number given range
import random
start=int(input("Enter the start number: "))
end=int(input("Enter the end number: "))
num=random.randint(start,end)
print("Random number is: ", num)