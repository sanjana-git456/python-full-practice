x = list(map(int, input("Enter numbers: ").split()))
t = int(input("Enter target: "))
def bin(n,t,left,right):
    if left > right:
        print("Not found")
        return
    mid = (left + right) // 2
    if t == n[mid]:
        print(f"Found at index {mid}")
    elif t < n[mid]:
        bin(n, t, left, mid-1)
    elif t > n[mid]:
        bin(n, t, mid+1, right)
left = 0
right = len(x)-1
bin(x, t, left, right)