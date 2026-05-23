x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))
if x>y and x>z:
    print(f"Largest number is: {x}")
elif y>x and y>z:
    print(f"Largest number is: {y}")
elif z>x and z>y:
    print(f"Largest number is: {z}")
else:
    print("Please enter three different numbers")