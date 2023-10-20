lis = []
n = int(input())
sol = list(map(int,input().split()))

bound = 1001
for i in range(n - 1):
    if abs(sol[i] - sol[i + 1]) < bound:
        a = i + 1
        b = i + 2
        bound = abs(sol[i] - sol[i + 1])
if abs(sol[0] - sol[n - 1]) < bound:
    a = n
    b = 1
print(a,b)
