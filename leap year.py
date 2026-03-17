#12 check Leap Year
a=int(input("Enter Year: "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print("Year is Leap=",a)
else:
    print("Year is not Leap")