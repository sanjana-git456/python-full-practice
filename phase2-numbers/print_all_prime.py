x = int(input("Enter number: "))
def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

print(f"Primary numbers till {x} are:")

for i in range(2,x+1):
    if prime(i):
        print(i, end = " ")