n = int(input())
arr = list(map(int, input().split()))

mapa = []
for i in range(n):
    mapa.append([arr[i], i])

l = sorted(mapa, key=lambda x : x[0])

ans = []
prev = -1
diff = 0
skip = -1

for i in range(n):
    if l[i][0] != skip:
        if l[i][0] != prev and prev != -1:
            ans.append([l[i - 1][0], diff])
            diff = 0

        else:
            if diff != 0:
                if l[i - 1][1] + diff != l[i][1]:
                    skip = l[i][0]
            else:
                if prev != -1:
                    diff = l[i][1] - l[i - 1][1]
        if i == n - 1:
            ans.append([l[i][0], diff])
                
    prev = l[i][0]

print(len(ans))
for i in ans:
    print(i[0],i[1])