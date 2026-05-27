x = input("Enter string: ")
a = []
for i in x:
    if i not in a:
        a.append(i)
print(f"String after removing duplicates: {''.join(a)}")