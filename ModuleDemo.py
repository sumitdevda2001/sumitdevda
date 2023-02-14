import UDF

while True:

    print("*************************")
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*************************")

    choice=int(input("Enter Your Choice : "))
    print("*************************")

    if choice==1:
        a=int(input("Enter Value : "))
        UDF.oddEven(a)
        print("*************************")
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        UDF.maxOfTwo(a,b)
        print("*************************")
    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        UDF.maxOfThree(a,b,c)
        print("*************************")
    elif choice==4:
        a=int(input("Enter Value : "))
        UDF.fibonacci(a)
        print("*************************")
    elif choice==5:
        a=int(input("Enter Value : "))
        UDF.prime(a)
        print("*************************")
    else:
        break
        
