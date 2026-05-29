x = list(map(int, input("Enter numbers: ").split()))
l = len(x)
for i in range(l):
    minimum = i
    for j in range(i+1, l):
        if x[i] > x[j]:
            minimum = j
    x[i], x[minimum] = x[minimum], x[i]
print(f"Selection sort: {x}")