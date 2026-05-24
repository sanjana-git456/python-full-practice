x = int(input("Enter number: "))
s=0
for i in range(1, x):
    if x%i == 0:
        s+=i
if s == x:
    print(f"{x} is a perfect number")
else:
    print(f"{x} is not a perfect number")