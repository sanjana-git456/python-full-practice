x = input("Enter string: ")
y = input("Enter string: ")
a = x + x
if len(x) != len(y):
    print(f"Lengths are not the same, hence {x} and {y} are not rotations of each other")
else:
    if y in a:
        print(f"{x} and {y} are rotation of each other")
    else:
        print(f"{x} and {y} are not rotations of each other")
