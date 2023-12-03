cp = int(input("enter a cost price hear: "))
sp = int(input("enter a selling price hear: "))
p = sp -cp
l = cp - sp
if(p > l):
    print("saller in profit ",p)
elif(l > p):
    print("saller in loss ",l)
else:
    print("saller no profit and no any loss")