y = int(input("enter a year hear: "))
if y%4==0 and y%100!=0:
    print("yes this is a leap year")
elif y%100==0:
    print("no is not leap year")
elif y%400==0:
    print("yes this is a leap year")
else:
    print("no is not leap year")