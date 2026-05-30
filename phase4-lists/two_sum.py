x = list(map(int, input("Enter numbers: ").split()))
t = int(input("Enter target: "))
found = False
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if (x[i] + x[j]) == t:
            print(f"Numbers at index {i} and {j} add up to {t}")
            found = True
            break
    if found:
        break
if not found:
    print("Cannot happen")

d = {}
for i in range(len(x)):
    complement = t-x[i]
    if complement in d:
        print(f"Numbers at index {d[complement]} and {i} add up to {t}")
        break
    d[x[i]] = i