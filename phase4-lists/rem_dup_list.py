x = list(map(int, input("Enter numbers: ").split()))
a = []
for i in x:
    if i not in a:
        a.append(i)
print(f"List after removing duplicates: {a}")
s = set(x)
print(f"List after removing duplicates: {list(s)}")