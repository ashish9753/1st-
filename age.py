age1 = int(input("enter a age1 hear: "))
age2 = int(input("enter a age2 hear: "))
age3 = int(input("enter a age3 hear: "))
if age1> age2 and age1> age3:
    print("age1 is grater")
elif age2> age1 and age2> age3:
    print("age 2 grater")
elif age3>age1 and age3> age2:
    print("age3 is grater")
else:
    print("all are equal")