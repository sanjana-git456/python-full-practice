x = input("Enter string: ").lower()
k = int(input("Enter shift: "))
c = []
for j in range (len(x)):
    if x[j] == ' ':
        c.append(' ')
    else:
        c.append(chr((ord(x[j]) - 97 + k) % 26 + 97))
print(f"Encoded string: {''.join(c)}")