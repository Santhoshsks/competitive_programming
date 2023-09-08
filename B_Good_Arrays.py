from collections import defaultdict

def check(d,s,n):
    if (s >= d + n and n > 1):
                return True
    return False

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = 0
    for i in l:
        if i == 1:
             d += 1
    if check(d, sum(l), n):
        print("YES")
    else:
        print("NO")