print("Matrix A:")
r1 = list(map(int, input("Enter row 1: ").split()))
r2 = list(map(int, input("Enter row 2: ").split()))
m1 = [r1, r2]
print("Matrix B:")
r3 = list(map(int, input("Enter row 1: ").split()))
r4 = list(map(int, input("Enter row 2: ").split()))
m2 = [r3, r4]
a = []
for i in range(len(m1)):
    row = []
    for j in range(len(m2)):
        row.append(m1[i][j] + m2[i][j])
    a.append(row)
print("Addition:")
for row in a:
    print(row)

m = []
for i in range(len(m1)):
    row = []
    for j in range(len(m2)):
        s = 0
        for k in range(len(m1)):
            s += m1[i][k] * m2[k][j]
        row.append(s)
    m.append(row)
print("Multiplication:")
for row in m:
    print(row)