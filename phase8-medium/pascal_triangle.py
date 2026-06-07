x = int(input("Enter rows: "))
l = [[1]]
for i in range(1,x):
    prev = l[-1]
    row = [1]
    for j in range(len(prev)-1):
        row.append(prev[j] + prev[j+1])
    row.append(1)
    l.append(row)
for row in l:
    print(' '.join(map(str, row)))