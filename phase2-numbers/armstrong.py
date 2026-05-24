x = int(input("Enter number: "))
a = str(x)
l = len(a)
s = 0

for i in range(l):
    s += int(a[i])**l
if s == x:
    print(f"{x} is an Armstrong number")
else:
    print(f"{x} is not an Armstrong number")