x = 0
for _ in range(int(input())):
    i = input()
    if i == "X++" or i == "++X":
        x += 1
    else:
        x -= 1
print(x)