x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
a=input("Enter operator (+, -, *, /): ")
if a=='+':
    print(f"Result: {x+y}")
elif a=='-':
    print(f"Result: {x-y}")
elif a=='*':
    print(f"Result: {x*y}")
elif a=='/':
    if y==0:
        print("Cannot divide by 0")
    else:
        print(f"Result: {round(x/y, 2)}")
else:
    print("Please enter valid operator")