x = input("Enter words: ")
w = x.split()
d = {}
for i in w:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for key in d:
    print(f"{key}: {d[key]}")