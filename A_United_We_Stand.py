for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] == a[-1]:
        print(-1)
    else:
        ind = 0
        while a[-1] != a[ind]:
            ind += 1
        print(ind,n - ind)
        print(' '.join(map(str,a[:ind])))
        print(' '.join(map(str,a[ind:])))