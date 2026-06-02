x = list(map(int, input("Enter numbers: ").split()))
d = {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print("Duplicates:")
for i in d:
    if d[i] > 1:
        print(i)