x = input("Enter string: ")
print(f"Reversed string is: {x[::-1]}")
n = len(x)
a = ""
while n:
    a += x[n-1]
    n-=1
print(f"Reversed string is: {a}")
b = reversed(x)
print(f"Reversed string is: ", end = "")
for i in b:
    print(i, end = "")
print()