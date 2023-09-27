inp = []
out = []
for _ in range(3):
    l = list(map(int, input().split()))
    inp.append(l)
    out.append([0,0,0])

for i in range(3):
    for j in range(3):
        ans = inp[i][j]
        if i + 1 < 3:
            ans += inp[i + 1][j]
        if i - 1 > -1:
            ans += inp[i - 1][j]
        if j + 1 < 3:
            ans += inp[i][j + 1]
        if j - 1 > -1:
            ans += inp[i][j - 1]
        if ans == 0:
            out[i][j] = 1
        elif ans % 2:
            out[i][j] = 0
        elif ans % 2 == 0:
            out[i][j] = 1  

for i in range(3):
    ans = "".join(map(str, out[i]))
    print(ans)