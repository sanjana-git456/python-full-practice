x = input("Enter brackets: ")
s = []
d = {')': '(', '}': '{', ']': '['}
for i in x:
    if i in "({[":
        s.append(i)
    elif i in ")}]":
        if len(s) == 0 or s[-1] != d[i]:
            print("Not balanced")
            break
        else:
            s.pop()
    else:
        print("Wrong input")
if s == []:
    print("Balanced")