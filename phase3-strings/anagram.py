x = input("Enter first string: ")
y = input("Enter second string: ")
a = sorted(x.lower())
b = sorted(y.lower())
if a == b:
    print(f"{x} and {y} are anagrams")
else:
    print(f"{x} and {y} are not anagrams")