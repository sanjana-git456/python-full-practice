x = list(map(int, input("Enter first list: ").split())) #1 3 5
y = list(map(int, input("Enter second list: ").split())) #2 4 6
new = []
i = 0
j = 0
while i<len(x) and j<len(y):
    if x[i] < y[j]:
        new.append(x[i])
        i += 1
    else:
        new.append(y[j])
        j += 1
new += x[i:]
new += y[j:]
print(f"Merged list: {new}")