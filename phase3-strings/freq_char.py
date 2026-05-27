x = input("Enter string: ")
d = {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(f"Most frequent character: {max(d, key = d.get)}")