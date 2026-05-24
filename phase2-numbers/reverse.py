x = int(input("Enter number: "))
def reverse(x):
    s = str(x)
    return int(s[::-1])
if x<0:
    y = abs(x)
    print(f"Reversed number of {x} is: -{reverse(y)}")
else:
    print(f"Reversed number of {x} is: {reverse(x)}")