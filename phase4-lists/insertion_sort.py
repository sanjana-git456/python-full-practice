x = list(map(int, input("Enter numbers: ").split()))
l = len(x)
for i in range(1,l):
    key = x[i]
    j = i-1
    while j >= 0 and x[j] > key:
        x[j+1] = x[j]
        j -= 1
    x[j+1] = key
print(f"Sorted list: {x}")