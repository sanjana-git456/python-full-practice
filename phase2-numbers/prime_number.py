x = int(input("Enter number: "))
a=0
if x<=0:
    print(f"{x} is not a prime number")
else:
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            a+=1
    if a == 0:
        print(f"{x} is a prime number")
    else:
        print(f"{x} is not a prime number")