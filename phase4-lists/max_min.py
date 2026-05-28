x = list(map(int, input("Enter numbers: ").split()))
maximum = x[0]
minimum = x[0] 
for i in range(len(x)):
    if maximum < x[i]:
        maximum = x[i]
    if minimum > x[i]:
        minimum = x[i]
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")