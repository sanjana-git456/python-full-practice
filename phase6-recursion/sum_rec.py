x = list(map(int, input("Enter numbers: ").split()))
def sumlist(n):
    if n == []:
        return 0
    else:
        return n[0] + sumlist(n[1:])
print(f"Sum is: {sumlist(x)}")