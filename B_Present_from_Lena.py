n = int(input())

for i in range(n + 1):
    spaces = " " * (n - i)
    numbers = " ".join(str(j) for j in range(i))
    line = f"{spaces}{numbers} {numbers[::-1]}{spaces}"
    print(line)

for i in range(n - 1, -1, -1):
    spaces = " " * (n - i)
    numbers = " ".join(str(j) for j in range(i))
    line = f"{spaces}{numbers} {numbers[::-1]}{spaces}"
    print(line)
