for _ in range(int(input())):
    n , k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    new = 1
    maxi = 0
    for i in range(n):
        if i + 1 < n:
            if abs(l[i] - l[i+1]) <= k:
                new += 1
            else:
                new = 1
        maxi = max(new,maxi)
    print(n - maxi)
            