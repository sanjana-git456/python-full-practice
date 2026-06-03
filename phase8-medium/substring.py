x = input("Enter string: ")
for i in range(len(x)):
    for j in range(i+1,len(x)+1):
        print(x[i:j], end = " ")