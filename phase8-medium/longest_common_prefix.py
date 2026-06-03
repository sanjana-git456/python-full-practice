x = input("Enter words: ").split()
x.sort()
c = ""
for i,j in zip(x[0],x[-1]):
    if i == j:
        c += i
    else:
        break
if c == "":
    print("Longest common prefix: none")
else:
    print(f"Longest common prefix: {c}")