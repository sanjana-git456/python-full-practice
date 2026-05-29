x = list(map(int,input("Enter numbers: ").split()))
y = int(input("Enter target: "))
for i in range(len(x)):
    if x[i] == y:
        print(f"Linear search: Found at index {i}")
z = x.copy()
s = sorted(z)
left = 0
right = len(s) - 1
while left <= right:
    mid = (left+right) // 2
    if s[mid] == y:
        print(f"Binary search: Found at index {mid}")
        break
    elif y < s[mid]:
        right = mid - 1
    elif y > s[mid]:
        left = mid + 1
else:
    print(f"{y} is not present in the list")