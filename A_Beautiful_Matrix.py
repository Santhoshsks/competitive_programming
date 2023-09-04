for i in range(5):
    coli = list(map(int,input().split()))
    for j in range(5):
        if coli[j] == 1:
            row = i
            col = j

print(abs(row - 2) + abs(col - 2))

