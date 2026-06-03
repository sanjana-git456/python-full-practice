x = list(map(int, input("Enter numbers: ").split()))
d = {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for key in d:
    if d[key] == 1:
        print(f"{key} appears 1 time")
    else:
        print(f"{key} appears {d[key]} times")