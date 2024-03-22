m, n, d = map(int, input().split())

mat = []
for _ in range(m):
    t = list(map(int, input().split()))
    mat.extend(t)

ans = 0
mat.sort()

def check(num):
    mini = 0
    for i in mat:
        if abs(num - i) % d == 0:
            mini += abs(num - i) // d
        else:
            return -1
    return mini

ans = float('inf')

for i in range(mat[-1]+1):
    temp = check(i)
    if  temp < ans and temp != -1:
        ans = temp

if ans != float('inf'):
    print(ans)
else:
    print(-1)
    
    