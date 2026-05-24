x = int(input("Enter number: "))
if x < 0:
    x = abs(x)
s = str(x)
final = 0
for i in range(len(s)):
    final += int(s[i])
print(f"Sum of digits of {x} is: {final}")