x = list(map(int, input("Enter numbers: ").split()))
a = []
b = []
for i in x:
    if i == 0:
        b.append(i)
    else:
        a.append(i)
print(f"After moving zeros: {a+b}")