l = int(input("enter a length hear: "))
b = int(input("enter a height hear: "))

a = l*b
p = 2*(l+b)
abig = a-p
pbig = p-a
if (a>p):
    print("area is grater then perimeter ",abig)
elif (p>a):
    print("perimeter is grater then area ",pbig)
else:
    print("both are equal ")

