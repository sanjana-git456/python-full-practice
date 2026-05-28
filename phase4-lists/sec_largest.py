x = list(map(int, input("Enter numbers: ").split()))
new = []

def largest(y):
        max_1 = y[0]
        for i in range(len(y)):
            if max_1 < y[i]:
                max_1 = y[i]
        return max_1

if len(x) == 1:
    print("Please enter more than 1 digit")
else:
    for i in x:
        if i == largest(x):
            continue
        else:
            new.append(i)
    if len(new) == 0:
        print("All numbers are the same")
    else:
        print(f"Second largest number: {largest(new)}")