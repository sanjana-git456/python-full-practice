orig = list(map(int, input("Enter numbers: ").split()))
x = orig.copy()
y = orig.copy()
print(f"Reversed list: {x[::-1]}")
x.reverse()
print(f"Reversed list: {x}")
r = []
l = len(y)
for i in range(l):
    r.append(y[l-1])
    l -= 1
print(f"Reversed list: {r}")