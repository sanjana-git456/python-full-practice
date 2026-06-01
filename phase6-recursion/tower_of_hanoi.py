x = int(input("Enter number: "))
def hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disc 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, helper)
    print(f"Move disc {n} from {source} to {destination}")
    hanoi(n-1, helper, source, destination)
hanoi(x, 'A', 'B', 'C')