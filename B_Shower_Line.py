from itertools import permutations
l = []
for i in range(5):
    k = list(map(int, input().split()))
    l.append(k)

perm = permutations([0,1,2,3,4])

ans = -1
for i in perm:
    temp = list(i)
    happi = 0
    while(len(temp) > 1):
        for j in range(0, len(temp), 2):
            if j < len(temp) - 1:
                happi += l[temp[j]][temp[j + 1]] + l[temp[j + 1]][temp[j]]
        temp.pop(0)
        
    if happi > ans:
        ans = happi
        
print(ans)