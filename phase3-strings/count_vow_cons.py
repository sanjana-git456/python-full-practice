y = input("Enter string: ")
x = y.lower().replace(" ", "")
v = ["a", "e", "i", "o", "u"]
vc = 0
cc = 0
for i in x:
    if i in v:
        vc += 1
    else:
        cc += 1
print(f"Number of vowels in {y}: {vc}")
print(f"Number of consonants in {y}: {cc}")