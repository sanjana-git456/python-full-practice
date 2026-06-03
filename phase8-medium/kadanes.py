x = list(map(int, input("Enter numbers: ").split()))
c = x[0]
m = x[0]
for i in range(1,len(x)):
    c = max(x[i],c+x[i])
    m = max(m,c)
print(f"Maximum subarray sum: {m}")