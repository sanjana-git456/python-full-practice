x = int(input("Enter number: "))
a=0
b=1
print("Fibonacci series:")
for i in range(x):
    print(a, end = " ")
    a,b = b, a+b

print("\n")
print("Using recursion")
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci series:")
for i in range(x):
    print(fibonacci(i), end = " ")