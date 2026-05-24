x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Euclidean method:")
def gcd(x,y):
    while y:
        x, y = y, x%y
    return x
def lcm(x,y):
    return (x*y) // gcd(x,y)
print(f"GCD of {x} and {y} is: {gcd(x,y)}")
print(f"LCM of {x} and {y} is: {lcm(x,y)}")