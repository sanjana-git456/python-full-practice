x = list(map(int, input("Enter first list: ").split()))
y = list(map(int, input("Enter second list: ").split()))
inters = []
u = []
t = x + y
for i in x:
    for j in y:
        if i == j:
            inters.append(i)
for i in t:
    if i not in u:
        u.append(i)
print(f"Intersection: {inters}")
print(f"Union: {u}")