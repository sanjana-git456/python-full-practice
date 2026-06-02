x = input("Enter words: ").split()
d = {}
for i in x:
    s = ''.join(sorted(i))
    if s in d:
        d[s].append(i)
    else:
        d[s] = [i]
for key in d:
    print(f"{d[key]}")