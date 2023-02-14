a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if a>b:
    if a>c:
        print("A is Greater Number")
    else:
        print("C is Greater Number")
elif b>c:
    print("B is Greater Number")
else:
    print("C is Greater Number")
