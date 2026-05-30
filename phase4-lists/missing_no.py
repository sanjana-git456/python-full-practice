x = list(map(int, input("Enter numbers: ").split()))
l = len(x)
n = l+1
s = int(n*(n+1)/2)
a = 0
for i in range(l):
    a += x[i]
print(f"Missing number: {s-a}")