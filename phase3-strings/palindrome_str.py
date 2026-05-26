x = input("Enter string: ")
y = x.lower()
rev = y[::-1]
if y == rev:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")