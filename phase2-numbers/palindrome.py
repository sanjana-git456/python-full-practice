x = int(input("Enter number: "))
a = abs(x)
s = str(a)
rev = s[::-1]
if s == rev:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")