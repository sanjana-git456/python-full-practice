x = int(input("Enter a number: "))
f=1
for i in range (1, x+1):
    f*=i
print(f"Factorial is: {f}")

print("Using recursion")
def factorial(x):
    if x<0:
        print("Enter positive number")
    elif x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
print(f"Factorial is: {factorial(x)}")