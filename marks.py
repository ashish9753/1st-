m = int(input("enter a marks of student hear: "))
if m>90 and m<101:
    print("EXCELlENT")
elif m<91 and m>80:
    print("VERY GOOD")
elif m<81 and m>70:
    print("GOOD")
elif m<71 and m>60:
    print("CAN DO BATTER")
elif m<61 and m>50:
    print("AVERAGE")
elif m<51 and m>40:
    print("BELLOW AVERAGE")
elif m<41:
    print("FAIL")
else:
    print("Plese Enter A Valid Marks")