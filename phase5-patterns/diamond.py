x = int(input("Enter number: "))
for i in range(1, x+1):
    print(" "*(x-i) + "* "*i)
i = x-1
while i > 0:
    print(" "*(x-i) + "* "*i)
    i -= 1