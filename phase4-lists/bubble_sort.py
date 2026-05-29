x = list(map(int, input("Enter numbers: ").split()))
l = len(x)
for i in range(l):
    for j in range(l-i-1):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
print(f"Sorted list using bubble sort: {x}")