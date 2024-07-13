a=int(input("Enter Value Of A : "))
b=int(input("Enter Value Of B : "))
c=int(input("Enter Value Of C : "))

if a>b:
    if a>c:
        print("A Is Max")
    else:
        print("C Is Max")
elif b>c:
    print("B Is Max")
else:
    print("C Is Max")
        
