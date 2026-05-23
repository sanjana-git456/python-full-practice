a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")
temp = a
a=b
b=temp
print(f"After swap: a = {a}, b = {b}")

print("One liner way")
c = int(input("Enter first number: "))
d = int(input("Enter second number: "))
print(f"Before swap: c = {c}, b = {d}")
c, d = d, c
print(f"After swap: c = {c}, d = {d}")