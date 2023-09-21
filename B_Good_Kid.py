for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = l[0] + 1
    for i in range(1,n):
        ans *= l[i]
    print(ans)
